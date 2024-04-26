# To open and read the file
with open("numbers.txt", "r") as my_file:
    lines = my_file.readlines()

even_numbers = []
odd_numbers = []

for line in lines:
    numbers = line.split()

    for num in numbers:
        num = int(num)
        if num %2 == 0:
            even_numbers.append(num)
        else: 
            odd_numbers.append(num)

print("Even:", even_numbers)
print("Odd:", odd_numbers)


