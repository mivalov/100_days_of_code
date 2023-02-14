# Day 64: OOP

class Job:
    name = None
    salary = None
    hours_worked = None

    def __init__(self, name, salary, hours_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked

    def print_details(self):
        """Display details nicely."""
        print(
            f'Job type: {self.name}',
            f'Salary: {self.salary}',
            f'Hours worked: {self.hours_worked}',
            sep='\n',
            end='\n\n'
        )


class Doctor(Job):
    specialty = None
    years_xp = None

    def __init__(self, name, salary, hours_worked, specialty, years_xp):
        super().__init__(name, salary, hours_worked)
        self.specialty = specialty
        self.years_xp = years_xp

    def print_details(self):
        """Display details nicely."""
        print(
            f'Job type: {self.name}',
            f'Salary: {self.salary}',
            f'Hours worked: {self.hours_worked}',
            f'Specialty: {self.specialty}',
            f'Years of Experience: {self.years_xp}',
            sep='\n',
            end='\n\n'
        )


class Teacher(Job):
    subject = None
    position = None

    def __init__(self, name, salary, hours_worked, subject, position):
        super().__init__(name, salary, hours_worked)
        self.subject = subject
        self.position = position

    def print_details(self):
        """Display details nicely."""
        print(
            f'Job type: {self.name}',
            f'Salary: {self.salary}',
            f'Hours worked: {self.hours_worked}',
            f'Subject: {self.subject}',
            f'Position: {self.position}',
            sep='\n',
            end='\n\n'
        )


def main() -> None:
    title = '🌟Jobs Jobs Jobs!🌟\n'
    print(title)
    lawyer = Job('Lawyer', '35.000 €', '40')
    lawyer.print_details()
    doctor = Doctor('Doctor', '60.000 €', '40', 'Internal Medicine', '10')
    doctor.print_details()
    teacher = Teacher('Teacher', '40.000 €', '40', 'Biology',
                      'Classroom Teacher')
    teacher.print_details()


if __name__ == '__main__':
    main()
