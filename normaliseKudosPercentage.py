import pandas as pd
import sys

def normalize_kudos(input_csv, output_csv):
    # Load the CSV file
    df = pd.read_csv(input_csv)

    # Calculate the total kudos and hits
    total_kudos = df['kudos'].sum()
    total_hits = df['hits'].sum()

    # Normalize the kudos and hits columns to percentage of total kudos and hits
    df['kudos_percentage'] = (df['kudos'] / total_kudos) * 100
    df['hits_percentage'] = (df['hits'] / total_hits) * 100

    # Save the result to a new CSV file
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python normaliseKudosPercentage.py <input_csv> <output_csv>")
    else:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]
        normalize_kudos(input_csv, output_csv)