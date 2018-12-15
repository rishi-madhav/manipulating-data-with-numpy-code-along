# --------------
import numpy as np
from collections import Counter
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
data_ipl = np.genfromtxt(path,delimiter = ',',skip_header = 1,dtype = str)
#print(data_ipl[:,3])

# How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
match_code_array = data_ipl[:,0]
#match_code_list = []
#for i in match_code_array:
 #   if i not in match_code_list:
  #      match_code_list.append(i)
#print(match_code_list)
#print(len(match_code_list))

num_unique_matches = len(set(match_code_array))
print("The number of unique matches in the dataset are",num_unique_matches)

# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
team1 = set(data_ipl[:,3])
team2 = set(data_ipl[:,4])
unique_teams = team1.union(team2)
print("The set of all unique teams that played in the matches are",unique_teams)

# An exercise to make you familiar with indexing and slicing up within data.
extras = data_ipl[:,17]
extras_num = extras.astype(int)
#extras_num2 = np.sum(extras_num)
#print(extras_num2)
print("The sum of all extras in all deliveries in all matches is",sum(extras_num))

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
filtered_ipl = data_ipl[data_ipl[:,-3] == 'SR Tendulkar']
delivery_num = filtered_ipl[:,-12]
wicket_type = filtered_ipl[:,-2]
print("The number of deliveries when Tendulkar got out is",delivery_num)
print("The ways that Tendulkar got out are",wicket_type)

# this exercise will help you get the statistics on one particular team
toss_winner_mask = (data_ipl[:,5] == 'Mumbai Indians')
toss_winner_data = data_ipl[toss_winner_mask]
unique_matches = set(toss_winner_data[:,0])
num_toss_winner_MI = len(unique_matches)
print("The number of matches MI team has won the toss are",num_toss_winner_MI)

# An exercise to know who is the most aggresive player or maybe the scoring player 
six_runs_mask = (data_ipl[:,-7] == '6')
data_ipl_filtered = data_ipl[six_runs_mask]
batsman_max_sixes = data_ipl_filtered[:,-10]
batsman_count = Counter(batsman_max_sixes)
print("The batsman who have scored the maximum no. of sixes is",batsman_count.most_common(2))






