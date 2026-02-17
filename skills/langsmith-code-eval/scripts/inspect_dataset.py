"""
Dataset Structure Inspector for LangSmith

Use this to understand the structure of your dataset before building an evaluator.
"""

from langsmith import Client
from typing import Optional
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file (searches cwd and parent directories)
load_dotenv(find_dotenv(usecwd=True))


def inspect_dataset_structure(
    dataset_name: str,
    num_examples: int = 3
) -> dict:
    """
    Inspect the structure of a LangSmith dataset.

    Args:
        dataset_name: The LangSmith dataset name
        num_examples: Number of examples to inspect (default 3)

    Returns:
        dict with structure information
    """
    client = Client()

    # Fetch dataset
    dataset = client.read_dataset(dataset_name=dataset_name)

    print("=" * 80)
    print("DATASET STRUCTURE ANALYSIS")
    print("=" * 80)
    print(f"\nDataset: {dataset.name}")
    print(f"ID: {dataset.id}")

    # Get examples
    examples = list(client.list_examples(dataset_name=dataset_name, limit=num_examples))

    if not examples:
        print("\nNo examples found in dataset")
        return {"dataset_name": dataset_name, "num_examples": 0}

    print(f"\nTotal examples inspected: {len(examples)}")

    structure = {
        "dataset_name": dataset_name,
        "dataset_id": str(dataset.id),
        "num_examples": len(examples),
        "inputs": {},
        "outputs": {},
        "metadata": {},
    }

    # Analyze inputs structure
    print("\n" + "=" * 80)
    print("INPUTS STRUCTURE")
    print("=" * 80)

    all_input_keys = set()
    for ex in examples:
        if ex.inputs:
            all_input_keys.update(ex.inputs.keys())

    if all_input_keys:
        print(f"\nInput keys found: {list(all_input_keys)}")
        structure["inputs"]["keys"] = list(all_input_keys)

        # Show sample values from first example
        first_ex = examples[0]
        print("\nSample values (first example):")
        for key in all_input_keys:
            value = first_ex.inputs.get(key)
            if value is not None:
                value_type = type(value).__name__
                sample = str(value)[:100]
                print(f"  {key} ({value_type}): {sample}{'...' if len(str(value)) > 100 else ''}")
                structure["inputs"][key] = {"type": value_type}
    else:
        print("\nNo inputs found")

    # Analyze outputs structure
    print("\n" + "=" * 80)
    print("OUTPUTS STRUCTURE (reference/expected)")
    print("=" * 80)

    all_output_keys = set()
    for ex in examples:
        if ex.outputs:
            all_output_keys.update(ex.outputs.keys())

    if all_output_keys:
        print(f"\nOutput keys found: {list(all_output_keys)}")
        structure["outputs"]["keys"] = list(all_output_keys)

        # Show sample values from first example
        first_ex = examples[0]
        print("\nSample values (first example):")
        for key in all_output_keys:
            value = first_ex.outputs.get(key) if first_ex.outputs else None
            if value is not None:
                value_type = type(value).__name__
                sample = str(value)[:100]
                print(f"  {key} ({value_type}): {sample}{'...' if len(str(value)) > 100 else ''}")
                structure["outputs"][key] = {"type": value_type}
    else:
        print("\nNo outputs found (dataset may not have reference outputs)")

    # Analyze metadata structure
    print("\n" + "=" * 80)
    print("METADATA STRUCTURE")
    print("=" * 80)

    all_metadata_keys = set()
    metadata_values = {}
    for ex in examples:
        if ex.metadata:
            all_metadata_keys.update(ex.metadata.keys())
            for key, value in ex.metadata.items():
                if key not in metadata_values:
                    metadata_values[key] = []
                metadata_values[key].append(value)

    if all_metadata_keys:
        print(f"\nMetadata keys found: {list(all_metadata_keys)}")
        structure["metadata"]["keys"] = list(all_metadata_keys)

        print("\nMetadata values across examples:")
        for key in all_metadata_keys:
            values = metadata_values.get(key, [])
            unique_values = list(set(str(v) for v in values))
            value_type = type(values[0]).__name__ if values else "unknown"

            print(f"  {key} ({value_type}):")
            if len(unique_values) <= 5:
                print(f"    Unique values: {unique_values}")
            else:
                print(f"    Sample values: {unique_values[:5]} ... ({len(unique_values)} unique)")

            structure["metadata"][key] = {
                "type": value_type,
                "unique_values": unique_values[:10]
            }
    else:
        print("\nNo metadata found")

    # Recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS FOR EVALUATOR")
    print("=" * 80)

    if all_metadata_keys:
        print("\n✓ Dataset has metadata - check for ground truth labels")
        print(f"  Available metadata keys: {list(all_metadata_keys)}")
        print("  Access via: example.metadata.get('key_name')")

    if all_output_keys:
        print("\n✓ Dataset has reference outputs")
        print(f"  Available output keys: {list(all_output_keys)}")
        print("  Access via: example.outputs.get('key_name')")

    print("\n" + "=" * 80)
    return structure


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python inspect_dataset.py <dataset_name> [num_examples]")
        print("\nExample:")
        print("  python inspect_dataset.py my-dataset")
        print("  python inspect_dataset.py my-dataset 5")
        sys.exit(1)

    dataset_name = sys.argv[1]
    num_examples = int(sys.argv[2]) if len(sys.argv) > 2 else 3

    structure = inspect_dataset_structure(dataset_name, num_examples)
