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
    
    print("\nAll records saved successfully to 'student_performance.csv' ✅")

# Run the program
if __name__ == "__main__":
    main()
