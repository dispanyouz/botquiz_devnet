import json
import click
import getpass


class Quiz:
    #Chaikenov Adilet
    def __init__(self, questions):
        """Initialize the Quiz object with a list of questions."""
        self.questions = questions
        self.score = 0
        self.wrong_answers = []

    def display_question(self):
        """Display each question and prompt the user for an answer."""
        for question in self.questions:
            print(question['question'])
            options = question['options']
            for i, option in enumerate(options):
                print(f"{i+1}. {option}")
            while True:
                user_input = input("Enter your answer (1-4 or option text): ")
                if user_input.isdigit():
                    user_input = int(user_input)
                    if 1 <= user_input <= len(options):
                        user_answer = options[user_input - 1]
                        break
                    else:
                        print(f"Invalid option! Please enter a number between 1 and {len(options)}.")
                else:
                    if user_input.lower() in [option.lower() for option in options]:
                        user_answer = user_input
                        break
                    else:
                        print("Invalid option! Please enter one of the provided options.")

            self.check_answer(question['question'], question['answer'], user_answer)


    #Yeltayev Magzhan
    def check_answer(self, question_text, correct_answer, user_answer):
        """Check if the user's answer is correct and update the score."""
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect! The correct answer is:", correct_answer)
            self.wrong_answers.append({
                "question": question_text,
                "correct_answer": correct_answer,
                "user_answer": user_answer
            })
            
    #Kurmanbek Temirlan
    def display_score(self):
        """Display the user's score and any wrong answers."""
        print("Your score is: {}/{}".format(self.score, len(self.questions)))
        if self.wrong_answers:
            print("\nYou got the following questions wrong:")
            for index, wrong_answer in enumerate(self.wrong_answers, start=1):
                print(f"\n{index}. Question: {wrong_answer['question']}")
                print(f"   Your Answer: {wrong_answer['user_answer']}")
                print(f"   Correct Answer: {wrong_answer['correct_answer']}")

#Yeltayev Magzhan
# Load questions from JSON file based on the selected category
def load_questions_from_json(filename):
    """Load questions from a JSON file."""
    try:
        with open(filename, 'r') as file:
            all_questions = json.load(file)
    except FileNotFoundError:
        all_questions = {}
    return all_questions


# Save questions to JSON file
def save_questions_to_json(filename, all_questions):
    """Save questions to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(all_questions, file, indent=4)


#Batyrkhan Bekzatkhan
# Add a new question
def add_question(filename):
    while True:
        category = input("Choose a category to add a question (Sport/Science/History): ").lower()
        if category in ['sport', 'science', 'history']:
            break
        else:
            print("Invalid category! Please choose either 'Sport', 'Science', or 'History'.")

    while True:  # Цикл для повторного запроса ввода вопроса после ошибки
        question = input("Enter the new question: ")
        answer = input("Enter the answer to the new question: ")

        options = []
        for i in range(4):
            option = input(f"Enter option {i+1}: ")
            options.append(option)

        # Добавим проверку наличия правильного ответа в списке опций
        if answer in options:
            break
        else:
            print("The correct answer is not in the options. Please make sure to include it in the options.")

    # Преобразуем категорию в нижний регистр
    category = category.lower()

    all_questions = load_questions_from_json(filename)
    if category not in all_questions:
        all_questions[category] = []

    all_questions[category].append({
        "question": question,
        "answer": answer,
        "options": options
    })

    save_questions_to_json(filename, all_questions)
    print("Question added successfully!")
#Yeltayev Magzhan
# Authenticate administrator
def authenticate_admin():
    """Authenticate the administrator."""
    while True:
        password = getpass.getpass("Enter the password: ")
        if password != "cisco":
            click.echo("Incorrect password! Access denied.")
        else:
            return True

#Kurmanbek Temirlan
# Main function
@click.command()
def main():
    filename = "questions.json"  # JSON file name with questions

    while True:
        user_type = click.prompt("Are you an administrator or a participant? (admin/participant)", type=str)

        if user_type.lower() == "admin":
            if authenticate_admin():
                add_question(filename)
        elif user_type.lower() == "participant":
            while True:
                category = click.prompt("Choose a category (Sport/Science/History)", type=str)
                questions = load_questions_from_json(filename).get(category, [])
                if not questions:
                    click.echo("No questions available for the selected category.")
                    play_again = click.prompt("Do you want to select another category? (yes/no)", type=str)
                    if play_again.lower() == "no":
                        break
                    else:
                        continue
                else:
                    quiz = Quiz(questions)
                    quiz.display_question()
                    quiz.display_score()

                    play_again = click.prompt("Do you want to play again? (yes/no)", type=str)
                    if play_again.lower() != "yes":
                        break
        else:
            click.echo("Invalid user type! Please choose either 'admin' or 'participant'.")

        play_again = click.prompt("Do you want to continue? (yes/no)", type=str)
        if play_again.lower() != "yes":
            break


if __name__ == "__main__":
    main()