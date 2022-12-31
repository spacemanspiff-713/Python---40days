import json

with open("bounus_examples/2.json","r") as file:
    content = file.read()

# print(type(content))

data = json.loads(content)

# print(type(data))
score = 0
for question in data:
    print(question["question_text"])
    for index, alternitive in enumerate(question["alternitives"]):
        print(f"{index + 1}: {alternitive}")
    user_choice = int(input("Enter your choice number:"))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score += 1

print(score)
