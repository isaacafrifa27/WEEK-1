print("Hello World")
print('Hello Isaac')
celsius_temperature = 38.4
fahrenheit_temperature = (celsius_temperature * 9/5) +32
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit.")
total_matches = 609
total_batted = 1014
total_not_out = 162
total_runs_scored = 48426
batting_average = total_runs_scored / (total_batted - total_not_out)
print(f"Geoffrey Boycott's batting average is: {batting_average:.2f}")
students = [113, 175, 12]
students_per_group = 24
full_groups = []
left_over_students = []
for num_students in students:
    full_group_count = num_students // students_per_group
    left_over_count = num_students % students_per_group
    full_groups.append(full_group_count)
    left_over_students.append(left_over_count)
for i in range(len(students)):
    print(f"For {students[i]} students:")
    print(f"Full groups: {full_groups[i]}")
    print(f"Left-over students: {left_over_students[i]}\n")

