from Coach import Coach
class Event:
    def __init__(self, id, name, time, num_coaches):
        self.id = id
        self.name = name
        self.time = time
        self.num = int(num_coaches)
        self.assigned_coach = None
        self.potential_coaches = []
        self.num_coaches = 0
        self.num_zero_priority = 0
    def get_name(self):
        return self.name
    def get_time(self):
        return self.time
    def get_num(self):
        return self.num
    def get_id(self):
        return self.id
    def get_coach(self):
        return self.assigned_coach
    def set_coach(self, coach):
        if isinstance(coach, Coach):
            self.assigned_coach = coach
        else:
            print("Invalid argument passed. Looking for Coach!")
    def add_potential_coach(self, coach_priority_pair):
        if(isinstance(coach_priority_pair, tuple) and isinstance(coach_priority_pair[0], int) and isinstance(coach_priority_pair[1], Coach)):
            self.potential_coaches.append(coach_priority_pair)
            if(coach_priority_pair[0] == 0):
                self.num_zero_priority += 1
            self.num_coaches += 1
        else:
            print("Invalid argument passed.")
    def get_potential_coaches(self):
        return self.potential_coaches
    def sort_coaches(self):
        self.potential_coaches = sorted(self.potential_coaches, key=lambda x: x[0])
    def print_info(self):
        print("Event:",self.get_name(), "ID:", self.get_id())
        print(self.get_time(), "shift")
        if self.assigned_coach is None:
            print("Potential Coaches:")
            for coach_tuple in self.potential_coaches:
                print("Coach: ", coach_tuple[1].get_name(), "ID: ", coach_tuple[1].get_id(), ", Priority: ", coach_tuple[0])
        else:
            print("Assigned Coach: ", self.assigned_coach)
        print()
    def __lt__(self, other):
        if(self.num_zero_priority != other.num_zero_priority):
            if(self.num_zero_priority > 0 and other.num_zero_priority == 0):
                return True
            elif(self.num_zero_priority == 0 and other.num_zero_priority > 0):
                return False
            else:
                return self.num_zero_priority < other.num_zero_priority 
        else:
            return self.num_coaches < other.num_coaches