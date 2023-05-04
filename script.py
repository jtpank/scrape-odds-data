#bovada endpoint:
# https://www.bovada.lv/services/sports/event/v2/events/A/description/basketball/nba
#
#
# DraftKings, 
# https://sportsbook.draftkings.com/event/den-nuggets-%40-pho-suns/28832865 example for data
#https://api.draftkings.com/sites/US-DK/sports/v1/sports?format=json
#
#FanDuel, BetMGM, Caesars, Bovada, MyBookie.ag
import requests
import json

BOVADA_URL = "https://www.bovada.lv/services/sports/event/v2/events/A/description/basketball/nba"



def make_request(url):
    response = requests.get(url)
    return response.json() if response and response.status_code == 200 else None

def main():

    with open('get_req_odds.json', 'r') as f:
        data = json.load(f)
        print(len(data))
        for i in range(len(data)):
            currentGame = data[i]
            print(currentGame['home_team'], "at" ,currentGame['away_team'], '\n')
            for book in currentGame['bookmakers']:
                print('\t\t',book['title'])
                for market in book['markets']:
                    team1 = market['outcomes'][0]
                    team2 = market['outcomes'][1]
                    print('\t\t\t', market['key'],team1['name'], team1['price'], team2['name'], team2['price'])



if __name__ == "__main__":
    main()
