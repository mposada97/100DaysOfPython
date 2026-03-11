class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def next_question(self):
        question = self.question_list[self.question_number]
        ans = input(f'Q.{self.question_number + 1} {question.text} (True/False):').lower()
        self.question_number += 1
        self.check_answer(ans, question.answer)
    def still_has_questions(self):
        return len(self.question_list) > self.question_number
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('thats wrong')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is {self.score}/{self.question_number}\n')

    