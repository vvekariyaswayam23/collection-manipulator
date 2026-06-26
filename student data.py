print("=" * 60)
print("📚 STUDENT DATA ORGANIZER")
print("=" * 60)

students = []
subjects = set()

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("\nEnter Your Choice : "))

    match choice:

        # ---------------- ADD STUDENT ----------------

        case 1:

            print("\n========= ADD STUDENT =========")

            s_id = input("Enter Student ID : ")
            name = input("Enter Student Name : ")
            age = int(input("Enter Student Age : "))
            grade = input("Enter Student Grade : ")
            dob = input("Enter Date of Birth (DD/MM/YYYY) : ")

            sub = input("Enter Subjects (comma separated) : ")

            subject_set = set()

            for i in sub.split(","):
                subject_set.add(i.strip())

            student = {
                "Student Info": (s_id, dob),
                "Student Name": name,
                "Student Age": age,
                "Student Grade": grade,
                "Student Subjects": subject_set
            }

            students.append(student)
            subjects.update(subject_set)

            print("\n✅ Student Added Successfully!")

        # ---------------- DISPLAY ----------------

        case 2:

            print("\n========= ALL STUDENTS =========")

            if len(students) == 0:
                print("No Student Found.")

            else:

                for student in students:

                    print("-" * 50)
                    print(f"Student ID   : {student['Student Info'][0]}")
                    print(f"Name         : {student['Student Name']}")
                    print(f"Age          : {student['Student Age']}")
                    print(f"Grade        : {student['Student Grade']}")
                    print(f"DOB          : {student['Student Info'][1]}")
                    print(f"Subjects     : {', '.join(student['Student Subjects'])}")

        # ---------------- UPDATE ----------------

        case 3:

            print("\n========= UPDATE STUDENT =========")

            sid = input("Enter Student ID : ")

            found = False

            for student in students:

                if student["Student Info"][0] == sid:

                    found = True

                    student["Student Name"] = input("Enter New Name : ")
                    student["Student Age"] = int(input("Enter New Age : "))
                    student["Student Grade"] = input("Enter New Grade : ")

                    new_sub = input("Enter New Subjects : ")

                    student["Student Subjects"] = set()

                    for s in new_sub.split(","):
                        student["Student Subjects"].add(s.strip())

                    subjects.update(student["Student Subjects"])

                    print("\n✅ Student Updated Successfully!")
                    break

            if not found:
                print("❌ Student Not Found!")

        # ---------------- DELETE ----------------

        case 4:

            print("\n========= DELETE STUDENT =========")

            sid = input("Enter Student ID : ")

            found = False

            for i in range(len(students)):

                if students[i]["Student Info"][0] == sid:

                    del students[i]

                    found = True

                    print("\n🗑 Student Deleted Successfully!")
                    break

            if not found:
                print("❌ Student Not Found!")

        # ---------------- SUBJECTS ----------------

        case 5:

            print("\n========= SUBJECTS OFFERED =========")

            if len(subjects) == 0:
                print("No Subjects Available.")

            else:

                for sub in sorted(subjects):
                    print("•", sub)

        # ---------------- EXIT ----------------

        case 6:

            print("\n🙏 Thank You for Using Student Data Organizer!")

            print("\n Welcome Back Soonn..! ")
            break

        # ---------------- INVALID ----------------

        case _:

            print("❌ Invalid Choice! Please Try Again.")
            print("\n Please Try Again. ")
