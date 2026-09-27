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
    
                
    def add_incident(self):
        id=self.automat_number()
        new_data_to_send=inct(
                        id,
                        title=input("Title: "),
                        type=input("""Type: select one :[Phishing,Malware,Brute Force,Unauthorized Access,Suspicious Login,Vulnerability,Other]\n"""),
                        severity=input("Severity:  select one:  [Low,Medium,High,Critical]\n"),
                        status=input("Status: [Open,In Progress,Resolved,Closed]\n"),
                        reporter=input("Reporter: "),
                        description=input("Description: "),
                        )
        diteil_file=new_data_to_send.to_dict()
        self.data_file[id]=diteil_file
        self.save_to_file()
        return"the add incident is successful"
    
   
    def show_all_incidents(self):
        return self.data_file
        
    
    def search(self,field, value):#با کمک دیپ سیک
        """
        field: 'type' یا 'severity' یا 'status' یا 'id'
        value: مقداری که می‌خوای فیلتر کنی
        """
        results = []
        
        if field == "id":
            # جستجو بر اساس ID (کلید دیکشنری)
            incident = self.data_file.get(str(value))
            if incident:
                results.append(incident)
        else:
            # جستجو بر اساس یه فیلد داخل هر incident
            for inc_id, inc_data in self.data_file.items():
                if inc_data.get(field, "").lower() == value.lower():
                    results.append(inc_data)
        
        return results
                
            
    
    
    
    def delete_incident(self,id):
        del self.data_file[id]
        self.save_to_file()
        return "sucssesful delete"
    
    
    
    def Change_Incident_Status(self,selected_id,choice):
            
            if choice==1:
                self.data_file[selected_id]["status"]="Open"
                self.save_to_file()
                return"successful change"
                
            elif choice==2:
                self.data_file[selected_id]["status"]="In Progress"
                self.save_to_file()
                return"successful change"
                
            elif choice==3:
                self.data_file[selected_id]["status"]="Resolved"
                self.save_to_file()
                return"successful change"
               
            elif choice==4:
                self.data_file[selected_id]["status"]="Closed"
                self.save_to_file()
                return"successful change"
               
            else:
                return"the number or id invalid"
    
    def Change_Incident_Severity(self,selected_id,choice) : 
         
        if choice==1:
            self.data_file[selected_id]["severity"]="low"
            self.save_to_file()
            return"successful change"
            
        elif choice==2:
            self.data_file[selected_id]["severity"]="Medium"
            self.save_to_file()
            return"successful change"
            
        elif choice==3:
            self.data_file[selected_id]["severity"]="High"
            self.save_to_file()
            return"successful change"
        

        elif choice==4:
            self.data_file[selected_id]["severity"]="Critical"
            self.save_to_file()
            return"successful change"
        else:
             return"the number or id invalid"     
                
              
    def save_to_file(self):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(self.data_file, file, indent=4, ensure_ascii=False)
        print("file save")

manager = incident_manager()
while True:
    print('''
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
          ''')
    
    entry_number=int(input("Choose an option:"))
    if entry_number==1:
         print(manager.add_incident())
    elif entry_number==2:
        print(manager.show_all_incidents())
    elif entry_number==3:#با کمک دیپ سیک
        
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
            results = manager.search("id", value)
        elif choice == "2":
            print("Type options: [Phishing, Malware, Brute Force, Unauthorized Access, Suspicious Login, Vulnerability, Other]")
            value = input("Enter type: ").strip()
            results = manager.search("type", value)
        elif choice == "3":
            print("Severity options: [Low, Medium, High, Critical]")
            value = input("Enter severity: ").strip()
            results = manager.search("severity", value)
        elif choice == "4":
            print("Status options: [Open, In Progress, Resolved, Closed]")
            value = input("Enter status: ").strip()
            results = manager.search("status", value)
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
    elif entry_number==4:
        id=input("enter id :")
        option=int(input("Status options: [1:Open, 2:In Progress, 3:Resolved,4: Closed]\n number:"))
        print(manager.Change_Incident_Status(selected_id=id,choice=option))
    elif entry_number==5:
        id=input("enter id :")
        option=int(input("Severity options: [1:Low,2: Medium,3: High,4: Critical]\n number:"))
        print(manager.Change_Incident_Severity(selected_id=id,choice=option))
    elif entry_number==6:
        manager.delete_incident(input("select id for delete:\n"))
    elif entry_number==7:
        print("goodbay")
        break