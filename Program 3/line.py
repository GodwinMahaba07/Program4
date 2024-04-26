def write_to_file(file_name):
    try:
        with open(file_name, 'w') as file:
            while True:
                line = input("Enter line: ")
                file.write(line + '\n')
                more_lines = input("Are there more lines y/n? ")
                if more_lines.lower() != 'y':
                    break
        print(f"Contents written to {file_name}")
    except IOError:
        print("Error writing to file.")

write_to_file("mylife.txt")
