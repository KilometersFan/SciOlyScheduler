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
        coach_names = []
        s = ", "
        for coach in self.get_coaches():
            if coach is not None:
                coach_names.append(coach.get_name())
        if len(coach_names) != 0:
            print("Team Coaches: ", s.join(coach_names))
        else: 
            print("No Coaches")

if __name__ == "__main__":
    sample_team = Team(3, "Test")
    coach1 = Coach(1, "M")
    coach2 = Coach(1, "P")
    sample_team.add_coach(coach1)
    sample_team.add_coach(coach2)
    sample_team.print_info()
