import csv
from datetime import datetime


class University:
    def __init__(self, country, name, price, major, deadline, profile):
        self.country = country
        self.name = name
        self.price = price
        self.major = major
        self.deadline = deadline  # expected format: YYYY-MM-DD
        self.profile = profile    # "Complete" or "No"

    def days_left(self):
        try:
            due = datetime.strptime(self.deadline, "%Y-%m-%d")
            return (due - datetime.now()).days
        except ValueError:
            return None


class universitymanager:
    def __init__(self, filename="UNIVERSITY.csv"):
        self.universities = []
        self.filename = filename
        self.loadfile()

    def loadfile(self):
        self.universities.clear()
        try:
            with open(self.filename, newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row or len(row) < 6:
                        continue
                    country, name, price, major, deadline, profile = row[:6]
                    self.universities.append(
                        University(country, name, price, major, deadline, profile)
                    )
        except FileNotFoundError:
            print("File", self.filename, "not found. Create new file!!!")

    def savefile(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            for uni in self.universities:
                writer.writerow(
                    [uni.country, uni.name, uni.price, uni.major, uni.deadline, uni.profile]
                )

    def adduniversity(self, uni):
        self.universities.append(uni)
        self.savefile()

    def listing(self):
        if not self.universities:
            print("No list created!")
            return
        print("UNIVERSITY LISTING")
        for i, uni in enumerate(self.universities):
            days = uni.days_left()
            days_str = f"{days} days left" if days is not None else "invalid date"
            print(
                f"{i}. {uni.name} ({uni.country}) | Major: {uni.major} | "
                f"Price: {uni.price} | Deadline: {uni.deadline} ({days_str}) | "
                f"Profile: {uni.profile}"
            )
        print()

    def checklist(self):
        """Flags anything that needs attention: incomplete profiles or close deadlines."""
        if not self.universities:
            print("No list created!")
            return
        print("CHECK RESULTS")
        any_issues = False
        for i, uni in enumerate(self.universities):
            issues = []
            if uni.profile.strip().lower() != "complete":
                issues.append("profile incomplete")
            days = uni.days_left()
            if days is None:
                issues.append("invalid deadline format (use YYYY-MM-DD)")
            elif days < 0:
                issues.append("DEADLINE PASSED")
            elif days <= 14:
                issues.append(f"deadline in {days} days — act soon")
            if issues:
                any_issues = True
                print(f"{i}. {uni.name}: {', '.join(issues)}")
        if not any_issues:
            print("Everything looks on track!")
        print()

    def count(self):
        return len(self.universities)

    def deleteuniversity(self, index):
        del self.universities[index]
        self.savefile()

    def deleteall(self):
        self.universities.clear()
        self.savefile()
    def edituniversity(self, choice_of_index, changed, new_aspect):
        if not (0 <= choice_of_index < len(self.universities)):
            print("Invalid index")
            return
        else:
            uni = self.universities[choice_of_index]
            setattr(uni, changed, new_aspect)
            self.savefile()
            print(f"Updated '{changed}' for index {choice_of_index} to '{uni.name}")




def add_university_flow(manager):
    country = input("Input Country: ")
    name = input("Input University: ")
    price = input("Input Price: ")
    major = input("Input Major: ")
    deadline = input("Input Deadline (YYYY-MM-DD): ")
    profile = input("Input Profile status (Complete/No): ")
    manager.adduniversity(University(country, name, price, major, deadline, profile))
    print("University added")
    print(
        f"University = {name} - Country = {country} - Price = {price} - "
        f"Major = {major} - Deadline = {deadline} - Profile = {profile}"
    )


def main():
    manager = universitymanager()

    while True:
        start = input("Start Program? (yes/no): ")
        if start.lower() == "no":
            print("Thank you for using this program")
            break
        elif start.lower() != "yes":
            print("Please answer yes or no.")
            continue

        while True:
            print("Please insert the following choices:")
            print(
                " 1.   Show List \n 2.   Add University    \n 3.   Delete University  "
                "\n 4.   Delete All  \n 5.   Check List (deadlines & profile status) "
                "\n 6.   Edit \n 7.   EXIT"
            )
            choice = input("Choice: ")

            if choice == "1":
                manager.listing()
            elif choice == "2":
                add_university_flow(manager)
            elif choice == "3":
                manager.listing()
                try:
                    index = int(input("Enter the University ID you want to delete: "))
                    if 0 <= index < manager.count():
                        manager.deleteuniversity(index)
                        print("Deleted")
                    else:
                        print("University not found")
                except ValueError:
                    print("University not found")
            elif choice == "4":
                manager.listing()
                confirm = input("Are you sure you want to delete all entries? (yes/no): ")
                if confirm.lower() == "yes":
                    manager.deleteall()
                    print("All deleted")
                else:
                    print("Operation cancelled")
            elif choice == "5":
                manager.checklist()
            elif choice == "6":
                manager.listing()
                try:
                    choice_of_index = int(input("Enter choice: "))
                except ValueError:
                    print("Choice not found")
                    continue
                if not (0 <= choice_of_index < manager.count()):
                    print("Choice not found")
                    continue
                field_options = {"1": "name",
                                 "2": "country",
                                 "3": "price",
                                 "4": "major",
                                 "5": "deadline",
                                 "6": "profile"
                                 }
                print('which aspect would you like to change? \n 1. University \n 2. Country \n 3. Price'
                      '\n 4. Major \n 5. Deadline')
                changed = input("Enter choice: ")
                if choice not in field_options:
                    print("Please choose a valid option from the menu.")
                    continue
                new_aspect = input("Enter the changed aspect: ")
                manager.edituniversity(choice_of_index, field_options[changed], new_aspect)

            elif choice == "7":
                print("Summary")
                print(f"Total universities tracked: {manager.count()}")
                print("Thank you for using this program")
                break
            else:
                print("Please choose a valid option from the menu.")
            # loop continues automatically until choice == "6" breaks it above


if __name__ == "__main__":
    main()

#We are still using a bit of claude here to do some debugging and improving efficiency of the code. The code is working fine but we can improve it by adding some error handling and input validation. We can also add some comments to make the code more readable.