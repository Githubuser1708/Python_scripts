# Define the function leaderboard(scorelist, new_score) that:
# Takes two arguments: a list of top 5 scores in decreasing order, and a new score
# Returns an updated list of top 5 scores

def  leaderboard(scorelist, new_score):
    scorelist.append(new_score)
    scorelist.sort(reverse=True)
    print(scorelist)
    return scorelist[0:5]

leaderboard([39,49,33,55,49,199,499], 99)
