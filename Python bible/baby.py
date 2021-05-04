# make baby ask a question
from random import choice

questions = [
    "Why is grass green?: ",
    "Why do birds fly?: ",
    "Why is the sky blue?: "
    ]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("OH, Okay")
