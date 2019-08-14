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
        self.events_remaining = list(self.events.keys())
        self.coaches = self.file_parser.get_coaches_as_map()
        self.coaches_remaining = list(self.coaches.keys())
        self.graph = self.file_parser.create_graph()
    def get_teams(self):
        return self.teams
    def get_events(self):
        return self.events
    def get_events_list(self):
        event_list = list(self.events.values())
        event_list.sort(reverse=True)
        # for event in event_list:
        #     print(str(event.get_id()), str(event.num_coaches))
        # print()
        return event_list
    def get_coaches(self):
        return self.coaches  
    def dfs(self, parent): 
        # Mark all the vertices as not visited 
        visited =[False]*(len(self.graph)) 
        # Create a queue for BFS 
        queue=[]
        s = 0
        t = len(self.events.values()) + len(self.coaches) + 1
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
        # Modified DFS 
        while queue: 
            u = queue.pop() 
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it             
            # normal iteration, goes through all neighbors, only used for source
            if(u == 0):
                for event in self.get_events_list(): 
                    if visited[event.get_id()] == False and self.graph[u][event.get_id()] > 0 and event.get_num() != len(event.get_coaches()) and len(event.get_potential_coaches()) > 0: 
                        queue.append(event.get_id()) 
                        visited[event.get_id()] = True
                        parent[event.get_id()] = u
            # only checks sink, used for the edges connecting coach to sink (since coach nodes only have edges to the sink in this graph)
            elif(u >= len(self.events)+1 and u <= len(self.events) + len(self.coaches)):
                if visited[t] == False and self.graph[u][t] > 0 :
                    queue.append(t) 
                    visited[t] = True
                    parent[t] = u
                    # if we've found a path from s to t, we have made a match between an event and coach
                    # so we can exit the loop
                    break
            # custom ordering of coach nodes since these edges will be ones from events to coaches
            # thus we need to make sure the most optimal coaches are looked at first (highest priority)
            elif(u > 0 and u <= len(self.events)):
                for priority,coach in self.events[u].get_potential_coaches():
                    # first check if the node is free to use and has some capacity left
                    if visited[coach.get_id()] == False and self.graph[u][coach.get_id()] > 0:
                        current_event = self.events[u]
                        current_coach = self.coaches[coach.get_id()]
                        team = self.teams[current_coach.get_team_number()-1]
                        # check the current coach node's teammate and see if the teammate's time shift is different than
                        # the current event's time shift
                        # if so, then you can add the current coach node to the bfs queue
                        if not any(teammate.get_time() == current_event.get_time() for teammate in team.get_teammate(current_coach)):
                            queue.append(coach.get_id())
                            visited[coach.get_id()] = True
                            parent[coach.get_id()] = u
                        # otherwise you cannot add the node to the bfs queue because no two coaches of the same team
                        # can be in events with the same time slot (both morning or both afternoon)
        # If we reached sink in DFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
    def ford_fulkerson(self): 
        # This array is filled by BFS and to store path 
        source = 0
        sink = len(self.events.values()) + len(self.coaches) + 1
        parent = [-1]*(len(self.graph)) 
        max_flow = 0
        # Augment the flow while there is path from source to sink 
        while self.dfs(parent):
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s != source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
            # Add path flow to overall flow 
            max_flow += path_flow
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v != source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow
                # assign coach to event and vice versa 
                if v >= len(self.events)+1 and v <= len(self.events) + len(self.coaches):
                    self.coaches[v].set_event(u)
                    self.coaches[v].set_time(self.events[u].get_time())
                    self.events[u].add_coach(self.coaches[v])
                    if u in self.events_remaining and self.events[u].get_num() == len(self.events[u].assigned_coaches):
                        self.events_remaining.remove(u)
                    self.coaches_remaining.remove(v)
                    # remove coaches from the events potential coaches, which will affect sorting and improve the outcome
                    self.events[u].potential_coaches = [pair for pair in self.events[u].potential_coaches if pair[1].get_id() != self.coaches[v].get_id() and not any(teammate.get_time() == self.events[u].get_time() for teammate in self.teams[pair[1].get_team_number()-1].get_teammate(pair[1])) and not pair[1].has_assigned_event()]         
                    self.events[u].reset_attributes()
                v = parent[v]
        return max_flow
    def fill_remaining(self):
        # loops over remaining events and coaches and matches them up arbitrarily while still making sure no coaches of the same team have the same time shift
        for id in self.events_remaining:
            while not self.events[id].has_coaches():
                potential_coach = self.find_match(self.events[id])
                if potential_coach:
                    self.events[id].add_coach(self.coaches[potential_coach])
                    self.coaches[potential_coach].set_event(id)
                    self.coaches[potential_coach].set_time(self.events[id].get_time())
                    self.coaches_remaining.remove(potential_coach)
                else:
                    print("No coaches more can be asisgned to this event!")
                    break
    def find_match(self, event):
        # handles checking if a coach can be assigned to an event based on the time shift of the coach's teammate(s)
        for id in self.coaches_remaining:
            teammates = self.teams[self.coaches[id].get_team_number()-1].get_teammate(self.coaches[id])
            if not any(teammate.get_time() == event.get_time() for teammate in teammates):
                return id
        return None
    def print_info(self):
        print("Event Information")
        for event in self.events.values():
            event.print_info()
        print("Excess Coaches:")
        for coach in self.coaches_remaining:
            print(self.coaches[coach].get_name())
        print()
        print("Team Information")
        for team in self.get_teams():
            team.print_info()
if __name__ == "__main__":
    s = Scheduler()
    print("Coaches assigned to a preferred event: ",s.ford_fulkerson())
    s.fill_remaining()
    s.print_info()