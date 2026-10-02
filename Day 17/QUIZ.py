print("===== PYTHON QUIZ =====")

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "What is the output of 10 + 5?",
        "options": ["A. 15", "B. 50", "C. 105", "D. 5"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
        "answer": "C"
    },
    {
        "question": "Which collection is mutable in Python?",
        "options": ["A. Tuple", "B. List", "C. String", "D. Integer"],
        "answer": "B"
    }
]

score = 0

# Loop through all questions
for i, q in enumerate(questions, start=1):
    print(f"\n{i}. {q['question']}")

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer: ").upper()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", q["answer"])

# Final result
print("\n===== QUIZ RESULT =====")
print("Your score:", score, "/ 5")

if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")