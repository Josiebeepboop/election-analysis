# The data we need to retrieve. Does the sequence matter here?
import csv
import os

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('Analysis','election_analysis.txt')
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data.
    # print(election_data)
    # read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the csv file
    # for row in file_reader:
    #     print(row)
    # Print the header row.
    headers = next(file_reader)
    print(headers)


# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")




