import json

try:
    with open("students.txt", "r") as f:
        students = json.load(f)
except:
    students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll: ")
        students.append({"name": name, "roll": roll})

    elif choice == "2":
        for s in students:
            print(s["name"], "-", s["roll"])

    elif choice == "3":
        name = input("Search name: ")
        for s in students:
            if s["name"] == name:
                print("Found:", s["name"], s["roll"])

    elif choice == "4":
        name = input("Delete name: ")
        for s in students:
            if s["name"] == name:
                students.remove(s)
                print("Deleted")
                break

    elif choice == "5":
        with open("students.txt", "w") as f:
            json.dump(students, f)
        print("Saved & Exiting")
        break