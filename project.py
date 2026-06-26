import json
import random
import os

# --- UPGRADE FEATURE: Question bank stored in a JSON format (dictionary) ---
QUESTION_BANK = {
    "math": {
        "easy": [
            {"question": "What is 5 + 7?", "answer": "12"},
            {"question": "What is 12 - 4?", "answer": "8"}
        ],
        "medium": [
            {"question": "What is 12 * 6?", "answer": "72"},
            {"question": "What is 144 / 12?", "answer": "12"}
        ],
        "hard": [
            {"question": "What is the square root of 225?", "answer": "15"},
            {"question": "Solve for x: 2x + 5 = 15", "answer": "5"}
        ]
    },
    "science": {
        "easy": [
            {"question": "What planet is known as the Red Planet?", "answer": "mars"},
            {"question": "What state of matter is water ice?", "answer": "solid"}
        ],
        "medium": [
            {"question": "What is the chemical symbol for Water?", "answer": "h2o"},
            {"question": "How many planets are in our solar system?", "answer": "8"}
        ],
        "hard": [
            {"question": "What is the powerhouse of the cell?", "answer": "mitochondria"},
            {"question": "What is the closest star to Earth?", "answer": "sun"}
        ]
    }
}

# --- FORMULA DATABASE ---
FORMULAS = {
    "algebra": {
        "name": "Slope Formula",
        "formula": "m = (y2 - y1) / (x2 - x1)",
        "explanation": "Calculates the steepness of a line between two points.",
        "variables": ["y2", "y1", "x2", "x1"]
    },
    "physics": {
        "name": "Force (Newton's Second Law)",
        "formula": "F = m * a",
        "explanation": "Force equals mass multiplied by acceleration.",
        "variables": ["mass", "acceleration"]
    }
}

# --- INPUT VALIDATION HELPER ---
def get_valid_input(prompt, valid_options):
    """UPGRADE FEATURE: Input validation to prevent crashes and invalid choices."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

# --- CORE FEATURE 1: QUIZ GENERATOR ---
def run_quiz():
    print("\n--- Welcome to the Quiz Generator ---")
    
    # Select Topic
    topic = get_valid_input("Choose a topic (math / science): ", ["math", "science"])
    
    # Select Difficulty
    difficulty = get_valid_input("Choose difficulty (easy / medium / hard): ", ["easy", "medium", "hard"])
    
    # Fetch and shuffle questions (UPGRADE FEATURE: Randomized quizzes)
    questions = QUESTION_BANK[topic][difficulty].copy()
    random.shuffle(questions)
    
    score = 0
    total_questions = len(questions)
    
    print(f"\nStarting your {difficulty} {topic} quiz! ({total_questions} questions)")
    print("-" * 40)
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        user_ans = input("Your answer: ").strip().lower()
        
        # Core: Instant feedback
        if user_ans == q['answer'].lower():
            print("✨ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was: {q['answer']}")
            
    # Core: Score tracking
    print("-" * 40)
    print(f"Quiz Complete! Your Score: {score}/{total_questions}")
    
    # UPGRADE FEATURE: Save scores to a file
    save_score = get_valid_input("Would you like to save your score? (yes / no): ", ["yes", "no"])
    if save_score == "yes":
        name = input("Enter your name for the leaderboard: ").strip()
        try:
            with open("scores.txt", "a") as file:
                file.write(f"Name: {name} | Topic: {topic} | Difficulty: {difficulty} | Score: {score}/{total_questions}\n")
            print("Score saved successfully to 'scores.txt'!")
        except Exception as e:
            print(f"Error saving score: {e}")

# --- CORE FEATURE 2: FORMULA HELPER ---
def run_formula_helper():
    print("\n--- Welcome to the Formula Helper ---")
    print("Available topics:")
    for topic in FORMULAS.keys():
        print(f"- {topic.capitalize()}")
        
    choice = get_valid_input("\nSelect a topic: ", list(FORMULAS.keys()))
    formula_data = FORMULAS[choice]
    
    # Show formula + explanation
    print(f"\n--- {formula_data['name']} ---")
    print(f"Formula:      {formula_data['formula']}")
    print(f"Explanation:  {formula_data['explanation']}")
    
    # Optional / Upgrade: Plug-in values to get solved answer
    calc_choice = get_valid_input("\nWould you like to solve this formula with your own numbers? (yes / no): ", ["yes", "no"])
    
    if calc_choice == "yes":
        print("\nEnter the values requested:")
        try:
            if choice == "algebra":
                y2 = float(input("Enter y2: "))
                y1 = float(input("Enter y1: "))
                x2 = float(input("Enter x2: "))
                x1 = float(input("Enter x1: "))
                
                if x2 - x1 == 0:
                    print("Error: Division by zero! Slope is undefined.")
                else:
                    result = (y2 - y1) / (x2 - x1)
                    print(f"\nCalculated Slope (m) = {result}")
                    
            elif choice == "physics":
                m = float(input("Enter mass (kg): "))
                a = float(input("Enter acceleration (m/s^2): "))
                result = m * a
                print(f"\nCalculated Force (F) = {result} N")
                
        except ValueError:
            print("⚠️ Error: Please enter valid numbers only.")

# --- UPGRADE FEATURE: MENU SYSTEM ---
def main():
    while True:
        print("\n" + "="*40)
        print("     QUIZ GENERATOR & FORMULA HELPER     ")
        print("="*40)
        print("1. Quiz Generator")
        print("2. Formula Helper")
        print("3. Exit")
        print("-" * 40)
        
        choice = get_valid_input("Please choose an option (1 / 2 / 3): ", ["1", "2", "3"])
        
        if choice == "1":
            run_quiz()
        elif choice == "2":
            run_formula_helper()
        elif choice == "3":
            print("\nThank you for using the tool! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()