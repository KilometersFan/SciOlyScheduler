from Coach import Coach
class Team:
    def __init__(self, number, name):
        self.number = number
        self.coaches = []
        self.name = name
    def add_coach(self, coach):
        if isinstance(coach, Coach):
            self.coaches.append(coach)
        else: 
            print("Invalid argument passed. Looking for Coach!")
    def get_teammate(self, coach):
        if coach in self.coaches:
            return [other_coach for other_coach in self.coaches if other_coach != coach]
        else:
            return None
    def get_coaches(self):
        return self.coaches
    def get_number(self):
        return self.number
    def get_name(self):
        return self.name
    def print_info(self):
        print("Team", self.get_number(), ":", self.get_name())
        print("Coaches:")
        if len(self.get_coaches()) > 0:
            for coach in self.get_coaches():
                coach.print_info()
                print()
        else: 
            print("No Coaches")
        print()

if __name__ == "__main__":
    pass
