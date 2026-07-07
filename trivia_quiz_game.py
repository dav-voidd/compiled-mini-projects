#Trivia Quiz

q_and_a = {}
score = 0

def add_qna():
    user_question = input("Whats the question: ")
    user_answer = input("Whats the answer: ")
    q_and_a[user_question] = user_answer

def answer_questions():
    global score
    number = 0
    for key in q_and_a:
        number += 1
        print(f"{number}. {key}")
        user_answer = input(f"Whats the answer for number {number}? : ")
        if user_answer == q_and_a[key]:
            score += 1
            print("Correct!")
        elif user_answer not in q_and_a.values():
            print("Incorrect")



while True:
    user_choice = input("Do you want to add question (y/n): ").lower()
    if user_choice == 'y':
        add_qna()
    elif user_choice == 'n':
        user_choice1 = input("Do you want to answer the questions or see the score and quit? (y/s): ").lower()
        if user_choice1 == 'y':
            answer_questions()
        elif user_choice1 == 's':
            print(f"You score is: {score}. You have exited the game.")
            break








