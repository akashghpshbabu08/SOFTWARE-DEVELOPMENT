print("Welcome to the quiz game!")
print("NOTE: If your spelling is incorrect, it will be considered as a wrong answer.")

# Quiz Game in Python

# Define a dictionary of questions and answers
questions = {
    "1.What Indian city is the capital of two states?": "Chandigarh",
    "2.What is the largest planet in our solar system?": "Jupiter",
    "3.What is the smallest country in the world?": "Vatican City",
    "4.Which city is the capital of India?": "New Delhi",
    "5.What is the highest mountain peak in the world?": "Mount Everest",
    "6.Where is Taj Mahal Located?":"Agra",
    "7.What is GPU":"Graphics processing unit"
}

# Initialize score to 0
score = 0

# Loop through each question
for question, answer in questions.items():
    # Print the question
    print(question)
    # Get the user's response
    user_answer = input("Enter your answer: ")
    # Check if the user's response is correct
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Sorry, the correct answer is {answer}.")

# Print the final score
print(f"Your final score is {score} out of {len(questions)}")
