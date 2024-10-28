import pandas as pd
import glob

# Specify the folder where your files are stored
folder_path = "/Users/changsin/Downloads/naver_stats_bk/"

# Find all Excel files in the folder
excel_files = glob.glob(folder_path + "*.xlsx")

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through each file
for file in excel_files:
    # Read the file starting from row 9 (index 8)
    df = pd.read_excel(file, skiprows=7)
    df.columns = ["rank", "title", "hits", "date"]
    # Append to the combined DataFrame
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# # Save the combined data to a new Excel file
# combined_data.to_excel("merged_data.xlsx", index=False)
# Group by the title in column B and sum the hits in column C
# Assuming titles are in column 'B' and hits in column 'C'
result = combined_data.groupby('title', as_index=False).agg({
    # 'rank': 'first',
    'hits': 'sum',               # Sum the values in Hits for each Title
    'date': 'first'      # Take the first value in Other_Column for each Title
})
result = result.sort_values(by='hits', ascending=False).reset_index(drop=True)

filename_out = "merged_data_with_summed_hits.xlsx"
# Save the combined data to a new Excel file
result.to_excel(filename_out, index=False)

print(f"Data merged successfully into {filename_out}")
