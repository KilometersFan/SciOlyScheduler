class Coach:
    def __init__(self, team_number, name):
        self.team_number = team_number
        self.name = name
        self.time = None
        self.assigned_event = None
    def get_team_number(self):
        return self.team_number
    def get_name(self):
        return self.name
    def get_time(self):
        return self.time
    def set_time(self, time):
        self.time = time
    def get_event(self):
        return self.assigned_event
    def set_event(self, event_id):
        if isinstance(event_id, int):
            self.assigned_event = event_id
        else:
            print("Invalid argument passed. Looking for int!")
    def has_assigned_event(self):
        return self.assigned_event != None

    def print_info(self):
        print("Coach", self.name, "for Team", self.team_number)
        if self.has_assigned_event():
            print("Proctor for event", self.assigned_event)
            if self.get_time() is not None:
                print(self.get_time, "shift")
        else:
            print("Does not proctor an event")
    
    
        