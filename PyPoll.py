import datetime
now = datetime.datetime.now()
print("The time right now is,", now)
# Add our dependendies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a varibale to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as elecion_data:
    file_reader = csv.reader(elecion_data)


    #Read header row.
    headers = next(file_reader)

    # Print each row in the csv file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
             # Add the candidate name to the candidate list.
             candidate_options.append(candidate_name)

             # Begin tracking that candidate's vote count.
             candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


# Print the candidate vote dictionary.
print(candidate_votes)

# Print the candidate list.
print(candidate_options)
# 3. Print the total votes.
print(total_votes)

#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    #Write some data to the file.

#Write thtee counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

