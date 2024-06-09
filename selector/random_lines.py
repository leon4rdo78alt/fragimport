import random

# File names
input_file_1 = 'list'
input_file_2 = 'gitChannels'
output_file = 'selector/random'

# Number of lines to select
num_lines_to_select = 10

def select_random_lines(input_file_1, input_file_2, output_file, num_lines):
    selected_lines = set()  # Set to keep track of selected lines

    # Read lines from first file
    with open(input_file_1, 'r') as f1:
        lines_1 = set(f1.readlines())

    # Read lines from second file
    with open(input_file_2, 'r') as f2:
        lines_2 = set(f2.readlines())

    # Randomly sample lines from the first file
    selected_lines.update(random.sample(lines_1, min(num_lines, len(lines_1))))

    # Randomly sample lines from the second file
    selected_lines.update(random.sample(lines_2, min(num_lines - len(selected_lines), len(lines_2))))

    # Write selected lines to output file
    with open(output_file, 'w') as f:
        f.writelines(selected_lines)

if __name__ == "__main__":
    select_random_lines(input_file_1, input_file_2, output_file, num_lines_to_select)
