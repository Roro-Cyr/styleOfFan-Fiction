import argparse

def process_line(line):
    elements = line.split()
    if len(elements) > 2:
        return f"{elements[0]} {elements[-2]} {elements[-1]}"
    elif len(elements) > 1:
        return f"{elements[0]} {elements[-1]}"
    return line.strip()

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line in lines[1:]:  # Skip the first line
            processed_line = process_line(line)
            outfile.write(processed_line + '\n')

def main():
    parser = argparse.ArgumentParser(description='Process a file.')
    parser.add_argument('input_file', type=str, help='The input file to process')
    parser.add_argument('output_file', type=str, help='The output file to write to')
    args = parser.parse_args()

    process_file(args.input_file, args.output_file)

if __name__ == '__main__':
    main()