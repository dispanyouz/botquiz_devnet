# Add a new question
def add_question(filename):
    """Add a new question to the JSON file."""
    category = click.prompt("Choose a category to add a question (Sport/Science/History)", type=str)
    question = click.prompt("Enter the new question", type=str)
    answer = click.prompt("Enter the answer to the new question", type=str)

    options = []
    for i in range(4):
        option = click.prompt(f"Enter option {i+1}", type=str)
        options.append(option)

    all_questions = load_questions_from_json(filename)
    if category not in all_questions:
        all_questions[category] = []

    all_questions[category].append({
        "question": question,
        "answer": answer,
        "options": options
    })

    save_questions_to_json(filename, all_questions)
    click.echo("Question added successfully!")

