import MySQLHelper
import csv

db_helper = MySQLHelper.MySQLHelper()


def country_data():
    csv_data = csv.reader(file('/Users/PradeepaShriJothinathan/Desktop/Spring_2017/DB_PROJECT1_PART1(1001241839_1001237691)/data/Country.csv'))
    for row in csv_data:
        Country_Name = row[0]
        Country_Name = Country_Name[1:-1]
        Population = float(row[1])
        No_of_Worldcup_won = int(row[2])
        Manager = row[3]
        Manager = Manager[1:-1]
        country_query = '''INSERT INTO COUNTRY(Country_Name, Population, No_of_Worldcup_won, Manager)
                            VALUES (%s, %s, %s, %s)''', (Country_Name, Population, No_of_Worldcup_won, Manager)
        db_helper.insert_data(query=country_query)


def players_data():
    csv_data = csv.reader(file('/Users/PradeepaShriJothinathan/Desktop/Spring_2017/DB_PROJECT1_PART1(1001241839_1001237691)/data/players.csv'))
    for row in csv_data:
        Player_id = int(row[0])
        Name = row[1]
        Name = Name[1:-1]
        Fname = row[2]
        Fname = Fname[1:-1]
        Lname = row[3]
        Lname = Lname[1:-1]
        DOB = row[4]
        DOB = DOB[1:-1]
        Country = row[5]
        Country = Country[1:-1]
        Height = int(row[6])
        Club = row[7]
        Club = Club[1:-1]
        Position = row[8]
        Position = Position[1:-1]
        Caps_for_Country = int(row[9])
        if row[10] == 'FALSE':
            IS_CAPTAIN = 0
        else:
            IS_CAPTAIN = 1
        player_query = '''INSERT INTO PLAYERS(Player_id, Name, Fname, Lname, DOB, Country, `Height(cms)`, Club, Position, Caps_for_Country, IS_CAPTAIN)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (Player_id, Name, Fname, Lname, DOB, Country, Height, Club, Position, Caps_for_Country, IS_CAPTAIN)
        db_helper.insert_data(query=player_query)


def match_results_data():
    csv_data = csv.reader(file('/Users/PradeepaShriJothinathan/Desktop/Spring_2017/DB_PROJECT1_PART1(1001241839_1001237691)/data/Match_results.csv'))
    for row in csv_data:
        Match_id = int(row[0])
        Date_of_Match = row[1]
        Date_of_Match = Date_of_Match[1:-1]
        Start_Time_Of_Match = row[2]
        Start_Time_Of_Match = Start_Time_Of_Match[1:-1]
        Team1 = row[3]
        Team1 = Team1[1:-1]
        Team2 = row[4]
        Team2 = Team2[1:-1]
        Team1_score = int(row[5])
        Team2_score = int(row[6])
        Stadium_Name = row[7]
        Stadium_Name = Stadium_Name[1:-1]
        Host_City = row[8]
        Host_City = Host_City[1:-1]
        match_results_query = '''INSERT INTO MATCH_RESULTS(Match_id, Date_of_Match, Start_Time_Of_Match, Team1, Team2, Team1_score, Team2_score, Stadium_Name, Host_City)
                                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', (Match_id, Date_of_Match, Start_Time_Of_Match, Team1, Team2, Team1_score, Team2_score, Stadium_Name, Host_City)
        db_helper.insert_data(query=match_results_query)


def player_cards_data():
    csv_data = csv.reader(file('/Users/PradeepaShriJothinathan/Desktop/Spring_2017/DB_PROJECT1_PART1(1001241839_1001237691)/data/Player_Cards.csv'))
    for row in csv_data:
        Player_id = int(row[0])
        Yellow_Cards = int(row[1])
        Red_Cards = int(row[2])
        player_cards_query = '''INSERT INTO PLAYER_CARDS(Player_id, Yellow_Cards, Red_Cards)
                                  VALUES (%s, %s, %s)''', (Player_id, Yellow_Cards, Red_Cards)
        db_helper.insert_data(query=player_cards_query)


def player_assists_goals_data():
    csv_data = csv.reader(file('/Users/PradeepaShriJothinathan/Desktop/Spring_2017/DB_PROJECT1_PART1(1001241839_1001237691)/data/Player_Assists_Goals.csv'))
    for row in csv_data:
        Player_id = int(row[0])
        No_of_Matches = int(row[1])
        Goals = int(row[2])
        Assists = int(row[3])
        Minutes_Played = int(row[4])
        player_assists_goals_query = '''INSERT INTO PLAYER_ASSISTS_GOALS(Player_id, No_of_Matches, Goals, Assists, Minutes_Played)
                                         VALUES (%s, %s, %s, %s, %s)''', (Player_id, No_of_Matches, Goals, Assists, Minutes_Played)
        db_helper.insert_data(query=player_assists_goals_query)

def close_connection():
    db_helper.close_connection()
