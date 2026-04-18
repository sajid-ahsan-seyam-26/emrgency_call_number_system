calls=[]
def add_emergency_number():
    print("add emergency number")
    caller_name=input("enter the phone number")
    phone=input("enter the phone number")
    location=input("enter the location")
    emergency_type=input("enter the emergency type")
    priority=input("enter the priority")
    status="pending"
    call={
    "caller_name":caller_name,
    "phone":phone,
    "priority":priority,
    "status":status
    }
    calls.append(call)
    print("emergency number added sucessfully")
def show_all_calls():
    print("\n-----all emergency call----")
    if len(calls)==0:
        print("no emergency call data found")
    else:
          count = 1
          for call in calls:
            print("\nCall", count)
            print("Caller Name    :", call["caller_name"])
            print("Phone          :", call["phone"])
            print("Location       :", call["location"])
            print("Emergency Type :", call["emergency_type"])
            print("Priority       :", call["priority"])
            print("Status         :", call["status"])
            count = count + 1


def serach_call():
    print("\n---- serach call-----")
    search_phone=input("enter the phone number")
    found=False
    for call in calls:
          if call["phone"] == search_phone:
            print("\nEmergency Call Found")
            print("Caller Name    :", call["caller_name"])
            print("Phone          :", call["phone"])
            print("Location       :", call["location"])
            print("Emergency Type :", call["emergency_type"])
            print("Priority       :", call["priority"])
            print("Status         :", call["status"])
            found = True
            break
          if found==False:
            print("emergency call not found")
def update_call():
    print("\n----update emergency call----")
    update_phone=input("enter for the update call")
    found=False
    for call in calls:
        if call["phone"]==update_phone:
            print("\n------ current information---------")
            print("\nCurrent Information:")
            print("Caller Name    :", call["caller_name"])
            print("Phone          :", call["phone"])
            print("Location       :", call["location"])
            print("Emergency Type :", call["emergency_type"])
            print("Priority       :", call["priority"])
            print("Status         :", call["status"])
            print("\n -------enter new information-------")
            new_caller_name=input("enter new caller name")
            new_locaton=input("enter new location")
            new_emergency_type=input("enter new emergency  type")
            new_priority=input("enter new priority")
            new_status=input('enetr new status')
            call["caller_name"]=new_caller_name
            call["location"]=new_locaton
            call["emergency_type"] = new_emergency_type
            call["priority"] = new_priority
            call["status"] = new_status
            print("emergency call upload sucessfully")
            found=True
            break
    if found==False:
        print("emergency call is not found")
def delete_call():
    print("\n--------delete emergency call-----")
    delete_phone=input("enter a call to delete the call")
    found=False
    for call in calls:
        if call["phone"]==delete_call:
            calls.remove(call)
            print("call remove sucesfully")
            found=True
            break
            if found==False:
                print("emergecny call not found")
def show_pending_call():
    print("\n show all pending call")
    found=False
    count=1
    for call in calls:
        if call["status"]=="pending":
            print("\n call",count)
            print("Caller Name    :", call["caller_name"])
            print("Phone          :", call["phone"])
            print("Location       :", call["location"])
            print("Emergency Type :", call["emergency_type"])
            print("Priority       :", call["priority"])
            print("Status         :", call["status"])
            count = count + 1
            found = True
        if found==False:
            print("no pending call found")
def mark_call_resolved():
    print("\n---------mark call as resolved-------")
    mark_call_resolved=input("enter resolved call")
    found=False
    for call in calls:
        if call["phone"]==resolved_phone:
            call["status"]='resolved'
            print("emergency call maked resolved sucesfully")
            found=True
            break
        if found==False:
            print("emergency call not found")
def menu():
    while True:
        print("=====emergency call center system=====")
        print("1.add emrgency calls")
        print("2.show all emrgency calls")
        print("3. serach emrgency calls")
        print("4.update emrgency call")
        print("5. delete emrgecny call ")
        pritn("6. show pending calls")
        print("7. mark call as resolved")
        print("8. Exit")
        choice=input("enter your choice")
                if choice == "1":
            add_emergency_call()
        elif choice == "2":
            show_all_calls()
        elif choice == "3":
            search_call()
        elif choice == "4":
            update_call()
        elif choice == "5":
            delete_call()
        elif choice == "6":
            show_pending_calls()
        elif choice == "7":
            mark_call_resolved()
        elif choice == "8":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
