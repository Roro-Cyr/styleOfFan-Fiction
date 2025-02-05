import csv
import sys

def merge_files(csv_file_path, txt_file_path, output_file_path):
    # Read the CSV file into a dictionary
    csv_data = {}
    with open(csv_file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Remove commas from kudos and strip surrounding double quotes
            kudos = row['kudos'].replace(',', '').strip('"')
            hits = row['hits'].replace(',', '').strip('"')
            csv_data[row['work_id']] = {'kudos': kudos, 'hits': hits}

    # Read the TXT file into a dictionary
    txt_data = {}
    with open(txt_file_path, mode='r') as txtfile:
        for line in txtfile:
            work_id, distance = line.strip().split()
            work_id = work_id.strip('"')  # Remove the surrounding double quotes
            txt_data[work_id] = distance

    # Merge the dictionaries
    merged_data = []
    for work_id, values in csv_data.items():
        if work_id in txt_data:
            merged_data.append({
                'work_id': work_id,
                'kudos': values['kudos'],
                'hits': values['hits'],
                'distance': txt_data[work_id]
            })

    # Write the merged data to a new CSV file
    with open(output_file_path, mode='w', newline='') as csvfile:
        fieldnames = ['work_id', 'kudos', 'hits', 'distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in merged_data:
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python zipDistanceKudos.py <csv_file_path> <txt_file_path> <output_file_path>")
    else:
        csv_file_path = sys.argv[1]
        txt_file_path = sys.argv[2]
        output_file_path = sys.argv[3]
        merge_files(csv_file_path, txt_file_path, output_file_path)