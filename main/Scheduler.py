from SciOlyScheduler.utility.Coach import Coach
from SciOlyScheduler.utility.Event import Event
from SciOlyScheduler.utility.Team import Team
from SciOlyScheduler.utility.FileParser import FileParser

class Scheduler:
    def __init__(self):
        self.file_parser = FileParser()
        file_parser.parse_coaches()
        file_parser.get_teams()
        file_parser.parse_events()
        self.events = file_parser.get_events()
        self.teams = file_parser.get_teams()
        self.coaches= file_parser.get_coaches()
        
    