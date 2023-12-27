import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_number):
        question = self.questions[question_number]['question']
        options = self.questions[question_number]['options']

        print(f"\nQuestion {question_number + 1}: {question}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    def get_user_answer(self):
        while True:
            try:
                user_input = int(input("\nEnter the number of your answer: "))
                if 1 <= user_input <= len(self.questions[0]['options']):
                    return user_input
                else:
                    print("Invalid input. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def evaluate_answer(self, question_number, user_answer):
        correct_answer = self.questions[question_number]['correct']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")

    def run_quiz(self):
        for i in range(len(self.questions)):
            self.display_question(i)
            user_answer = self.get_user_answer()
            self.evaluate_answer(i, user_answer)

        print("\nQuiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")


# Customize your quiz by modifying questions, options, and correct answers
questions_data = [
    {
        'question': "What is the capital of France?",
        'options': ["Berlin", "Madrid", "Paris", "Rome"],
        'correct': 3,
    },
    {
        'question': "Which programming language is known for its readability and simplicity?",
        'options': ["Java", "C++", "Python", "JavaScript"],
        'correct': 3,
    },
    {
        'question': "What is the largest planet in our solar system?",
        'options': ["Mars", "Jupiter", "Earth", "Venus"],
        'correct': 2,
    },
]

# Shuffle questions to make the quiz more interesting
random.shuffle(questions_data)

# Create and run the quiz
quiz = QuizGame(questions_data)
quiz.run_quiz()
