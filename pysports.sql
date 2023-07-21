-- Active: 1689893229423@@localhost@3306@pysports
CREATE USER 'pysports_user'@'localhost'IDENTIFIED WITH mysql_native_password BY 'MySQLIsGreat!';
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';
DROP USER IF EXISTS 'pysports_user'@'locahost';
CREATE TABLE team (
    team_id INT  NOT NULL  AUTO_INCREMENT,
    team_name VARCHAR(75) NOT NULL,
    mascot VARCHAR (75)   NOT NULL,
    PRIMARY KEY(team_id)
);
CREATE TABLE team (
    player_id INT  NOT NULL  AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR (75)   NOT NULL,
    PRIMARY KEY(player_id)
    CONSTRAINT(player) fk_team
    FOREIGN KEY((team_id))
    REFERENCES team(team_id)
);
INSERT INTO team(team_name, mascot)
    VALUES('Team Gandald', 'White Wizards');
    DROP TABLE IF EXISTS player;
    SELECT team_id FROM team WHERE team_name = 'Team Sauron')
    #Title: SQL_instructions
    #Author: Tzvi Kaplan
    #Date: 20 July 2023
    # SQL_instructions
import mysql.connector
from mysql.connector import errorcode

# 
config = {
    "user": "root",
    "password": "Trump2024",
    "host": "localhost",
    "database": "pysports",
    "port": 3306
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
        db.close()//
                