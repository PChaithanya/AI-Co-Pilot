def menu():
    while True:
        print("\n--- AI Project Co-Pilot ---")
        print("1. Create Project")
        print("2. Create Task")
        print("3. List Projects")
        print("4. Get Tasks by Project ID")
        print("5. Get Recommendation")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_project()
        elif choice == "2":
            create_task()
        elif choice == "3":
            get_projects()
        elif choice == "4":
            pid = int(input("Enter Project ID: "))
            get_tasks_by_project(pid)
        elif choice == "5":
            get_recommendation()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
