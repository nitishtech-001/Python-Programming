"""
getting the all subject with respective obtain and total marks then after calculating the percentage we assign the grade for each student

I am also trying to validating the user input for perfect performance
"""
def get_subject_marks():
    # am using the dictionary to store the "subject" -> [obtain_marks,total_marks]
    subject_marks = {}
    subject_count = 0
    while True:
        subject_count += 1
        subject = input(f"Enter {subject_count} subject name : ")
        obtain_marks = float(input(f"Enter obtain marks for ,{subject} : "))
        total_marks = float(input(f"Enter the total marks for {subject} : "))
        subject_marks[subject] = [obtain_marks,total_marks]

        next = input("Is there another subject (y/n): ")
        if next.lower() == "n":
            break
    return subject_marks

def calculate_percentage(subject_marks):
    # finding the grand total and obtain total
    obtain_total = 0
    grand_total = 0
    for obtain,total in subject_marks.values():
        obtain_total += obtain
        grand_total += total

    return (obtain_total/grand_total)*100

def get_grade(percentage):
    # each index range form 0-10, 10-20, 20-30, 30-40,40-50, 50-60, 60-70, 70-80, 80-90, 90-100
    grade = ["F","F","E","D","D+","C","C+","B","B+","A","A+"]

    grade_idx = int(percentage//10)
    # percentage is 100%
    if grade_idx >= 10: # full marks obtain
        return "A+"
    
    # for percentage multiple of 10    
    if percentage%10 == 0:
        return grade[grade_idx]

    return grade[grade_idx+1]

def display_info(subject_marks):
    print("\nSubject details are ::::: ")
    print(f"Subject     Obtain_marks    Total_marks  Percentage     Grade")
    for sub, marks in subject_marks.items():
        percentage = (marks[0]/marks[1])*100
        grade = get_grade(percentage)

        print(f"{sub} \t\t{marks[0]}\t\t {marks[1]}\t\t {percentage}\t\t {grade}")
    print()


def result(student_name,standard):
    subject_marks = get_subject_marks()
    percentage = calculate_percentage(subject_marks)
    print(percentage)
    grade = get_grade(percentage)
    display_info(subject_marks)
    print(f"""
            Name : {student_name},
            Standard : {standard},
            Percentage : {percentage}
            Grade : {grade}
        """)


if __name__  == "__main__":
    student_name = input("Enter your name : ")
    standard = input("Enter the standard : ")

    result(student_name,standard)
