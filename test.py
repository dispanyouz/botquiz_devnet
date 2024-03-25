import unittest
from unittest.mock import patch
from script import Quiz, load_questions_from_json

class TestQuiz(unittest.TestCase):
    def test_check_answer(self):
        # На входе мы получаем список вопросов из категории "history" загруженных из JSON файла с помощью функции load_questions_from_json
        questions = load_questions_from_json("questions.json").get("history", [])
        # Экземпляр класса Quiz который создается с полученным списком вопросов
        quiz = Quiz(questions)
        user_answer = "Paris"
        quiz.check_answer("What is the capital of France?", "Paris", user_answer)
        self.assertEqual(quiz.score, 1)
        # На выходе мы ожидаем что счет викторины quiz.score(переменная которая обьявлена в функции check_answer) увеличиться на 1 в случае
        # если ответ пользователя user_answer совпадает с правильным ответом на вопрос
if __name__ == "__main__":
    unittest.main()
