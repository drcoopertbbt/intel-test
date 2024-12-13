from datasets import load_from_disk
import os

# Use absolute path or verify the relative path
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(script_dir, "nvd_testing_data_10Dec24.hf")

# Verify directory exists before trying to load it
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Dataset directory not found at: {dataset_path}")

# Load the dataset using Hugging Face's datasets library
dataset = load_from_disk(dataset_path)

# Convert to pandas DataFrame (if needed)
df = dataset.to_pandas()

# Get basic dataset information
print("Dataset shape:", df.shape)
print("\nColumns:", df.columns.tolist())

# Get description length statistics
print("\nDescription lengths:")
print(df['description'].str.len().describe())

# Print complete example of text field
print("\nComplete example of 'text' field:")
print(df['text'].iloc[0])