import argparse
import csv
import os

def main():
    csv.field_size_limit(1000000000)
    parser = argparse.ArgumentParser(description='Create a shorter CSV with selected columns')
    parser.add_argument('csv', metavar='csv', help='the name of the csv with the original data')
    parser.add_argument('output_csv', metavar='output_csv', help='the name of the output csv')
    parser.add_argument('columns', metavar='columns', nargs='+', help='the columns to include in the output csv')

    args = parser.parse_args()
    csv_name = args.csv
    output_csv_name = args.output_csv
    selected_columns = args.columns

    if not csv_name.endswith(".csv"):
        csv_name = csv_name + ".csv"
    if not output_csv_name.endswith(".csv"):
        output_csv_name = output_csv_name + ".csv"

    with open(csv_name, 'rt') as csvfile, open(output_csv_name, 'w', newline='') as output_csvfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(output_csvfile, fieldnames=selected_columns)

        writer.writeheader()
        for row in reader:
            filtered_row = {col: row[col] for col in selected_columns if col in row}
            writer.writerow(filtered_row)

if __name__ == "__main__":
    main()