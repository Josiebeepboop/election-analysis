# count = 7
# while count < 1:
#     print("Hello World!")

# for county in counties:
#     print(county)

# counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
# for county, voters in counties_dict.items():
#     print(f'{county} county has {voters:,} registered voters.')

voting_data = [{"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}
                ]
# for county_dict in voting_data:
#     print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")
# for i, county_dict in enumerate(voting_data):
#     print(f"{i}. {county_dict['county']} county has {county_dict['registered_voters']} registered voters.")
#     print(county_dict.get('population'))
# jeff = voting_data.index({"county":"Jefferson","registered_voters":432438})
# print(voting_data[jeff]['registered_voters'])
# my_list = ['a', 1, 'b', 2]
# print(my_list.index('b'))
for county_dict in voting_data:
    if county_dict['county'] == "Jefferson":
        print(f"{county_dict['registered_voters']}")

new_v_d = [c for c in voting_data]
print(new_v_d)

county_names = [c['county'] for c in voting_data]
print(county_names)

big_counties = [c for c in voting_data if c['registered_voters'] > 422829]
print(big_counties)

voter_numbers = [c['registered_voters'] for c in voting_data if c['county'] == "Jefferson"]
print(voter_numbers[0])
print(type(voter_numbers))
print(type(voter_numbers[0]))

jefferson_voters = [c['registered_voters'] for c in voting_data if c['county'] == "Jefferson"][0]
print(type(jefferson_voters),jefferson_voters)