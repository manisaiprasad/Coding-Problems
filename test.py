class Question:
    def __init__(self, questionId, markedOption, score, status="Not Answered"):
        self.questionId = questionId
        self.markedOption = markedOption
        self.score = score
        self.status = status

class Student:
    def __init__(self, registedId, questionsAttempted):
        self.registedId = registedId
        self.questionsAttempted = questionsAttempted

    def evaluateQuestions(self, answerKey, questionsAttemptedlist):
        for key, value in answerKey:
            for i in range(len(questionsAttemptedlist)):
                if questionsAttemptedlist[i].questionId == key:
                    if questionsAttemptedlist[i].markedOption == value:
                        questionsAttemptedlist[i].status = "correct"
                    else:
                        questionsAttemptedlist[i].status = "incorrect"

    def findGrade(self, questionsAttemptedlist):
        totalScore = 0
        for i in range(len(questionsAttemptedlist)):
            if questionsAttemptedlist[i].status == "correct":
                totalScore += questionsAttemptedlist[i].score
        if totalScore >= 80:
            return "A"
        elif totalScore >= 70 and totalScore < 80:
            return "B"
        elif totalScore >= 60 and totalScore < 70:
            return "C"
        else:
            return "F"


noOfQuestions = int(input())
questionsAttemptedlist = []
for i in range(noOfQuestions):
    questionId = input()
    markedOption = input()
    score = int(input())
    questionsAttemptedlist.append(
        Question(questionId, markedOption, markedOption))

countAnswerKey = int(input())
answerKey = {}
for i in range(countAnswerKey):
    questionId = input()
    answer = input()
    answerKey[questionId] = answer

studentObj = Student.evaluateQuestions(answerKey, questionsAttemptedlist)

for i in range(len(questionsAttemptedlist)):
    print(questionsAttemptedlist[i].questionId +
          " " + questionsAttemptedlist[i].status)

print(studentObj.findGrade(questionsAttemptedlist))
