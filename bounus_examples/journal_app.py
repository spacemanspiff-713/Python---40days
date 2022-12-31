import json

with open("journal_app/2.txt", "r") as file:
    x = file.read()
    y = json.loads(x)
    y["age"] = "45"

print(y)

