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


# Authenticate administrator
def authenticate_admin():
    """Authenticate the administrator."""
    while True:
        password = getpass.getpass("Enter the password: ")
        if password != "cisco":
            click.echo("Incorrect password! Access denied.")
        else:
            return True
