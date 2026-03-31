import csv

def classify_performance(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Good"
    elif average >= 50:
        return "Average"
    else:
        return "Poor"

n = int(input("Enter number of students: "))

with open("gokul.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow(["Name ", " Marks1 ", " Marks2 ", " Marks3 ", " Total ", " Average ", " Performance"])
    
    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        name = input("Enter student name: ")
        marks1 = float(input("Enter Marks 1: "))
        marks2 = float(input("Enter Marks 2: "))
        marks3 = float(input("Enter Marks 3: "))
        total = marks1 + marks2 + marks3
        average = total / 3
        performance = classify_performance(average)
        print(f"\nStudent: {name}")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print(f"Performance: {performance}")
        writer.writerow([ name , marks1 , marks2 , marks3 , total , round(average, 2) , performance])

print("\nAll records have been saved in 'gokul.csv'")

