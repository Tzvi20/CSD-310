-- Active: 1689893229423@localhost@3306@pysports
#author: Tzvi Kaplan
#date: July 23 2023
#sql_queries.py
#description:query the pysports database for team and player information
import mysql.connector
from mysql.connector import errorcode
try:
    pysports = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Trump2024",
        database="pysports"
    )
    cursor = pysports.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()
    for team in teams:
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))


    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()

    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))
    cursor.close()
    pysports.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Error: {}".format(err))