# #26 was a solution video to Ex-:2 
# This Video is Ex-:3 Named as Kaun Banega Crorepati

# Create a program capable of displaying Questions to the user like KBC.
# Use list data type to store the questions and their correct answers
# Display the total amount user is taking home after playing the game

# This Was Attempted by me


# THis Done by Harry 

questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

# yaha tak 2 list banai harry ne ek question aur dursi list levels

money = 0
for i in range(0, len(questions)):
      question = questions[i]
      print(f"\n\nQuestion for Rs. {levels[i]}")
      print(f"{question[0]}")                            # THIS LINE WAS ADDED MY ME
      print(f"a. {question[1]}          b. {question[2]} ")
      print(f"c. {question[3]}          d. {question[4]} ")
      rep = (input("Enter your answer (a-d) or  0 to quit:\n" ))
      if (rep == 0):
            money = levels[i-1]
            break
      if(rep ==question[4]):
            print(f"Correct answer, you have won Rs. {levels[i]}")
      if(i == 4):
            money = 10000
      elif(i == 9):
            money = 320000
      elif(i == 14):
            money = 10000000
      else:
            print("Wrong answer!")
            break 

print(f"Your take home money is {money}")

# Ismei Agar hum aage ke questions Change karenge to kyya hoga kal dekhte hai