from Coach import Coach
from Team import Team
from Event import Event
import csv

class FileParser:
    def __init__(self):
        self.events = {}
        self.coaches = []
        self.teams = {}
        self.total_events = 0
    def parse_events(self):
        file = open("C:/Users/milop/SciOlyScheduler/SciOlyScheduler/utility/events.csv", 'r', newline='')
        reader = csv.reader(file)
        next(reader)
        i = 1
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
        self.total_events = i-1
        file.close()
    def parse_teams(self):
        file = open("C:/Users/milop/SciOlyScheduler/SciOlyScheduler/utility/teams.csv",'r', newline='')
        reader = csv.reader(file)
        for i,row in enumerate(reader):
            team = Team(i+1, row[0])
            self.teams[row[0].lower()] = team
        file.close()
    def parse_coaches(self):
        file = open("C:/Users/milop/SciOlyScheduler/SciOlyScheduler/utility/coaches.csv", 'r', newline='')
        reader = csv.reader(file)
        i = 1
        for row in reader:
            if(row[0] == ''):
                continue
            team = self.teams[row[0].lower()]
            coach = Coach(team.get_number(), row[1], i+self.total_events)
            team.add_coach(coach)
            i += 1
            self.coaches.append(coach)
            for j in range(2, len(row), 2):
                event_list = self.events[row[j].lower()]
                if row[j+1].lower() == "no":
                    pair = (int(j/2), coach)
                else:
                    pair = (0, coach)
                for event in event_list:
                    event.add_potential_coach(pair)
        for event_list in self.events.values():
            for event in event_list:
                event.sort_coaches()
                # event.print_info()
        file.close()
    def create_graph(self):
        graph = []
        # get number of nodes in graph 
        event_num = len(self.get_events_as_map().values())
        coach_num = len(self.get_coaches())
        row = event_num + coach_num + 2
        # create empty graph (no edges)
        for i in range(0, row):
            graph.append([])
            for j in range(0, row):
                graph[i].append(0)
        # fill in edge weights
        # edges from source to events
        for i in range(1, event_num+1):
            graph[0][i] = self.get_events_as_map()[i].get_num()
        # edges from events to coaches
        for i in range(1, event_num+1):
            for priority,coach in self.get_events_as_map()[i].get_potential_coaches():
                graph[i][coach.get_id()] = 1
        # edges from coaches to sink
        for i in range(event_num+1, row-1):
            graph[i][row-1] = 1
        return graph
    def get_events(self):
        if len(self.events) > 0:
            return list(self.events.values())
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
    def get_coaches_as_map(self):
        coach_map = {}
        for coach in self.coaches:
            coach_map[coach.get_id()] = coach
        return coach_map
    def get_teams(self):
        if len(self.teams) > 0:
            # print(self.teams.values())
            return list(self.teams.values())
        else:
            print("No teams parsed.")
            return None

if __name__ == "__main__":
    fp = FileParser()
    fp.parse_teams()
    fp.parse_events()
    fp.parse_coaches()
    fp.create_graph()