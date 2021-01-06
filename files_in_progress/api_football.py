import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-key': "8170b7d23273ff036180c8da96206def",
    'x-rapidapi-host': "https://v3.football.api-sports.io/"
    }

conn.request("GET", "/teams/statistics?season=2020&team=48&league=2790", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
