# life in weeks
age = input("What is your age")

# age_as_int = int(age)

years_remaining = 90 - (int(age))
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months, and {years_remaining} years left."
print(message)
