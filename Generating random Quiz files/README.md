
# US State Capitals Quiz Generator
#### Creating a program that generates multiple unique quizzes for a class of students, with randomized questions and answers to prevent cheating.

----

## Quiz Creation:
### The program should be able to perform the following tasks:
  + **Generate 35 different quizzes for the students**
  + **Each quiz should contain 50 questions, with the states listed in random order**
  + **For each question, provide the correct answer and three incorrect (randomly chosen) answers in random order**

## Logic and Operations:
- **Write the quizzes to 35 separate text files, one for each student**
- **Store the US state-capital pairs in a dictionary**
- **Use the random.shuffle() method to randomize the order of states and the order of multiple-choice options**
- **Use file operations (open(), write(), and close()) to save the quizzes and answer keys into text files**
