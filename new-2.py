
quiz = {
      "question1" : 
        {"question" : "What is the captial of France?", "answer" : "Paris"},
      "question2" :
        {"question" : "What is the captial of Germany?", "answer" : "Berlin"},

      "question3" : 
        {"question" : "What is the captial of Italy?", "answer" : "Rome"},
  "question4" : 
  {"question" : "What is the captial of Spain?", "answer" : "Madrid"},   "question5" : 
  {"question" : "What is the captial of Portugal?", "answer" : "Lisbon"},   "question6" : 
  {"question" : "What is the captial of Switzerland?", "answer" : "Bern"},   "question7" : 
  {"question" : "What is the captial of Austria?", "answer" : "Vienna"}}

score = 0

for key, value in quiz.items():
  print(value["question"])
  answer = input("Answer? ")


  if answer.lower() == value["answer"].lower():
    print("Correct!")
    score = score + 1
    print("Your score is: "+ str(score))
    print("")
    print("")

  else:
    print("Wrong!")
    print("The correct answer is " + value["answer"])
    print("Your score is: " + str(score))
    print("")
    print("")

  print("Your final score is: " + str(score) + " out of 7")
  print("Your prercentage is " + str(int(score/7) * 100)+ "%")
  
  

