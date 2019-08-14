# SciOlyScheduler
## What is this?
The SciOlyScheduler is a scheduling system for Science Olympiad competitions. Given a list of events and coaches with their preferences, this program will assign coaches to proctor events and optimize the assignments so that events will be proctored by coaches who have proctored them before. Additionally, the program can be changed to maximize assignements solely for assigning coaches to thier preferred events.
## How to use
### Prerequisites
- Create a spreadsheet and fill the first column with the participating school names like so:

| School |
| ------ |
| Sample HS |
| Sample HS 2 |

- Download this file as a csv file and title it "teams.csv".
- Create a spreadsheet and fill in the columns with event information like so:

| Event | Proctors | Time |
| ----- | -------- | ---- |
| Towers | 2 | Morning |
| Boomilever | 1 | Afternoon |
| Chemistry Lab | 2 | Both |

- Be mindful of spelling errors when entering in values and note that "Both" means the event occurs in the morning and afternoon. Download this file as a csv and title it "events.csv".

- Create a spreadsheet and fill in the columns with coach information like so:

| School | Coach | Choice 1 | Run before? | Choice 2 | Run before? | Choice 3 | Run before? |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Sample HS | John Hancock | Chemistry Lab | No | Boomilever | Yes | Towers | No |

- Note that the number of choices are not restricted to 3 (must be >= 1). Also be mindful of spelling errors and make sure that the event and school names match those in the "teams.csv" and "events.csv" files. Download this file as a csv and title it "coaches.csv".

- Move the created csv files into the utility directory of the repository.

### Instructions 
- Install the latest version of Python3
- Clone this repository.
- Move into the utility directory.
- Type "python3 Scheduler.py"
- The results will be printed in the console. You will see each event and their assigned coaches, each team and the information of its members, and the coaches who were not assigned to any event. 
