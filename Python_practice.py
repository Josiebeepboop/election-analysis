print("Hello World!")

counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

# How to print from tuples
counties_tuple = ("Arapahoe","Denver","Jefferson")
for counties in (counties_tuple):
    print(counties)

# dictionary
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
# how to print the key
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
# How to print the values
for voters in counties_dict.values():
    print(voters)
for voter in counties_dict:
    print(counties_dict[voter])
for county in counties_dict:
    print(counties_dict.get(county))
# How to print key-value pairs
for county, voters in counties_dict.items():
    print(county, voters)
# Print how many voters each county has in a sentence
for county, voters in counties_dict.items(): 
    print(f'{county} county has {voters} registered voters.')

# Using a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters":422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}]
# Prints each dictionary in a separate line
for county_dict in voting_data:
    print(county_dict)
# Iterates through the list of dictionaries to print only the counties
for counties in range(len(voting_data)):
    print(voting_data[counties]["county"])
# Retrieve only values from each dictionary, we need to use a for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# Retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict["registered_voters"])
# Print only county name
for county_dict in voting_data:
    print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election?"))
# total_votes = int(input("What is the total votes in the election?"))
# percentage_votes = (my_votes / total_votes)*100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# # Using f-strings to simplify printing statements
# print(f'I received {my_votes / total_votes * 100}% of the total votes.')

# Multiple f-strings
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
# message_to_candidate = (
#     f'You received {candidate_votes} number of votes. '
#     f'The total number of votes in the election was {total_votes}. '
#     f'You received {candidate_votes / total_votes * 100} of the total votes')
# print(message_to_candidate)

# Format floating-point decimals
message_to_candidate = (
    f'You received {candidate_votes:,} number of votes.'
    f'The total number of votes in the election was {total_votes:,}.'
    f'You received {candidate_votes / total_votes * 100:.2f}% of the total votes.')
print(message_to_candidate)