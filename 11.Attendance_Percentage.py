#  Write a program that takes total classes and attended classes, then calculates the attendance percentage and checks if the student is eligible to appear for an exam.  

def check_attendance(total, attended): 
    if total <= 0 or attended < 0 or attended > total: 
        return "Invalid input! Attendance must be between 0 and total classes." 
    percentage = (attended / total) * 100 
    return f"Attendance: {percentage}% " + ("Allowed for exam" if percentage >= 75 else "Not allowed for exam") 

total_classes = int(input("Enter total classes: ")) 
attended_classes = int(input("Enter attended classes: ")) 
print(check_attendance(total_classes, attended_classes))