from functools import reduce
import operator
import mysql.connector

db_in_use = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="04041963@Win",
  database="golfHandicap",
  auth_plugin='mysql_native_password'
)
mycursor = db_in_use.cursor()

def unpackTuple(tup):
  return (reduce(operator.add, tup))

#creating a list out of tuple list returned from query
#might turn into function
def getRoundScores(course,player):
  mycursor.execute(f"SELECT roundScore FROM roundsTbl WHERE courseID={course} AND playerID={player}")
  myresult = mycursor.fetchall()
  unpacked = unpackTuple(myresult)
  return unpacked

#using result of previous query to query for course rating and slope as list of ints
def getRates(course,tee):
  mycursor.execute(f"SELECT gcCourseRate,gcSlopeRate FROM teeYardsTbl WHERE courseID={course} AND teeID={tee}")
  myresult_1 = mycursor.fetchall()
  unpacked_1 = unpackTuple(myresult_1)
  return unpacked_1
