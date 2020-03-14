# Add our dependendies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a varibale to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
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
# Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"--------------------------\n"
            f"Total Votes : 369,711\n"
            f"--------------------------\n")
        print(election_results, end="")
        # Save the final vate count to the text file.
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate in candidate_votes:
            # Retrieve vote count and percentage.
            votes = candidate_votes[candidate]
            vote_pecentage = float(votes) / float(total_votes)*100
            # Print each candidate, their voter count, and percentage to the
            # terminal. 
            candidate_results = (
                f"{candidate}: {vote_pecentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(candidate_results)
            # Determine winnign vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_pecentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate
                winning_percentage = vote_pecentage               
        # To do: print out the winning candidate, vote count and percentage to
        # terminal
        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candiadte's results to the text file.
        txt_file.write(winning_candidate_summary)
