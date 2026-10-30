# The General Knowledge Quiz (Extended)

questions = [
    {"q": "What is the capital of France?", "answers": ["paris"], "display": "Paris"},
    {"q": "Which planet is known as the Red Planet?", "answers": ["mars"], "display": "Mars"},
    {"q": "How many continents are there on Earth?", "answers": ["7", "seven"], "display": "7"},
]

score = 0
total = len(questions)

print("Welcome to the General Knowledge Quiz!")
print("-" * 40)

for number, item in enumerate(questions, start=1):
    answer = input(f"Q{number}: {item['q']} ").strip().lower()

    if answer in item["answers"]:
        print("Correct! +1 point\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {item['display']}.\n")

# Final score
print("-" * 40)
print(f"Quiz finished! Your final score: {score}/{total}")

# Message based on score
if score == total:
    print("Excellent! Perfect score!")
elif score >= 2:
    print("Good job! Almost there.")
elif score == 1:
    print("Not bad, keep practicing!")
else:
    print("Try again, you can do better!")
