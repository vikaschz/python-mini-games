quiz = [
    {
        "question": "What is the national animal of India?",
        "options": ["A. Lion", "B. Elephant", "C. Tiger", "D. Peacock"],
        "answer": "C",
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": [
            "A. Charles Babbage",
            "B. Alan Turing",
            "C. Tim Berners-Lee",
            "D. Bill Gates",
        ],
        "answer": "A",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C",
    },
    {
        "question": "What is the hardest natural substance?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Quartz"],
        "answer": "C",
    },
    {
        "question": "Which blood group is known as the universal donor?",
        "options": ["A. AB+", "B. O+", "C. O-", "D. AB-"],
        "answer": "C",
    },
    {
        "question": "Which language has the most native speakers?",
        "options": ["A. English", "B. Spanish", "C. Mandarin", "D. Hindi"],
        "answer": "C",
    },
    {
        "question": "What is the process of cell division in humans called?",
        "options": ["A. Mitosis", "B. Meiosis", "C. Binary Fission", "D. Budding"],
        "answer": "A",
    },
    {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["A. England", "B. France", "C. Germany", "D. Spain"],
        "answer": "B",
    },
    {
        "question": "Which is the tallest mountain in the world?",
        "options": ["A. K2", "B. Mount Everest", "C. Kangchenjunga", "D. Lhotse"],
        "answer": "B",
    },
    {
        "question": "Which festival is known as the Festival of Lights?",
        "options": ["A. Holi", "B. Eid", "C. Christmas", "D. Diwali"],
        "answer": "D",
    },
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C",
    },
    {
        "question": "Who wrote the Indian National Anthem?",
        "options": [
            "A. Mahatma Gandhi",
            "B. Rabindranath Tagore",
            "C. Bankim Chandra Chatterjee",
            "D. Subhash Chandra Bose",
        ],
        "answer": "B",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": [
            "A. Oxygen",
            "B. Nitrogen",
            "C. Carbon Dioxide",
            "D. Hydrogen",
        ],
        "answer": "C",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": [
            "A. Elephant",
            "B. Blue Whale",
            "C. Giraffe",
            "D. Hippopotamus",
        ],
        "answer": "B",
    },
    {
        "question": "Which organ purifies blood in the human body?",
        "options": ["A. Heart", "B. Liver", "C. Kidney", "D. Lungs"],
        "answer": "C",
    },
    {
        "question": "How many bytes make one kilobyte (KB)?",
        "options": ["A. 100", "B. 512", "C. 1000", "D. 1024"],
        "answer": "D",
    },
    {
        "question": "Which ocean is the largest in the world?",
        "options": [
            "A. Atlantic Ocean",
            "B. Indian Ocean",
            "C. Arctic Ocean",
            "D. Pacific Ocean",
        ],
        "answer": "D",
    },
    {
        "question": "Which metal is liquid at room temperature?",
        "options": ["A. Iron", "B. Mercury", "C. Aluminium", "D. Lead"],
        "answer": "B",
    },
    {
        "question": "Who invented the telephone?",
        "options": [
            "A. Thomas Edison",
            "B. Alexander Graham Bell",
            "C. Nikola Tesla",
            "D. Guglielmo Marconi",
        ],
        "answer": "B",
    },
]

# Initialize score
score = 0

# Ask questions
for i, item in enumerate(quiz, start=1):
    print(f"\nQuestion {i}: {item['question']}")
    for option in item["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D) (Enter Q to exit): ").strip().upper()

    if user_answer == "Q":
        break
    elif user_answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {item['answer']}")

# Final score
print(f"\nYour final score is: {score} out of {len(quiz)}")
