# count = 7
# while count < 1:
#     print("Hello World!")

# for county in counties:
#     print(county)

counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')

voting_data = {"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}
print(f"{voting_data['county']} county has {voting_data['registered_voters']} registered voters.")
