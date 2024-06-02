class EventManagementSystem:
    def _init_(self):
        self.events = {}
        self.eidc = 0

    def create_event(self):
        start_date = input("Enter start date: ")
        end_date = input("Enter end date: ")
        
        for event in self.events.values():
            if (event['start_date'] <= start_date <= event['end_date']) or (event['start_date'] <= end_date <= event['end_date']):
                print("There is another event in this date, please choose another date")
                return
        
        self.eidc += 1
        event_id = self.eidc
        print("Event ID:", event_id)
        event_title = input("Enter event title: ")
        reserved_members = int(input("Enter reserved members: "))
        if reserved_members==0 :
            print("Event cannot be created")
            return 

        event = {
            "event_title": event_title,
            "reserved_members": reserved_members,
            "start_date": start_date,
            "end_date": end_date
        }

        self.events[event_id] = event
        print("Event created successfully!")

    def read_event(self):
        event_id = int(input("Enter event ID: "))

        if event_id in self.events:
            event = self.events[event_id]
            print("Event ID:", event_id)
            print("Event Title:", event["event_title"])
            print("Reserved Members:", event["reserved_members"])
            print("Start Date:", event["start_date"])
            print("End Date:", event["end_date"])
        else:
            print("Event not found!")

    def get_attendence_statistics(self):
        a = int(input("Enter event id to know the attendance"))
        if a in self.events:
            event = self.events[a]
            c = int(event["reserved_members"])
            print("Total reserved members:", event["reserved_members"])
            b = int(input("Enter the number of members attended: "))
            per = (b / c) * 100
            print("Percentage of attendance:", per)
        else:
            print("Invalid event ID")

    def update_event(self):
        event_id = int(input("Enter event ID: "))

        if event_id in self.events:
            event = self.events[event_id]
            print("Current Event Details:")
            print("Event ID:", event_id)
            print("Event Title:", event["event_title"])
            print("Reserved Members:", event["reserved_members"])
            print("Start Date:", event["start_date"])
            print("End Date:", event["end_date"])

            event_title = input("Enter new event title (leave blank to keep current): ")
            reserved_members = input("Enter new reserved members (leave blank to keep current): ")
            start_date = input("Enter new start date (leave blank to keep current): ")
            end_date = input("Enter new end date (leave blank to keep current): ")

            for event in self.events.values():
                if  (event['start_date'] <= end_date <= event['end_date']):
                    print("There is another event in this date, please choose another date")
                    return
              

            if event_title:
                event["event_title"] = event_title
            if reserved_members:
                event["reserved_members"] = reserved_members
            if start_date:
                event["start_date"] = start_date
            if end_date:
                event["end_date"] = end_date

            print("Event updated successfully!")
        else:
            print("Event not found!")

    def delete_event(self):
        event_id = int(input("Enter event ID: "))

        if event_id in self.events:
            del self.events[event_id]
            print("Event deleted successfully!")
        else:
            print("Event not found!")

    def start_system(self):
        while True:
            print("\nEmployee Event Management System")
            print("1. Create Event")
            print("2. Read Event")
            print("3. Update Event")
            print("4. Delete Event")
            print("5. To know the attendance")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_event()
            elif choice == "2":
                self.read_event()
            elif choice == "3":
                self.update_event()
            elif choice == "4":
                self.delete_event()
            elif choice == "5":
                self.get_attendence_statistics()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")



ems = EventManagementSystem()
ems.start_system()
