class AllStaff:
    def __init__(self, name, age, emp_id, birth_date, job_title):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.birth_date = birth_date
        self.job_title = job_title

    def show(self):
        print(f"{self.emp_id} is {self.name} aged {self.age} being born "
              f"{self.birth_date} employed as {self.job_title}")


# Child classes contain attributes unique to that class
class Management(AllStaff):
    def __init__(self, name, age, emp_id, birth_date, job_title, car):
        # Adds car attribute - unique to Management
        super().__init__(name, age, emp_id, birth_date, job_title)  # Gets
# name and age attributes from superclass-AllStaff
        self.car = car

    def show(self):
        print(f"{self.emp_id} is {self.name} aged {self.age} being born "
              f"{self.birth_date} employed as {self.job_title} and drives a "
              f"{self.car}")


class Clerical(AllStaff):
    def __init__(self, name, age, emp_id, birthdate, job_title,
                 typing_speed):  # Adds unique attribute typing speed
        super().__init__(name, age, emp_id, birthdate, job_title)  # Gets
        # name and age attributes from superclass-AllStaff
        self.typing_speed = typing_speed

    def show(self):
        print(f"{self.emp_id} is {self.name} aged {self.age} being born "
              f"{self.birth_date} employed as {self.job_title} and with a "
              f"typing speed of {self.typing_speed} words per minute")


class Factory(AllStaff):
    pass  # No unique attributes


# Main routine
a = Management("Jenny", 22, "ID007", "20/12/2000", "Managing Director",
               "Jaguar")
a.show()
print()

b = Clerical("Tim", 17, "ID119", "01/01/2005", "Secretary", 123)
b.show()
print()

c = Factory("Jake", 16, "ID125", "17/08/2006", "Labourer")
c.show()
print()
