
import json
import random

class User():
    # A class with user name, quiz start, and leaderboard functions.
    leaderboard = []

    def __init__(self,name):
        self.name = name

    def start_quiz(self,quiz):
        print("==="*30)
        print("==="*10,"Welcome To General Knowledge Quiz","==="*10) 
        print("==="*30)
        score = quiz.start()
        User.leaderboard.append((self.name,score))

    @classmethod
    def history (a):
        print("===" * 10, "Leaderboard", "===" * 10)
        print("")
        if not a.leaderboard:
            print("No players yet. Be the first to take the quiz!")
            print("")
            print("==="*24)
            return

        sort = sorted(a.leaderboard,key = lambda x :x[1] , reverse=True )
        for rank , (name,score) in enumerate(sort,start = 1):
            print(f"{rank}. {name}: {score} points.")

        print("==="*24)
        

class Question():
    # question class, you can define the questions yourself if you wish. But ı would like to read with json file.
    
    def __init__(self,question,options,correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self,answer):
        return answer == self.correct_answer
    
def json_question(file_path):
    #Function that reads predefined questions in JSON format
    questions = []
    with open(file_path, "r", encoding="utf-8" ) as file:
        question_list = json.load(file)
        for item in question_list:
            q = Question(
                question=item["text"],
                options=item["options"],
                correct_answer= item["correct"]
            )
            questions.append(q)
    return questions
     
class Quiz():
# shuffles the questions, lists them, and checks the user's answers.
    def __init__(self,questions):
        self.questions = questions

    def start(self):
        random.shuffle(self.questions)
        score = 0
        
        for i,q in enumerate(self.questions, start=1):
            print(f"Question {i}: {q.question}")

            for index, options in enumerate(q.options,start=1):
                print(f"{index}) {options}")
            while True:
                try:
                    answer= int(input("Enter your answer: ")) -1 
                    if answer <0 or answer > 4:
                        print("Please enter a valid option")
                        continue
                    break
                except ValueError:
                    print("Please enter a number.")

            if q.is_correct(answer):
                        print("Correct!")
                        score += 1
            else:
                print("Wrong...")
                correct_option = q.options[q.correct_answer]
                print(f"the correct option was: {correct_option}")

        self.result(score)
        return score
        
    def result(self,score):
        print("==="*10, "Quiz Finished","==="*10)
        print(f"Your score: {score}/{len(self.questions)}")



def main():
    # menu that runs the program
    questions = json_question("questions.json")
    quiz = Quiz(questions)

    while True:
        print("                                     ")
        print("==="*10,"The Menu","==="*10)
        print("1) Start Quiz")
        print("2) Show Leaderboard") 
        print("3) Exit")

        try:
            choice = int(input("Select an option (1-3): "))
        except ValueError:
            print("Please enter a valid option")
            continue
            
        if choice == 1:
            name = input("Enter your name: ")
            user = User(name)
            user.start_quiz(quiz)

        elif choice == 2:
            User.history()
        elif choice == 3:
                print("Exiting... GodBye!")
                break
        else:
            print("İnvalid choice, please try again")

main()