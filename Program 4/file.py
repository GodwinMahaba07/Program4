def process_integers(input_file, output_file_even, output_file_odd):
    try:
        with open(input_file, 'r') as file:
            integers = [int(num) for num in file.readlines()]
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return

    even_numbers = [num ** 2 for num in integers if num % 2 == 0]
    odd_numbers = [num ** 3 for num in integers if num % 2 != 0]

    try:
        with open(output_file_even, 'w') as file:
            file.write('\n'.join(map(str, even_numbers)))
        print(f"Square of even numbers saved to {output_file_even}")

        with open(output_file_odd, 'w') as file:
            file.write('\n'.join(map(str, odd_numbers)))
        print(f"Cube of odd numbers saved to {output_file_odd}")
    except IOError:
        print("Error writing to output files.")

    # Displaying all the outputs
    print("Squares of even numbers:")
    print('\n'.join(map(str, even_numbers)))

    print("Cubes of odd numbers:")
    print('\n'.join(map(str, odd_numbers)))


# Example usage:
process_integers("integers.txt", "double.txt", "triple.txt")
