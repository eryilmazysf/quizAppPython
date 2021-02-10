#question
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkAnswer(self,answer):
        return self.answer==answer



#quiz
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0


    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Soru {self.questionIndex+1}:{question.text}')

        for q in question.choices:
            print("-"+q)


        answer=input("answer:")
        self.guess(answer)
        self.loadQUestion()
        #print(question.checkAnswer(answer))


    def guess(self,answer):
        question=self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1

        self.questionIndex += 1

    def loadQUestion(self):
        self.displayProgress()
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()

    def showScore(self):
        return print("Your score:",self.score)

    def displayProgress(self):
        totalQUestion=len(self.questions)
        questionNumber=self.questionIndex

        if questionNumber>=totalQUestion:
            print("quiz is over".center(50,'*'))
        else:
            print(f'QUestion {questionNumber+1} of {totalQUestion}'.center(50,'*'))
q1=Question("best programing languages?",["C#","python","javascript","java"],"python")
q2=Question("most popular programing languages?",["python","javascript","C#","java"],"python")
q3=Question("easy learning programing languages?",["javascript","java","C#","python"],"python")
questions=[q1,q2,q3]

quiz=Quiz(questions)
question=quiz.getQuestion()
quiz.loadQUestion()