#import poll
import os
import csv

#Open File
csvpath=os.path.join('/Users/anishak98/Desktop/Python-Challenge/PyPoll/Resources/election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # variables
    votes = []
    county = []
    candidates = []
    Charles = []
    Diana = []
    Raymon = []



    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #VOTE COUNT
    total_votes = (len(votes))

    #Votes for each candidate
    for candidate in candidates:
        if candidate == "Charles":
            Charles.append(candidates)
            charles_votes = len(Charles)
        elif candidate == "Diana":
            Diana.append(candidates)
            diana_votes = len(Diana)
        elif candidate == "Raymon":
            Raymon.append(candidates)
            raymon_votes = len(Raymon)
       
    charles_votes = len(Charles)
    diana_votes = len(Diana)
    raymon_votes = len(Raymon)

    #Percentages
    charles_percent = round(((charles_votes / total_votes) * 100), 2)
    diana_percent = round(((diana_votes / total_votes) * 100), 2)
    raymon_percent = round(((raymon_votes / total_votes) * 100), 2)

    
    #The Winner 
    if charles_percent > max(diana_percent, raymon_percent):
        winner = "Charles Casper Stockham"
    elif diana_percent > max(charles_percent, raymon_percent):
        winner = "Diana DeGette"  
    else:
        winner = "Raymon Anthony Doane"

#Print Statements

print(f"Election Results"+'\n') 
print(f"-----------------------------------"+'\n') 
print(f"Total Votes: {total_votes}" + "\n")
print(f"-----------------------------------"+ "\n") 
print(f"Stockham: {charles_percent}% ({charles_votes})"+ "\n") 
print(f"DeGette: {diana_percent}% ({diana_votes})"+ "\n") 
print(f"Doane: {raymon_percent}% ({raymon_votes})"+ "\n") 
print(f"-----------------------------------"+ "\n") 
print(f"Winner: {winner}"+ "\n") 
print(f"-----------------------------------")