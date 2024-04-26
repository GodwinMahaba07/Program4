def highest_gwa(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return

    max_gwa = 5
    top_student = None

    for line in lines:
        name, gwa = line.strip().split(',')
        gwa = float(gwa)
        if gwa < max_gwa:
            max_gwa = gwa
            top_student = (name, gwa)

    if top_student:
        print(f"The student with the highest GWA is {top_student[0]} with a GWA of {top_student[1]}")
    else:
        print("No data found.")


highest_gwa("students_gwa.txt")
