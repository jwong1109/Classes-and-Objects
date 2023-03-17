class Student:
    def __init__(self, name, age, phone_num, form_class, subjects, is_male,):
        self.name = name
        self.age = age  # Integer
        self.phone_num = phone_num  # string ""
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = is_male
        self.enrolled = True
        student_list.append(self)

    def student_details(self):
        print(self.name)
        print(self.age)
        print(self.phone_num)
        print(self.form_class)
        print(self.subjects)
        print(self.is_male)
        print(self.enrolled)
        print("##################")


def display_info():
    for student in student_list:
        student.student_details()


def select_student_age():
    count_age = 0
    age = int(input("Display the info for this age or more: "))
    for student in student_list:
        if student.age > age:
            student.student_details()
            count_age += 1
    print(f"There are {count_age} students with the age of {age}!")


def generate_students():
    # available form classes are "BAKER", "MORGAN", "MCNICOL", "GRAHAM",
    # "BELL", "NIMMO", "BARKER"
    # available classes are: "ART", "ENG", "MAT", "GRA", "DTC", "PHY", "BIO"
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4],
                    is_male)


def count_students():
    count = 0
    input_class = input("What class are you looking for? ")
    for student in student_list:
        if input_class in student.subjects:
            count += 1
    if count == 0:
        print(f"There are no students in this {input_class}")
    else:
        print(f"There are {count} students in this {input_class}")


def find_student():
    student_to_find = input("Enter the name of the student: ").title()
    for student in student_list:
        if student.name == student_to_find:
            print("#####################")
            print(f"Name: {student_to_find}")
            print("#####################")
            print(f"Age: {student.age}")
            print(f"Phone Number: {student.phone_num}")
            print(f"Form Class: {student.form_class}")
            print(f"Classes: {student.subjects}")

            if student.is_male:
                print(f"{student_to_find} is male")
            else:
                print(f"{student_to_find} is female")

            print(f"Enrolled: {True}")
            return student_to_find

    print("Sorry, no student was found with that name")
    return None


# Main Routine
student_list = []
generate_students()

# select_student_age()
# display_info()
# count_students()
# find_student()

# User menu
new_action = True
while new_action:
    print("1. Count students taking a particular subject")
    print("2. Print a full list of all students")
    print("3. Print a list of students above a particular age")
    print("4. Get details of a particular student")

    choice = input("\nWhat would you like to do? - enter a number or 'Q' to "
                   "exit: ").title()
    if choice == "1":
        count_students()
    elif choice == "2":
        display_info()
    elif choice == "3":
        select_student_age()
    elif choice == "4":
        find_student()
    elif choice == "Q":
        print("Goodbye")
        new_action = False
    else:
        print("\n*** That was not a valid choice ***\n")
