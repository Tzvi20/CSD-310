update team
set team_id = 2,
    team_name = 'sauron'
where team_name = 'gandalf';
delete from team where team_name  = 'sauron';
insert into player (first_name, last_name, team_id)
    values('smeagol', 'shire folk', 1);
SELECT player_id, first_name, last_name, team_name
from player
Inner join team
on player.team_id = team.team_id;
# author: tzvi kaplan
# date: July 26 2023
#pysports_update_and_delete.py
# updates and deletes information from the pysports database
