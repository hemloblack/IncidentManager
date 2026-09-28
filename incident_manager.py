from incident import Incident as inct
import json

file_name = "Incident.json"


class incident_manager:
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data_file = json.load(file)

        if not isinstance(data_file, dict):
            print("Invalid structure. Starting with empty data.")
            data_file = {}

            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        print("File not found. Creating new file.")
        data_file = {}

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data_file, file, indent=4, ensure_ascii=False)

    except json.JSONDecodeError:
        print("Invalid JSON file. Starting with empty data.")
        data_file = {}

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data_file, file, indent=4, ensure_ascii=False)

    def automat_number(self):
        if self.data_file:
            return max(int(k) for k in self.data_file.keys()) + 1

        return 1001

    def add_incident(self):
        new_id = self.automat_number()

        while str(new_id) in self.data_file:
            new_id += 1

        new_data = inct(
            new_id,
            title=input("Title: ").strip(),
            type=input(
                "Type [Phishing, Malware, Brute Force, Unauthorized Access, "
                "Suspicious Login, Vulnerability, Other]: "
            ).strip(),
            severity=input(
                "Severity [Low, Medium, High, Critical]: "
            ).strip(),
            status=input(
                "Status [Open, In Progress, Resolved, Closed]: "
            ).strip(),
            reporter=input("Reporter: ").strip(),
            description=input("Description: ").strip()
        )

        self.data_file[str(new_id)] = new_data.to_dict()

        self.save_to_file()

        return f"Incident {new_id} added successfully."

    def show_all_incidents(self):
        print("--------- Show All Incidents ---------")

        if not self.data_file:
            print("There is no incident.")
            return

        print(f"\n{len(self.data_file)} incident(s):\n")

        for inc_id, inc_data in self.data_file.items():
            print(f"ID: {inc_id}")
            print(json.dumps(inc_data, indent=4, ensure_ascii=False))
            print("-" * 40)

    def search(self, field, value):
        results = []

        if field == "id":
            incident = self.data_file.get(str(value))

            if incident:
                results.append(incident)

        else:
            for inc_data in self.data_file.values():
                field_value = str(inc_data.get(field, ""))

                if field_value.lower() == value.lower():
                    results.append(inc_data)

        return results

    def delete_incident(self, incident_id):
        incident_id = str(incident_id)

        if incident_id not in self.data_file:
            print(f"ID {incident_id} not found.")
            print(f"Available IDs: {list(self.data_file.keys())}")
            return None

        del self.data_file[incident_id]

        self.save_to_file()

        return "Successful delete."

    def Change_Incident_Status(self, selected_id, choice):
        selected_id = str(selected_id)

        if selected_id not in self.data_file:
            return f"ID {selected_id} not found."

        statuses = {
            1: "Open",
            2: "In Progress",
            3: "Resolved",
            4: "Closed"
        }

        if choice not in statuses:
            return "Invalid choice (1-4)."

        self.data_file[selected_id]["status"] = statuses[choice]

        self.save_to_file()

        return "Successful change."

    def Change_Incident_Severity(self, selected_id, choice):
        selected_id = str(selected_id)

        if selected_id not in self.data_file:
            return f"ID {selected_id} not found."

        severities = {
            1: "Low",
            2: "Medium",
            3: "High",
            4: "Critical"
        }

        if choice not in severities:
            return "Invalid choice (1-4)."

        self.data_file[selected_id]["severity"] = severities[choice]

        self.save_to_file()

        return "Successful change."

    def save_to_file(self):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(
                self.data_file,
                file,
                indent=4,
                ensure_ascii=False
            )


manager = incident_manager()


while True:
    print("""
================================
     CYBER INCIDENT TRACKER
================================

1. Add Incident
2. Show All Incidents
3. Search Incidents
4. Change Incident Status
5. Change Incident Severity
6. Delete Incident
7. Exit
""")

    try:
        entry_number = int(input("Choose an option: "))

    except ValueError:
        print("Error: Please enter a number.")
        continue

    if entry_number == 1:

        print(manager.add_incident())

    elif entry_number == 2:

        manager.show_all_incidents()

    elif entry_number == 3:

        print("""
Search by:
1. ID
2. Type
3. Severity
4. Status
""")

        try:
            choice = int(input("Choose field: ").strip())

        except ValueError:
            print("Error: Please enter a number.")
            continue

        if choice == 1:

            value = input("Enter ID: ").strip()
            results = manager.search("id", value)

        elif choice == 2:

            print(
                "Type options: [Phishing, Malware, Brute Force, "
                "Unauthorized Access, Suspicious Login, Vulnerability, Other]"
            )

            value = input("Enter type: ").strip()
            results = manager.search("type", value)

        elif choice == 3:

            print("Severity options: [Low, Medium, High, Critical]")

            value = input("Enter severity: ").strip()
            results = manager.search("severity", value)

        elif choice == 4:

            print("Status options: [Open, In Progress, Resolved, Closed]")

            value = input("Enter status: ").strip()
            results = manager.search("status", value)

        else:

            print("Invalid choice.")
            results = []

        if not results:

            print("No incidents found.")

        else:

            print(f"\nFound {len(results)} incident(s):\n")

            for inc in results:
                print(
                    json.dumps(
                        inc,
                        indent=4,
                        ensure_ascii=False
                    )
                )

                print("-" * 40)

    elif entry_number == 4:

        try:
            sid = int(input("Enter ID: "))

        except ValueError:
            print("Please enter the correct ID.")
            continue

        try:
            option = int(
                input(
                    "Status options: "
                    "[1:Open, 2:In Progress, 3:Resolved, 4:Closed]\n"
                    "Number: "
                )
            )

        except ValueError:
            print("Please enter the correct number.")
            continue

        print(
            manager.Change_Incident_Status(
                selected_id=str(sid),
                choice=option
            )
        )

    elif entry_number == 5:

        try:
            sid = int(input("Enter ID: "))

        except ValueError:
            print("Please enter the correct ID.")
            continue

        try:
            option = int(
                input(
                    "Severity options: "
                    "[1:Low, 2:Medium, 3:High, 4:Critical]\n"
                    "Number: "
                )
            )

        except ValueError:
            print("Please enter the correct number.")
            continue

        print(
            manager.Change_Incident_Severity(
                selected_id=str(sid),
                choice=option
            )
        )

    elif entry_number == 6:

        result = manager.delete_incident(
            input("Select ID for delete: ").strip()
        )

        if result:
            print(result)

    elif entry_number == 7:

        print("Goodbye!")
        break

    else:

        print("Invalid option. Please choose between 1 and 7.")