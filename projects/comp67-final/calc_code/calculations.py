# The basic calculation of a golf handicap is as follows

# handicap index = handicap differential x 0.96

# differential can be calculated per round using the following formula:
# [(a-b) * 113]/C = d

# where: 
# a is the adjusted gross score
# b is the course rating as provided by the governing body/course
# c is the slope rating as provided by the governing body/course

#  depending on how many scores are input for a course, an average of the differentials should be taken 
#  for use in the handicap differential equation

#  i.e.
# 5-6 scores submitted = Lowest differential
# 7-8 scores submitted = avg of 2 lowest differentials
# 9-10 scores submitted = avg of 3 lowest differentials
# 11-12 scores submitted = avg of lowest 4 differentials

def difList(scores,rates):
    hand_diff_list = []
    for score in scores:
        crs_rate = rates[0]
        crs_slope = rates[1]
        hand_diff = ((score - crs_rate)*113) / crs_slope
        hand_diff_list.append(hand_diff)
    return hand_diff_list

def hIndex(x_list):
    #sorting the list as the lowest single diff should be pulled
    sort_diffs = sorted(x_list)
    #final handicap index
    if len(x_list) <= 6:
        hand_diff = sort_diffs[0]
        return hand_diff * 0.96
    elif len(x_list) > 6 and len(x_list) <= 8:
        hand_diff = (sort_diffs[0]+sort_diffs[1])/2
        return hand_diff * 0.96
    elif len(x_list) > 8 and len(x_list) <= 10:
        hand_diff = (sort_diffs[0]+sort_diffs[1]+sort_diffs[2])/3
        return hand_diff * 0.96
    elif len(x_list) > 10 and len(x_list) <= 12:
        hand_diff = (sort_diffs[0]+sort_diffs[1]+sort_diffs[2]+sort_diffs[3])/4
        return hand_diff * 0.96

def printHdcpIndex(hInd):
    print(f'Your handicap index for the course is: {int(hInd)}')
