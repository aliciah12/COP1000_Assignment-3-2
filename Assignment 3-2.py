testScoreString = input("Enter the student's test score: ")
classRankString = input("Enter the student's class rank: ")
testScore = int(testScoreString)
classRank = int(classRankString)

while True: 
    testScoreString = input("Enter the student's test score: (1-87): ")
    testScore = int(testScoreString)
    if testScore >= 1 and testScore <= 87:
        break
    else:
        print("Invalid test score. Please try again.")

while True:
    classRankString = input("Enter the student's class rank: (1-60): ")
    classRank = int(classRankString)
    if classRank >= 1 and classRank <= 60:
        break
    else:
        print("Invalid class rank. Please try again.") 

print(f"Student's test score is: {testScore}")
print(f"Student's class rank is: {classRank}")
                            
