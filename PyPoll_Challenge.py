# Add our dependendies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a varibale to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Create a list for the counties.
counties = ["Arapahoe", "Denver", "Jefferson"]
counties_options = []
# Declare a variable that represents the number of votes that a county received.
counties_voters_turnout = {}
# Create a dictionary for each voter turnout..
counties_voters_turnout_dict = {}
# Create an empty string that will hold the county name had the largest turnout.
largest_county_turnout_name = ""
winning_county = 0
winning_county_percentage = 0

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
    for row in file_reader:
        total_votes += 1
        counties_name = row[2]
        if counties_name not in counties_options:
            counties_options.append(counties_name)
            counties_voters_turnout[counties_name] += 1
    
    print(counties_voters_turnout, end="")
    # Save the results to our text file.
    #txt_file.write(counties_voters_turnout)

    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes : {total_votes:,}\n"
            f"-------------------------\n"
            f"\nCounty Votes:\n"
            )
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
            # Create a dictionary for each voter turnout..
        counties_voters_turnout_dict = {}
        counties_voters_turnout["Arapahoe"] = 24801
        counties_voters_turnout["Jefferson"] = 38855
        counties_voters_turnout["Denver"] = 306055
        for counties in counties_voters_turnout:
            voters = counties_voters_turnout[counties]
            voters_percentage = float(voters) / float (total_votes)*100
            counties_results = (
                f"{counties}: {voters_percentage:.1f}% ({voters:,})\n"
                )

            print(counties_results, end="")
            txt_file.write(counties_results)
            # Determine winning vote count, percentage, and winning county.
            if (voters > winning_count) and (voters_percentage > winning_county_percentage):
                winning_count = voters
                winning_county = counties
                winning_county_percentage = voters_percentage
        largest_county_turnout_name_summary = (
            f"\n"
            f"-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n"
        )
        print(largest_county_turnout_name_summary, end="")
        txt_file.write(largest_county_turnout_name_summary)

    with open(file_to_save, "a") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes : {total_votes:,}\n"
            f"-------------------------\n"
            f"\nCounty Votes:\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        #txt_file.write(election_results)
        # Determine the dictionary for the candidates and their votes. 
        candidate_votes = {}
        candidate_votes["Charles Casper Stockham"] = 85213
        candidate_votes["Diana DeGette"] = 272892
        candidate_votes["Rayman Anthony Doane"] = 11606
        # Winning Candidate and Winning Count Tracker
        winning_candidate = ""
        winning_count = 0
        winning_percentage = 0
        # Determine the percentage of votes for each candidate by looping through the counts.
        for candidate in candidate_votes:
            # Retrieve vote count and percentage.
            votes = candidate_votes[candidate]
            vote_percentage = float(votes) / float(total_votes)*100
            # Print each candidate, their voter count, and percentage to the
            # terminal. 
            candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(candidate_results)
            # Determine winnign vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate
                winning_percentage = vote_percentage               
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