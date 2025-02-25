import time

#initalize empty dictionary
student_grades = {

}


#add student
def add_student(name, grade=0):  #for default grade
    student_grades[name] = grade
    print(f"Student name: {name} with grade :{grade} has been added.")


#update student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student name: {name} with grade :{grade} has been updated.")

    else:
        print("No data found ! ")


#delete student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student data of {name} has been deleted.")

    else:
        print("No data found ! ")


#display student
def display_student():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"Student name: {name} with grade :{grade}")

    else:
        print("No data found ! ")


def main():
    while True:
        print("\nStudent Grade System ")
        print("1. ADD STUDENT ")
        print("2. UPDATE STUDENT ")
        print("3. DELETE STUDENT ")
        print("4. DISPLAY STUDENT ")
        print("5. EXIT ")

        choice = input("ENTER YOUR CHOICE OF OPERATION: ")

        if choice == "1":
            name = input("ENTER THE NAME OF STUDENT = ").capitalize()
            grade = int(input("ENTER THE MARKS OF STUDENT = "))
            add_student(name, grade)

        elif choice == "2":
            name = input("ENTER THE NAME OF STUDENT = ").capitalize()
            grade = int(input("ENTER THE MARKS OF STUDENT = "))
            update_student(name, grade)

        elif choice == "3":
            name = input("ENTER THE NAME OF STUDENT = ").capitalize()
            delete_student(name)

        elif choice == "4":
            display_student()

        elif choice == "5":
            closing = input("Do you want to close the  program [yes or no]:  ")
            if closing != "yes":
                continue

            else:
                print("Program is closing... ")
                time.sleep(3)
                break


        else:
            print("INVALID CHOICE ... ")


main()
