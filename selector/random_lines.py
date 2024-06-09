import random

# File names
input_file_1 = 'list'
input_file_2 = 'Channels'
output_file = 'selector/random'

# Number of lines to select
num_lines_to_select = 10

def select_random_lines(input_file_1, input_file_2, output_file, num_lines):
    with open(input_file_1, 'r') as f1, open(input_file_2, 'r') as f2:
        lines = f1.readlines() + f2.readlines()

    # Ensure we do not exceed the number of available lines
    num_lines = min(num_lines, len(lines))
    
    # Randomly sample lines without replacement
    selected_lines = random.sample(lines, num_lines)
    
    with open(output_file, 'w') as f:
        f.writelines(selected_lines)

if __name__ == "__main__":
    select_random_lines(input_file_1, input_file_2, output_file, num_lines_to_select)
