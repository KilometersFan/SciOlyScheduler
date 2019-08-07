from Coach import Coach
from Team import Team
from Event import Event
import csv

class FileParser:
    def __init__(self):
        self.events = {}
        self.coaches = []
        self.teams = {}
    def parse_events(self):
        file = open("../input/events.csv", newline='')
        reader = csv.reader(file)
        next(reader)
        i = 0
        for row in reader:
            if(row[2] == 'Both'): 
                event1 = Event(i, row[0], "Morning", row[1])
                event2 = Event(i+1, row[0], "Afternoon", row[1])
                self.events[row[0].lower()] = [event1, event2]
                i += 1
            else:
                event = Event(i, row[0], row[2], row[1])
                self.events[row[0].lower()] = [event]
            i += 1
    def parse_teams(self):
        file = open("../input/teams.csv", newline='')
        reader = csv.reader(file)
        for i,row in enumerate(reader):
            team = Team(i+1, row[0])
            self.teams[row[0].lower()] = team
        # print(self.teams.keys())
    def parse_coaches(self):
        file = open("../input/coaches.csv", newline='')
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == ''):
                continue
            team = self.teams[row[0].lower()]
            coach = Coach(team.get_number(), row[1])
            for i in range(2, len(row), 2):
                # print(row[i].lower())
                event_list = self.events[row[i].lower()]
                if row[i+1].lower() == "no":
                    pair = (int(i/2), coach)
                else:
                    pair = (0, coach)
                for event in event_list:
                    event.add_potential_coach(pair)
        # for event_list in self.events.values():
        #     for event in event_list:
        #         event.print_info() 
    def get_events(self):
        if len(self.events) > 0:
            return self.events.values
        else:
            print("No events parsed.")
            return None
    def get_events_as_map(self):
        event_map = {}
        for value in self.events.values():
            for event in value:
                event_map[event.get_id()] = event
        return event_map
    def get_coaches(self):
        if len(self.coaches) > 0:
            return self.coaches
        else:
            print("No coaches parsed.")
            return None
    def get_teams(self):
        if len(self.teams) > 0:
            return self.teams.values
        else:
            print("No coaches parsed.")
            return None


if __name__ == "__main__":
    fp = FileParser()
    fp.parse_teams()
    fp.parse_events()
    fp.parse_coaches()