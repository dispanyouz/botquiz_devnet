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

  
