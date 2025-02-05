import csv
import argparse
from statistics import mean, median

# Function to determine the distance range
def get_distance_range(distance):
    lower_bound = int(distance * 10) / 10
    upper_bound = lower_bound + 0.1
    return f"{lower_bound:.1f}-{upper_bound:.1f}"

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Process CSV file paths.')
parser.add_argument('input_file', type=str, help='Path to the input CSV file')
parser.add_argument('output_file', type=str, help='Path to the output CSV file')
args = parser.parse_args()

# Read the CSV file and group data by distance ranges
distance_groups = {}
with open(args.input_file, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        distance = float(row['distance'])
        kudos = int(row['kudos'])
        hits = int(row['hits'])
        kudos_percentage = float(row['kudos_percentage'])
        hits_percentage = float(row['hits_percentage'])
        distance_range = get_distance_range(distance)
        if distance_range not in distance_groups:
            distance_groups[distance_range] = {'kudos': [], 'hits': [], 'kudos_percentage': [], 'hits_percentage': []}
        distance_groups[distance_range]['kudos'].append(kudos)
        distance_groups[distance_range]['hits'].append(hits)
        distance_groups[distance_range]['kudos_percentage'].append(kudos_percentage)
        distance_groups[distance_range]['hits_percentage'].append(hits_percentage)

# Calculate median, average kudos, average hits, and count for each distance range
results = []
for distance_range, data in distance_groups.items():
    median_kudos = median(data['kudos'])
    average_kudos = mean(data['kudos'])
    median_hits = median(data['hits'])
    average_hits = mean(data['hits'])
    median_kudos_percentage = median(data['kudos_percentage'])
    average_kudos_percentage = mean(data['kudos_percentage'])
    median_hits_percentage = median(data['hits_percentage'])
    average_hits_percentage = mean(data['hits_percentage'])
    count = len(data['kudos'])
    results.append({
        'distance_range': distance_range,
        'median_kudos': median_kudos,
        'average_kudos': average_kudos,
        'median_hits': median_hits,
        'average_hits': average_hits,
        'median_kudos_percentage': median_kudos_percentage,
        'average_kudos_percentage': average_kudos_percentage,
        'median_hits_percentage': median_hits_percentage,
        'average_hits_percentage': average_hits_percentage,
        'count': count
    })

# Sort the results by distance range
results = sorted(results, key=lambda x: float(x['distance_range'].split('-')[0]))


# Write the results to the output CSV file
with open(args.output_file, mode='w', newline='') as csvfile:
    fieldnames = ['distance_range', 'median_kudos', 'average_kudos', 'median_hits', 'average_hits', 'median_kudos_percentage', 'average_kudos_percentage', 'median_hits_percentage', 'average_hits_percentage', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow(result)