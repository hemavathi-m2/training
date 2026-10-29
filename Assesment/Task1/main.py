import pandas as pd

# Read employee data
df = pd.read_csv("employees.csv")


# 1. Bonus function: *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


print("Bonus:", bonus(50000, 0.1, 500, 1000, cap=6000))


# 2. Custom exception
class InvalidSalaryError(Exception):
    pass


# 3. Employee class
class Employee:

    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee:{self.name},Salary:{self.salary}"


# 4. Manager inheritance and method overriding
class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager:{self.name},Salary:{self.salary}," f"Team size:{self.team_size}"
        )


emp = Employee("Hema", 50000)
print(emp.get_details())
print("Annual salary:", emp.annual_salary())

man = Manager("Aarthi", 65000, 5)
print(man.get_details())


# 5. List comprehension: Salary above 50000
high_salary_names = [
    name for name, salary in zip(df["name"], df["salary"]) if salary > 50000
]

print("Above 50000:", high_salary_names)


# 6. map() and lambda: 10% salary raise
salaries = df["salary"].tolist()

raised_salaries = list(map(lambda salary: round(salary * 1.10, 2), salaries))

print("Salaries after 10% raise:", raised_salaries)


# 7. filter() and lambda: Chennai employees
employees = df.to_dict("records")

chennai_employees = list(filter(lambda emp: emp["city"] == "Chennai", employees))

chennai_names = [emp["name"] for emp in chennai_employees]

print("Chennai:", chennai_names)


# 8. Custom exception handling
try:
    emp2 = Employee("Test", -500)

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction finished")


# 9. continue and break
test_salaries = [0] + salaries

for salary in test_salaries:

    if salary == 0:
        continue

    if salary > 85000:
        #print("Salary above 85000 found. Stopping.")
        break
