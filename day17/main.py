from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    q_text = i["text"]
    q_answer = i["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

# 创建 question_bank 的目的是将从 question_data 提取的数据转换为 Question 类的对象
# question_bank里的数据类型大概如下，列表里每一条都是'Question'类的（object）对象
# question_bank = [
#     Question(text="Question 1 text", answer="True"),
#     Question(text="Question 2 text", answer="False"),
#     # ...
# ]

quiz = QuizBrain(question_bank)

while quiz.if_still_question():
    quiz.next_question()
