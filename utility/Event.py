from Coach import Coach
class Event:
    def __init__(self, id, name, time, num_coaches):
        self.id = id
        self.name = name
        self.time = time
        self.num = int(num_coaches)
        self.assigned_coaches = []
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
    def get_coaches(self):
        return self.assigned_coaches
    def add_coach(self, coach):
        if isinstance(coach, Coach):
            self.assigned_coaches.append(coach)
        else:
            print("Invalid argument passed. Looking for Coach!")
    def has_coaches(self):
        return self.num == len(self.assigned_coaches)
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
    def reset_attributes(self):
        new_num = 0
        new_zero = 0
        for pair in self.potential_coaches:
            new_num += 1
            if pair[0] == 0:
                new_zero += 1
        self.num_coaches = new_num
        self.num_zero_priority = new_zero
        # print("Num coaches", self.num_coaches, "Num zero", self.num_zero_priority)
    def sort_coaches(self):
        self.potential_coaches = sorted(self.potential_coaches, key=lambda x: x[0])
    def print_info(self):
        print("Event:",self.get_name(), "ID:", self.get_id())
        print(self.get_time(), "shift")
        print("Coach number:",self.get_num())
        if len(self.assigned_coaches) != self.num:
            print("Assigned Coaches: ")
            for coach in self.assigned_coaches:
                print(coach.get_name())
            print("Potential Coaches:")
            for coach_tuple in self.potential_coaches:
                if(not coach_tuple[1].has_assigned_event()):
                    print("Coach: ", coach_tuple[1].get_name(), "ID: ", coach_tuple[1].get_id(), ", Priority: ", coach_tuple[0])

        else:
            print("Assigned Coaches: ")
            for coach in self.assigned_coaches:
                print(coach.get_name())
        print()
    def __lt__(self, other):
        # prioritizes those with coaches who have done it before
        
        # if(self.num_zero_priority != other.num_zero_priority):
        #     if(self.num_zero_priority > 0 and other.num_zero_priority == 0):
        #         return True
        #     elif(self.num_zero_priority == 0 and other.num_zero_priority > 0):
        #         return False
        #     else:
        #         return self.num_zero_priority < other.num_zero_priority 
        # else:
        #     return self.num_coaches < other.num_coaches
        # prioritizes events with less coaches who are interested
        
        if(self.num_coaches < other.num_coaches):
            return True
        elif(self.num_coaches > other.num_coaches):
            return False
        else:
            if(self.num_zero_priority > 0 and other.num_zero_priority == 0):
                return True
            elif(self.num_zero_priority == 0 and other.num_zero_priority > 0):
                return False
            else:
                return self.num_zero_priority < other.num_zero_priority