def write_numbers_file(numbers, filename):
    with open(filename,"w") as file:
        for num in numbers:
            file.write(str(num) + "\n")


user_input = input("Enter Odd,Even, or Numbers:")

if user_input == "Odd":
    with open("odd.txt", "r") as file:
        print (file.read())
elif user_input == "Even":
    with open("even.txt", "r" ) as file:
        print(file.read())
elif user_input == "Numbers":
    with open("numbers.txt", "r") as file:
        print(file.read())
else:
    print("Invalid, Please enter Odd,Even, or Numbers")