from requests import get
pickup = get("https://vinuxd.vercel.app/api/pickup").json()["pickup"]
print(pickup)