import random

# Data storage
users_data = {}  # Stores user details and profiles
questions_data = {
    "Python": [
        {"question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "7"], "answer": "8"},
        {"question": "Which data type is immutable?", "options": ["List", "Set", "Dictionary", "Tuple"], "answer": "Tuple"},
        {"question": "How do you create a function in Python?", "options": ["function()", "def()", "create()", "lambda()"], "answer": "def()"},
        {"question": "Which keyword is used for loops in Python?", "options": ["loop", "for", "iterate", "while"], "answer": "for"},
        {"question": "What is PEP 8?", "options": ["Python package", "Coding style guide", "IDE", "Framework"], "answer": "Coding style guide"}
    ],
    "DSA": [
        {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "answer": "O(log n)"},
        {"question": "Which data structure is FIFO?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue"},
        {"question": "What does DFS stand for?", "options": ["Depth First Search", "Data First Search", "Dynamic First Search", "Directed First Search"], "answer": "Depth First Search"},
        {"question": "What is a balanced binary tree?", "options": ["Tree with equal nodes", "Tree with balanced height", "Tree with all left children", "Tree with all right children"], "answer": "Tree with balanced height"},
        {"question": "Which sorting algorithm is fastest on average?", "options": ["Bubble Sort", "Merge Sort", "Quick Sort", "Selection Sort"], "answer": "Quick Sort"}
    ],
    "DBMS": [
        {"question": "What does DBMS stand for?", "options": ["Data Base Management System", "Database Management System", "Data Backup Management System", "Data Business Management System"], "answer": "Database Management System"},
        {"question": "Which SQL command is used to fetch data?", "options": ["FETCH", "SELECT", "GET", "DISPLAY"], "answer": "SELECT"},
        {"question": "What is a primary key?", "options": ["Unique identifier", "Any column", "Foreign key", "Redundant data"], "answer": "Unique identifier"},
        {"question": "What is normalization?", "options": ["Data structuring", "Data redundancy removal", "Data manipulation", "Data storage"], "answer": "Data redundancy removal"},
        {"question": "Which is a NoSQL database?", "options": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"], "answer": "MongoDB"}
    ]
}

def register():
    username = input("Enter a username: ")
    if username in users_data:
        print("Username already exists. Try logging in.")
        return
    password = input("Enter a password: ")
    users_data[username] = {"password": password, "profile": {"quizzes_taken": 0, "last_score": 0}}
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    if username not in users_data:
        print("Username not found. Please register first.")
        return None
    password = input("Enter your password: ")
    if users_data[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Incorrect password.")
        return None

def take_quiz(username):
    print("Welcome to the Quiz!")
    score = 0
    topics = ["Python", "DSA", "DBMS"]
    random.shuffle(topics)
    
    for topic in topics:
        print(f"Topic: {topic}")
        questions = random.sample(questions_data[topic], 5)
        for q in questions:
            print(f"\n{q['question']}")
            for i, option in enumerate(q["options"], start=1):
                print(f"{i}. {option}")
            answer = input("Enter the correct option number: ")
            if q["options"][int(answer) - 1] == q["answer"]:
                score += 1
                print("Correct!")
            else:
                print(f"Wrong! Correct answer is: {q['answer']}")
    
    users_data[username]["profile"]["quizzes_taken"] += 1
    users_data[username]["profile"]["last_score"] = score
    print(f"\nQuiz Completed! Your score is: {score}/15")

def view_profile(username):
    profile = users_data[username]["profile"]
    print("User Profile")
    print(f"Quizzes Taken: {profile['quizzes_taken']}")
    print(f"Last Score: {profile['last_score']}")

def main():
    while True:
        print("Welcome to the Quiz App!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                while True:
                    print("\n1. Take Quiz")
                    print("2. View Profile")
                    print("3. Logout")
                    sub_choice = input("Enter your choice: ")
                    
                    if sub_choice == "1":
                        take_quiz(username)
                    elif sub_choice == "2":
                        view_profile(username)
                    elif sub_choice == "3":
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main()
