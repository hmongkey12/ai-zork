import requests

url = "http://0.0.0.0:2224"

resp = requests.get(f"{url}/scenarios")
#print(resp)
#print(resp.json())

scenes= resp.json()
for scene in scenes:
    print(f"story of {scene} {scenes[scene]}\n")
