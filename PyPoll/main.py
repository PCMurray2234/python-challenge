#open module
import os
import csv

#set total votes before election to "0"
total_votes= 0
#list of candidates
candidate_list = []
candidate_name = [] 
#set vote counter and vote % to "0"
candidate_vote = [0, 0, 0, 0,]
candidate_vote_percent = [0, 0, 0, 0]
candidate_winner = []

#results file
csvpath = os.path.join('Resources', 'election_data.csv')

# open and read csv file
with open(csvpath, newline='') as csvfile:

    #read and store
    csvreader= csv.reader(csvfile, delimiter=',')

    #skip csv header
    csv_header = next(csvreader)
    row = next(csvreader)

    #loop through file
    for row in csvreader:
        total_votes += 1
        candidate_list.append(str(row[2]))
    for row[2] in candidate_list:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] ==candidate_name[0]:
            candidate_vote[0] += 1
        elif row[2] == candidate_name[1]:
            candidate_vote[1] += 1
        elif row[2] == candidate_name[2]:
            candidate_vote[2] +=1
        elif row[2] == candidate_name[3]:
            candidate_vote[3] += 1

    #% of total vote for each candidate
    candidate_vote_percent[0] = round(100 * (candidate_vote[0] / total_votes), 4)
    candidate_vote_percent[1] = round(100 * (candidate_vote[1] / total_votes), 4)
    candidate_vote_percent[2] = round(100 * (candidate_vote[2] / total_votes), 4)
    candidate_vote_percent[3] = round(100 * (candidate_vote[3] / total_votes), 4)

    # calculate winner
    if candidate_vote[0] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]): candidate_winner = candidate_name[0]
    elif candidate_vote[1] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]): candidate_winner = candidate_name[1]
    elif candidate_vote[2] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]): candidate_winner = candidate_name[2]
    elif candidate_vote[3] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]): candidate_winner = candidate_name[3]

    # print screen
    print("election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})")
    print(f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})")
    print(f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})")
    print(f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})")
    print("-------------------------")
    print(f"Winner: {candidate_winner}")

    # path to text file output folder
    output_file = os.path.join('Resources', 'election_Results.txt')

    with open(output_file, 'w', newline='') as text_file:

        #write report to text file in output folder
        print("Election Results", file=text_file)
        print("---------------------", file=text_file)
        print(f"Total Votes: {total_votes}", file=text_file)
        print("---------------------", file=text_file)
        print(f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})", file=text_file)
        print(f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})", file=text_file)
        print(f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})", file=text_file)
        print(f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})", file=text_file)
        print("---------------------", file=text_file)
        print(f"Winner: {candidate_winner}", file=text_file)

        csvfile.close()

        # People I read and took ideas and pieces of code from for both PyPoll and PyBank:
# bigbluey, AllenRayC, blueskiesatx, 
# # https://stackoverflow.com/questions/42847440/in-python-writing-to-a-text-file-not-working In Python, writing to a text file not working
# Kahn Acaddemy \ Philip Guo, Python Tutor and Writer
# YK Sugishita \ CS Dojo
