import click
def display_score(self):
    """Display the user's score and any wrong answers."""
    print("Your score is: {}/{}".format(self.score, len(self.questions)))
    if self.wrong_answers:
        print("\nYou got the following questions wrong:")
        for index, wrong_answer in enumerate(self.wrong_answers, start=1):
            print(f"\n{index}. Question: {wrong_answer['question']}")
            print(f"   Your Answer: {wrong_answer['user_answer']}")
            print(f"   Correct Answer: {wrong_answer['correct_answer']}")


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
