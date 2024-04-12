import random
class Question:
    def __init__(self, question, option1, option2, option3, option4, answer):
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.answer = answer

class KBCGame:
    def __init__(self, questions, name, age):
        self.questions = questions
        self.current_question = 0
        self.amount_won = 0
        self.current_level = 15
        self.name = name
        self.age = age


    def play(self):
        self.current_question = 0
        a = random.randint(0, self.current_level)
        b = []
        try:
            while True and len(b) != self.current_level: 
                if a not in b :
                    b.append(a)
                else:
                    a = random.randint(0, self.current_level)
                    continue
                question = self.questions[a]
                print(f"Question {self.current_question+1}: {question.question}")
                options = [question.option1, question.option2, question.option3, question.option4]
                for i, option in enumerate(options):
                    print(f"{i+1}. {option}")
                answer = int(input("Enter your answer (1-4): "))
                if answer < 1 or answer > 4:
                    raise ValueError("Invalid answer. Please enter a number between 1 and 4.")
                if question.answer == answer and  len(b) == 1:
                    self.amount_won += 1000
                    print(f"Correct answer! You have won Rs. {self.amount_won}.")
                elif question.answer == answer:
                    self.amount_won *= 2
                    print(f"Correct answer! You have won Rs. {self.amount_won}.")
                else:
                    print("Incorrect answer. Game over.")
                    print(f"Congratulations! {self.name} have won Rs. {self.amount_won}.")
                    break
                self.current_question += 1
                if self.current_question == self.current_level:
                    print(f"Congratulations! {self.name} you have won Rs. {self.amount_won}.")
                    break
        except ValueError as e:
            print(e)
            self.play()


