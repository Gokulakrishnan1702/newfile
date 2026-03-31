stu = {
    ("adi", 90),
    ("aka", 99),
    ("gok", 88)
}

total = 0
for name, marks in stu:
    print(f"{name} scored {marks} mark")
    total += marks

average = total / len(stu)
print(f"Average marks: {average}")