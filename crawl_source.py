# -*- coding: utf-8 -*-
import datetime
from dateutil.relativedelta import relativedelta
import mariaDB,json

def time_calc():
    return_val = dict()
    y = int(raw_input('시작년도 :'))
    m = int(raw_input('월 :'))

    yy = int(raw_input('종료년도 :'))
    mm = int(raw_input('월 :'))

    start = datetime.date(y, m, 1)
    end = datetime.date(yy, mm, 1) + relativedelta(months=1)

    diff = (relativedelta(end,start).years*12) + relativedelta(end,start).months
    for i in range(diff/2):
        temp_end = start + relativedelta(months=2)
        return_val[start] = temp_end - datetime.timedelta(days=1)
        start = temp_end
    if relativedelta(end,start).months!=0:
        temp_end = start + relativedelta(months=1)
        return_val[start] = temp_end - datetime.timedelta(days=1)
    return return_val

def load_key_value():
    with open('key_values.txt','r') as f:
        result = f.read()
    result = result.split()
    return result

def mariadb_json(json_data):
    c= json.loads(json_data)
    keys = load_key_value()

    str1 = 'INSERT INTO mat_dat_15_16 (round, date, Home_Team, Away_Team'

    str2 = "VALUES ('"
    str2 = str2 + str(c['SoccerFeed']['SoccerDocument']['Competition']['Stat'][3]['@value']) + "','"
    str2 = str2 + str(c['SoccerFeed']['SoccerDocument']['MatchData']['MatchInfo']['Date'][:8]) + "','"  # Date append
    str2 = str2 + str(c['SoccerFeed']['SoccerDocument']['Team'][0]['Name']) + "','"  # Home team name append
    str2 += str(c['SoccerFeed']['SoccerDocument']['Team'][1]['Name'])  # Away team name append

    home_stat = c['SoccerFeed']['SoccerDocument']['MatchData']['TeamData'][0]['Stat']
    away_stat = c['SoccerFeed']['SoccerDocument']['MatchData']['TeamData'][1]['Stat']

    for home_value in home_stat:
        if(home_value['@attributes']['Type'] not in keys): continue
        str1 += ',' + str(home_value['@attributes']['Type'])
        str2 += "','" + str(home_value["@value"])
    for away_value in away_stat:
        if(away_value['@attributes']['Type'] not in keys): continue
        str1 += ',A' + str(away_value['@attributes']['Type'])
        str2 += "','" + str(away_value["@value"])

    str1 += ')'
    str2 += "');"
    insert_str = str1 + str2

    print insert_str

    #mariaDB.create_db_table(insert_str,'goal_statistics')
    print str(c['SoccerFeed']['SoccerDocument']['MatchData']['MatchInfo']['Date'][:8]) + ' ' \
          + str(c['SoccerFeed']['SoccerDocument']['Team'][0]['Name']) + ' DB Write Complete'

