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
