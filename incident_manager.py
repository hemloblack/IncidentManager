from incident import Incident as inct
import json
file_name="Incident.json"

class incident_manager:
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data_file = json.load(file)
    except FileNotFoundError:
        print("File not found")
        data_file = {}  # مقداردهی اولیه به صورت دیکشنری خالی
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data_file, file, indent=4, ensure_ascii=False)
        print("Created file users.json")
    except json.JSONDecodeError:
        print("Invalid JSON file. Starting with empty data.")
        data_file = {}
    def automat_number(self):
        if self.data_file:
            next_id = max(int(k) for k in self.data_file.keys()) + 1
        else:
            next_id = 1001
        return next_id
    def __init__(self,
                    title,
                    type,
                    severity,
                    status,
                    reporter,
                    description):
            self.id=self.automat_number()
            self.title=title
            self.type=type
            self.severity=severity
            self.status=status
            self.reporter=reporter
            self.description=description
    def add_incident(self):
        
        new_data_to_send=inct(self.id,self.title,self.type,self.severity,self.status,self.reporter,self.description)
        diteil_file=new_data_to_send.to_dict()
        self.data_file[self.id]=diteil_file
        incident_manager.save_to_file()
        return"the add incident is successful"
    
    @staticmethod
    def show_all_incidents():
        return incident_manager.data_file
    @staticmethod
    def Show_Incident_Details():
        ls_value=[]
        for i in incident_manager.data_file.values():
            ls_value.append(i)
        return ls_value
        
    @staticmethod
    def search(field, value):#با کمک دیپ سیک
        """
        field: 'type' یا 'severity' یا 'status' یا 'id'
        value: مقداری که می‌خوای فیلتر کنی
        """
        results = []
        
        if field == "id":
            # جستجو بر اساس ID (کلید دیکشنری)
            incident = incident_manager.data_file.get(str(value))
            if incident:
                results.append(incident)
        else:
            # جستجو بر اساس یه فیلد داخل هر incident
            for inc_id, inc_data in incident_manager.data_file.items():
                if inc_data.get(field, "").lower() == value.lower():
                    results.append(inc_data)
        
        return results
                
            
    
    
    @staticmethod
    def delete_incident(id):
        del incident_manager.data_file[id]
        incident_manager.save_to_file()
        return "sucssesful delete"
    
    
    @staticmethod
    def Change_Incident_Status(selected_id,choice):
            
            if choice==1:
                incident_manager.data_file[selected_id]["status"]="Open"
                incident_manager.save_to_file()
                return"successful change"
                
            elif choice==2:
                incident_manager.data_file[selected_id]["status"]="In Progress"
                incident_manager.save_to_file()
                return"successful change"
                
            elif choice==3:
                incident_manager.data_file[selected_id]["status"]="Resolved"
                incident_manager.save_to_file()
                return"successful change"
               
            elif choice==4:
                incident_manager.data_file[selected_id]["status"]="Closed"
                incident_manager.save_to_file()
                return"successful change"
               
            else:
                return"the number or id invalid"
    @staticmethod
    def Change_Incident_Severity(selected_id,choice) : 
         
        if choice==1:
            incident_manager.data_file[selected_id]["severity"]="low"
            incident_manager.save_to_file()
            return"successful change"
            
        elif choice==2:
            incident_manager.data_file[selected_id]["severity"]="Medium"
            incident_manager.save_to_file()
            return"successful change"
            
        elif choice==3:
            incident_manager.data_file[selected_id]["severity"]="High"
            incident_manager.save_to_file()
            return"successful change"
        

        elif choice==4:
            incident_manager.data_file[selected_id]["severity"]="Critical"
            incident_manager.save_to_file()
            return"successful change"
        else:
             return"the number or id invalid"     
                
    @staticmethod           
    def save_to_file():
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(incident_manager.data_file, file, indent=4, ensure_ascii=False)
        print("file save")
        
while True:
    print('''
================================
     CYBER INCIDENT TRACKER
================================

1. Add Incident
2. Show All Incidents
3. Show Incident Details
4. Search Incidents
5. Change Incident Status
6. Change Incident Severity
7. Delete Incident
8. Exit
          ''')
    
    entry_number=int(input("Choose an option:"))
    if entry_number==1:
         manager = incident_manager(
            input("Title: "),
            input("""Type: select one :[Phishing,Malware,Brute Force,Unauthorized Access,Suspicious Login,Vulnerability,Other]\n"""),
            input("Severity:  select one:  [Low,Medium,High,Critical]\n"),
            input("Status: [Open,In Progress,Resolved,Closed]\n"),
            input("Reporter: "),
            input("Description: "))
         print(manager.add_incident())
    elif entry_number==2:
        print(incident_manager.show_all_incidents())
    elif entry_number==3:
       print(incident_manager.Show_Incident_Details())
    elif entry_number==4:#با کمک دیپ سیک
        
        print("""
        Search by:
        1. ID
        2. Type
        3. Severity
        4. Status
        """)
        choice = input("Choose field: ").strip()
        
        if choice == "1":
            value = input("Enter ID: ").strip()
            results = incident_manager.search("id", value)
        elif choice == "2":
            print("Type options: [Phishing, Malware, Brute Force, Unauthorized Access, Suspicious Login, Vulnerability, Other]")
            value = input("Enter type: ").strip()
            results = incident_manager.search("type", value)
        elif choice == "3":
            print("Severity options: [Low, Medium, High, Critical]")
            value = input("Enter severity: ").strip()
            results = incident_manager.search("severity", value)
        elif choice == "4":
            print("Status options: [Open, In Progress, Resolved, Closed]")
            value = input("Enter status: ").strip()
            results = incident_manager.search("status", value)
        else:
            print("Invalid choice")
            results = []
        
        if not results:
            print("No incidents found.")
        else:
            print(f"\nFound {len(results)} incident(s):\n")
            for inc in results:
                print(json.dumps(inc, indent=4, ensure_ascii=False))
                print("-" * 40)
    elif entry_number==5:
        id=input("enter id :")
        option=int(input("Status options: [1:Open, 2:In Progress, 3:Resolved,4: Closed]\n number:"))
        print(incident_manager.Change_Incident_Status(selected_id=id,choice=option))
    elif entry_number==6:
        id=input("enter id :")
        option=int(input("Severity options: [1:Low,2: Medium,3: High,4: Critical]\n number:"))
        print(incident_manager.Change_Incident_Severity(selected_id=id,choice=option))
    elif entry_number==7:
        incident_manager.delete_incident(input("select id for delete:\n"))
    elif entry_number==8:
        print("goodbay")
        break