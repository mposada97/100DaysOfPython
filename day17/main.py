import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for a in data.question_data:
    question_bank.append(Question(a['text'], a['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You completed the quiz')
print(f'Your final score is {quiz.score}/{quiz.question_number}')