output_file = "output.txt"
input_file = "input.txt"

# breaks file into sections
delimiter_char = input("Enter delimiter string. Leave blank if none.\n> ")

# storage for writing to file
out_data = []

if delimiter_char:
    data = open(input_file, 'r').read().split(delimiter_char)
    for section in data:
        # breaks sections into lines to output somewhere
        for line in section.split('\n'):
            # look for whatever you want to output
            if 'no' in line:
                out_data.append(line)
                print(out_data)
else:
    data = open(input_file, 'r').readlines()
    # goes through each line to output somewhere
    for line in data:
        # look for whatever you want to output
        if 'no' in line:
            out_data.append(line.strip('\n'))
            print(out_data)