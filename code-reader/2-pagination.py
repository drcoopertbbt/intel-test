from IPython.display import clear_output
import pandas as pd

class DataFramePaginator:
    def __init__(self, df, rows_per_page=5):
        self.df = df
        self.rows_per_page = rows_per_page
        self.current_page = 0
        self.total_pages = len(df) // rows_per_page + (1 if len(df) % rows_per_page else 0)

    def show_page(self):
        clear_output(wait=True)
        start_idx = self.current_page * self.rows_per_page
        end_idx = start_idx + self.rows_per_page
        
        print(f"\nPage {self.current_page + 1} of {self.total_pages}")
        print("-" * 80)
        
        for idx in range(start_idx, min(end_idx, len(self.df))):
            row = self.df.iloc[idx]
            print(f"\nRecord {idx + 1}:")
            print("Description:", row['description'][:200] + "..." if len(row['description']) > 200 else row['description'])
            print("\nText:", row['text'][:200] + "..." if len(row['text']) > 200 else row['text'])
            print("-" * 80)
        
        print("\nCommands: 'n' for next page, 'p' for previous page, 'q' to quit")

    def navigate(self):
        while True:
            self.show_page()
            command = input("\nEnter command (n/p/q): ").lower()
            
            if command == 'n' and self.current_page < self.total_pages - 1:
                self.current_page += 1
            elif command == 'p' and self.current_page > 0:
                self.current_page -= 1
            elif command == 'q':
                break
            else:
                print("Invalid command or can't move in that direction!")

# Use it with your existing code:
from datasets import load_from_disk
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(script_dir, "nvd_testing_data_10Dec24.hf")
dataset = load_from_disk(dataset_path)
df = dataset.to_pandas()

# Create and use the paginator
paginator = DataFramePaginator(df, rows_per_page=3)  # Show 3 records at a time
paginator.navigate()