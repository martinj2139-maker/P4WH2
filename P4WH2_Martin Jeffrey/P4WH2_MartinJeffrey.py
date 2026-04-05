# Jeffrey Martin
# 4/05/2024
# P4HW2_Salary_MartinJeffrey.py
# Salary Calculator with Loops

# Create Accumulator Variables for overtime pay, regular pay, gross pay and employee count
overtime_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

# request employee info
name = input("Enter employee's name or 'done' to finish: ")

while name != 'done':
    # Add employee count
    employee_count += 1 # employee_count = employee_count + 1
    # ask for employee info
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay rate? "))

    # Evaluate overtime
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    # Add to accumulator totals
    overtime_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay



    # Display results for each employee
    print("------------------------------------------------")
    print(f'Employee Name: {name}')
    print(f'{"Hours Worked":15}{"Pay Rate":<12}{"Overtime Pay":12}{"Regular Pay":15}{"Gross Pay":12}')
    print("----------------------------------------------------------------------------------------------")
    print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')


    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employees: ", employee_count)
print("Total amount paid for overtime: $", format(overtime_total, ',.2f'))
print("Total amount paid for regular pay: $", format(regularpay_total, '.2f'))
print("Total amount paid for gross pay: $", format(grosspay_total, '.2f'))


