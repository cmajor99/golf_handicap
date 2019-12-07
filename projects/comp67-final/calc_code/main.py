from calculations import printHdcpIndex,difList,hIndex
from query_funcs import getRates,getRoundScores

#query database for scores based on courseID(arg 1) and playerID(arg 2)
player1_scores = getRoundScores(1,1)

#query database for scores based on courseID(arg 1) and teeID(arg 2)
player1_rates = getRates(2,4)

#storing list of differentials for hIndex calculation
play1_diffs = difList(player1_scores,player1_rates)

#calculating based on size of differential list
play1_hIndex = hIndex(play1_diffs)

#printing the final result
printHdcpIndex(play1_hIndex)









