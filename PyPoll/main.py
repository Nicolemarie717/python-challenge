import csv
import os

csvpath = os.path.join('onedrive', 'Data Science', 'Resources', 'Module_3', 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

total_votes = 0 

canidate_options = []
canidate_votes = {}

county_list = []
county_votes = {}

winning_canidate = ""
winning_count = 0 
winning_percentage = 0 

largest_c_turnout = ""
largest_v_turnout = 0 

reader = csv.reader('election_data.csv')

total_votes = total_votes + 1 
candidate_name = row = [2]
county_name = row = (1)
if candidate_name not in canidate_options:
    canidate_options.append(candidate_name)
    canidate_votes[candidate_name] += 1 
if county_name not in county_list:
    county_list.append(county_name)
    county_votes[county_name] = 0
    county_votes[county_name] += 1


print('Election Results')
print("-------------------------------------")
print('Total Votes : ' + str(total_votes))
print("-------------------------------------")
print("Khan : " + str('{:,.2%}'.format("Khan"/total_votes)+" " + str("Khan")))
print("Correy : " + str('{:,.2%}'.format("Correy"/total_votes)+" " + str("Correy")))
print("Li : " + str('{:,.2%}'.format("Li"/total_votes)+ " " +  str(Li)))
print("O'Tooley : " + str('{:,.2%}'.format("O'Tooley"/total_votes)+" " + str("O'Tooley")))
print("-------------------------------------")