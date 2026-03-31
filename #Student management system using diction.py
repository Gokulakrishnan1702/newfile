#Student management system using dictionary

Student = {}

while True:
    print("\n--- Student Management System ---")
    print("1.Add Student")
    print("2.Display All Student")
    print("3.Search Student by Roll Number")
    print("4.Update Marks")
    print("5.Delete Student")
    print("6.Exit")
    
    choice = input("Enter your choice 1-6: ")

    if choice == '1':
        Roll = input("Enter Roll Number: ")
        Name = input("Enter Name: ")
        Dept = input("Enter Department: ")
        Marks = float(input("Enter Marks: "))
        Student[Roll] = {'Name': Name, 'Department': Dept, 'Marks': Marks}
        print("Student added successfully.")
    elif choice == '2':
        if Student:
            print("\n--- All Students ---")
            for roll, details in Student.items():
                print(f"Roll Number: {roll}, Name: {details['Name']}, Department: {details['Department']}, Marks: {details['Marks']}")
        else:
            print("No student records found.")
    elif choice == '3':
        Roll = input("Enter Roll Number to search: ")
        if Roll in Student:
            details = Student[Roll]
            print(f"Roll Number: {Roll}, Name: {details['Name']}, Department: {details['Department']}, Marks: {details['Marks']}")
        else:
            print("Student not found.")
    elif choice == '4':
        Roll = input("Enter Roll Number to update marks: ")
        if Roll in Student:
            Marks = float(input("Enter new Marks: "))
            Student[Roll]['Marks'] = Marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")
    elif choice == '5':
        Roll = input("Enter Roll Number to delete: ")
        if Roll in Student:
            del Student[Roll]
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    elif choice == '6':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
import csv
def classify_performance(average):
    """Classify student performance based on average marks."""
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Good"
    elif average >= 50:
        return "Average"
    else:
        return "Poor"
def main():
    print("===== Student Performance Analyzer =====")
    
    # Get number of students
    n = int(input("Enter number of students: "))

    # CSV file setup
    filename = "student_performance.csv"
    fields = ["Name", "Marks", "Total", "Average", "Performance"]
    
    # Open CSV file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)  # write header row
        
        for i in range(n):
            print(f"\n--- Enter details for Student {i+1} ---")
            name = input("Enter student name: ")
            
            marks_input = input("Enter marks separated by space (e.g. 85 90 78 92): ")
            marks = [float(m) for m in marks_input.split()]
            
            total = sum(marks)
            average = total / len(marks)
            performance = classify_performance(average)
            
            # Write student data to CSV
            writer.writerow([name, marks, total, round(average, 2), performance])
            
            # Display results on screen
            print("\nStudent Result:")
            print(f"Name: {name}")
            print(f"Total Marks: {total}")
            print(f"Average Marks: {average:.2f}")
            print(f"Performance: {performance}")
    
    print("\nAll records saved successfully to 'student_performance.csv' ")
