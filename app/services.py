import requests 

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
            if black["username"] in users and white["username"] in users:
                x += 1
                result = {"white": white, "black": black}
                results.append(result)
        results1.extend(results)
        return results1