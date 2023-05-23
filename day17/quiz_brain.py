class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def if_still_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False): \n ")
        # 这里的.test是question_model里的方法
        self.check_answer(user_answer, current_question.answer)
        # 这里的.test是question_model里的方法,因为current_question是Question类的对象

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("you are right!")
        else:
            print("you are wrong.")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
