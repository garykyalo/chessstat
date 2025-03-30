import requests 
from datetime import datetime



def gamereviews(username):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://api.chess.com/pub/player/{username}/games/2025/03"
    response =  requests.get(url,headers = headers). json()
    games = response["games"]
    matches  = []
    for game in games:
        white = game["white"]
        black = game["black"]
        gameurl = game["url"]
        endtime = game["end_time"]
        dt = datetime.utcfromtimestamp(endtime)
        date = dt.strftime('%Y-%m-%d')
        time = dt.strftime('%H:%M')
        if white["username"] == username:
            opponent = black["username"]
            played = "white"
        else:
            opponent = white["username"]
            played = "black"
        match = {"timestamp": endtime, "opponent": opponent,  "date": date ,"time": time, "gameurl": gameurl, "played": played}
        matches.append(match)
    sorted_matches = sorted(matches, key=lambda x: x["timestamp"], reverse=True)
    return sorted_matches 


def ProcessScores():
    users = ["miranjidoc", "balleriontheblackdread", "garymark5", "MIRANJIDOC"]
    usersb = ["miranjidoc", "balleriontheblackdread"]
    headers = {
    "User-Agent": "Mozilla/5.0"
}
    results1 = []
    for user in usersb:
        print( user)
        url = f"https://api.chess.com/pub/player/{user}/games/2025/03"
        print(url)
        response =  requests.get(url,headers = headers). json()
        results = []
        data = response["games"]
        x = 0
        for item in data:
            white = item["white"]
            black = item["black"]
            url = item["url"]
            if black["username"] in users and white["username"] in users:
                x += 1
                result = {"white": white, "black": black}
                results.append(result)
        results1.extend(results)
        return results1