import unittest
from unittest.mock import patch
from script import Quiz, load_questions_from_json, add_question, authenticate_admin


class TestQuiz(unittest.TestCase):

    def test_load_questions_from_json(self):
        # Проверяем, что функция загружает вопросы из JSON файла корректно
        loaded_questions = load_questions_from_json("questions.json")
        self.assertTrue(loaded_questions)  # Проверяем, что вопросы успешно загружены

    def test_quiz_score(self):
        # Загружаем вопросы из файла
        questions = load_questions_from_json("questions.json").get("history", [])
        # Создаем экземпляр викторины и предполагаемый ответ
        quiz = Quiz(questions)
        user_answer = "Paris"
        # Проверяем, что при правильном ответе счет увеличивается на 1
        quiz.check_answer("What is the capital of France?", "Paris", user_answer)
        self.assertEqual(quiz.score, 1)

    def test_add_question(self):
    # Prepare the mock inputs
        mock_inputs = ["History", "Test question", "Test answer", "Test answer", "Option 1", "Option 2", "Option 3", "Option 4"]
    # Patch the builtins.input function with a MagicMock object
        with patch('builtins.input', side_effect=mock_inputs):
        # Call the function being tested
            add_question("questions.json")
    # Load the questions from the JSON file
        loaded_questions = load_questions_from_json("questions.json")
    # Assert that the question was added correctly
        self.assertTrue(loaded_questions.get("history"))  # Check if the category with questions was created
        self.assertEqual(loaded_questions["history"][-1]["question"], "Test question")


    def test_authenticate_admin(self):
        # Подменяем ввод пароля для тестирования функции authenticate_admin
        with patch('getpass.getpass', return_value="cisco"):
            self.assertTrue(authenticate_admin())


if __name__ == "__main__":
    unittest.main()