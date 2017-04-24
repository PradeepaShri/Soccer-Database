tee /Users/Naren/Desktop/Database_Project_1/log.txt

create Schema WORLD_CUP_2014;

create table WORLD_CUP_2014.COUNTRY (
Country_Name Varchar(20),
Population decimal(10,2),
No_of_Worldcup_won int,
Manager varchar (20),
PRIMARY KEY(Country_Name));

create table WORLD_CUP_2014.PLAYERS (
Player_id int,
Name varchar (40),
Fname varchar (20),
Lname 	varchar (35),
DOB date,
Country varchar(20),
`Height(cms)` int,
Club varchar(30),
Position varchar(10),
Caps_for_Country int,
IS_CAPTAIN Boolean,
PRIMARY KEY(Player_id),
FOREIGN KEY(Country) REFERENCES WORLD_CUP_2014.COUNTRY(Country_Name));

create table WORLD_CUP_2014.MATCH_RESULTS (
Match_id int,
Date_of_Match date,
Start_Time_Of_Match time,
Team1 varchar(25),
Team2 varchar(25),
Team1_score int,
Team2_score int,
Stadium_Name varchar(35),
Host_City varchar(20),
PRIMARY KEY(Match_id),
FOREIGN KEY(Team1) REFERENCES WORLD_CUP_2014.COUNTRY(Country_Name),
FOREIGN KEY(Team2) REFERENCES WORLD_CUP_2014.COUNTRY(Country_Name));

create table WORLD_CUP_2014.PLAYER_CARDS(
Player_id int,
Yellow_Cards int,
Red_Cards int,
PRIMARY KEY(Player_id),
FOREIGN KEY(Player_id) REFERENCES WORLD_CUP_2014.PLAYERS(Player_id));

create table WORLD_CUP_2014.PLAYER_ASSISTS_GOALS (
Player_id int,
No_of_Matches int,
Goals int,
Assists int,
Minutes_Played int,
PRIMARY KEY(Player_id),
FOREIGN KEY(Player_id) REFERENCES WORLD_CUP_2014.PLAYERS(Player_id));

notee