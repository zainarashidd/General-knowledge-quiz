# The General Knowledge Quiz

A simple command-line quiz game built in Python as part of the **DecodeLabs Python Programming Industrial Training Kit (Project 4)**.

## Goal

Ask the player general knowledge questions, keep a score counter (+1 point for every correct answer), and print the final score at the end.

## Key Skills

- Variables
- If / Elif / Else logic (Control Flow)
- Lists and dictionaries
- Loops (`for` with `enumerate`)
- String handling (`.strip()`, `.lower()`) and f-strings

## Features

- Questions stored in a list, so adding a new one takes a single line
- Case-insensitive answers ("Paris", "PARIS", " paris " all work)
- Multiple accepted answers per question (e.g. `7` or `seven`)
- Final score shown as `score/total`
- Feedback message based on the final score

## How to Run

1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repository or download `quiz.py`
3. Run in your terminal:

```bash
python quiz.py
```

## Sample Output

```
Welcome to the General Knowledge Quiz!
----------------------------------------
Q1: What is the capital of France? paris
Correct! +1 point

Q2: Which planet is known as the Red Planet? venus
Wrong! The correct answer is Mars.

Q3: How many continents are there on Earth? 7
Correct! +1 point

----------------------------------------
Quiz finished! Your final score: 2/3
Good job! Almost there.
```

## Adding Your Own Questions

Add a new dictionary to the `questions` list in `quiz.py`:

```python
{"q": "Which is the largest ocean?", "answers": ["pacific", "pacific ocean"], "display": "Pacific Ocean"},
```

The total score updates automatically.

## Project Structure

```
.
├── quiz.py
└── README.md
```

## Author

Zaina
