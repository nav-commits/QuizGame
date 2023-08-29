

# Quiz Game
def quiz_game():
    print("Welcome to my Quiz Game")

    # Game Rules
    playing_game= input("Do want to play this game? ")
    if playing_game != "yes":
        print("okay bye")
        quit()
    else:
     print("okay lets play this game")

    # Score 
    score = 0

    # Question 1
    question_One = input("What JS programming language stand for ? ")
    if question_One == "javascript":
        print("correct")
        score += 1
    else:
        print("wrong")
    
    # Question 2
    question_Two = input("What is the best programming language in 2023 ? ")
    if question_Two == "Javascript":
        print("correct")
        score += 1
    else:
        print("wrong")
    
    # Question 3
    question_Three = input("What programming language is used for web development ? ")
    if question_Three == "JavaScript":
        print("correct")
        score += 1
    else:
        print("wrong")

     # Question 4
    question_Four = input("What programming language is used for machine learning ? ")
    if question_Four == "python":
        print("correct")
        score += 1
    else:
        print("wrong")
    
    print("your score is " + str(score) + " out of 4 ") 
    
print(quiz_game()) 