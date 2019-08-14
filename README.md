# SciOlyScheduler
## What is this?
The SciOlyScheduler is a scheduling system for Science Olympiad competitions. Given a list of events and coaches with their preferences, this program will assign coaches to proctor events and optimize the assignments so that events will be proctored by coaches who have proctored them before. Additionally, the program can be changed to maximize assignements solely for assigning coaches to thier preferred events. The program will make sure that no coaches from the same team will be assigned to the same time shift, which ensures that a coach will always be with their students.
## How to use
### Prerequisites
1. Create a spreadsheet and fill the first column with the participating school names like so:

| School |
| ------ |
| Sample HS |
| Sample HS 2 |

2. Download this file as a csv file and title it "teams.csv".

3. Create a spreadsheet and fill in the columns with event information like so:

| Event | Proctors | Time |
| ----- | -------- | ---- |
| Towers | 2 | Morning |
| Boomilever | 1 | Afternoon |
| Chemistry Lab | 2 | Both |

- Note: Be mindful of spelling errors when entering in values and note that "Both" means the event occurs in the morning and afternoon. Also, the "Proctors" value should be the number of coaches assigned to each time shift. In the above example, Chemistry Lab will have a total of 4 proctors since it is run in both the morning and afternoon, but the value entered in the spreadsheet should be 2 because each shift has 2 coaches. 
4. Download this file as a csv and title it "events.csv".

5. Create a spreadsheet and fill in the columns with coach information like so:

| School | Coach | Choice 1 | Run before? | Choice 2 | Run before? | Choice 3 | Run before? |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Sample HS | John Hancock | Chemistry Lab | No | Boomilever | Yes | Towers | No |

- Note: The number of choices are not restricted to 3 (at least 1). 
5. Download this file as a csv and title it "coaches.csv".
6. Move the created csv files into the utility directory of the repository.

- Note: A lot of the following should be automated using Google Forms or similar software because the initialization of the program is dependent on spelling-sensitive file parsing. This program will <b>not</b> work properly if spelling is not checked. For instance, if an event is labeled "Chemistry Lab" in "events.csv" but a coach lists "Chem Lab" as one of their preferred events, the program will not recognize the coach's preference as a valid event.
### Instructions 
1. Install the latest version of Python3
2. Clone this repository.
3. Move into the utility directory of this repository.
4. Type `python3 Scheduler.py` into the window.
5. After the program has run, the results will be printed in the console. You will see each event and their assigned coaches, each team and the information of its members, and the coaches who were not assigned to any event. 
