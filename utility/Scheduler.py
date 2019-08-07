from Coach import Coach
from Event import Event
from Team import Team
from FileParser import FileParser
import functools
class Scheduler:
    def __init__(self):
        self.file_parser = FileParser()
        self.file_parser.parse_teams()
        self.file_parser.parse_events()
        self.file_parser.parse_coaches()
        self.teams = self.file_parser.get_teams()
        self.events = self.file_parser.get_events_as_map()
        self.coaches= self.file_parser.get_coaches()
        self.graph = self.file_parser.create_graph()
        for row in self.graph:
            print(row)
    def get_teams(self):
        return self.teams
    def get_events(self):
        return self.events
    def get_events_list(self):
        return list(self.events.values())
    def get_coaches(self):
        return self.coaches

if __name__ == "__main__":
    s = Scheduler()
    events = s.get_events_list()
    events.sort()
    for event in events:
        event.print_info()