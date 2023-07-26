SELECT player_id, first_name, last_name, team_name
from player
Inner join team
    on player.team_id = team.team_id;
select player_id, first_name, last_name, team_name
from player
left outer join team
    on player.team_id = team.team_id;
select player_id, first_name, last_name, team_name
from player
right outer join team
    on player.team_id = team.team_id;
select first_name, last_name
from player where player_id = 3;
select player_id, first_name, last_name, team_name
from player
inner join team
    on player.team_id = team.team_id;
