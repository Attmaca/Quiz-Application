📘 Online Quiz Application

A console-based quiz system built using Python and Object Oriented Programming (OOP) principles.
The application loads questions from a JSON file, allows users to take a multiple-choice quiz, evaluates their answers, and stores all results in a dynamic leaderboard.

🚀 Features

✔ Object-Oriented design (User, Quiz, Question classes)

✔ Loads questions from a JSON file

✔ Shuffles questions each game

✔ Automatic scoring system

✔ Input validation using try/except

✔ Shows correct answer when user is wrong

✔ Leaderboard stored as class-level data

✔ Interactive menu with Start / Leaderboard / Exit options


🧠 How It Works
1) Questions Loaded from JSON

The file questions.json contains all quiz questions:

{
  "text": "What is the capital of France?",
  
  "options": ["London", "Berlin", "Paris", "Rome"],
  
  "correct": 2
}

3) User Starts the Quiz

	•	User enters their name
	•	Quiz questions are shuffled
	•	Answers are validated
	•	Score is calculated
	•	Score is added to leaderboard

5) Leaderboard

Displays all users sorted by score (highest → lowest).

Example output:

===== Leaderboard =====
1. Ahmet: 7 points
2. Beyza: 6 points
=======================

🏗️ Class Overview

🔹 Question Class

Represents a single quiz question.

Attributes:
	•	question
	•	options
	•	correct_answer

Methods:
	•	is_correct(answer)

  🔹 Quiz Class

Handles the quiz session.

Responsibilities:
	•	Shuffling the questions
	•	Displaying question text and options
	•	Validating user input
	•	Tracking user score
	•	Showing the final result

⸻

🔹 User Class

Represents the quiz player.

Responsibilities:
	•	Storing username
	•	Starting the quiz
	•	Updating the leaderboard

The leaderboard is a class variable, meaning it belongs to all users.

📸 Example Program Output

========== General Knowledge Quiz ==========

Question 1: Which planet is known as the Red Planet?
1) Venus
2) Mars
3) Jupiter
4) Saturn
Enter your answer: 1
Wrong...
Correct answer: Mars

👥 Group Members (Control-Z)

Beyza Nur Çelik
20232831
Ahmet Atmaca
20230526


📄 Course Information
Course: AII108 Object Oriented Programming
Instructor: AMR ABDELBARI
Date: 05.12.2025

🏁 Conclusion
This project demonstrates the practical application of Object-Oriented Programming in Python.
By designing multiple classes, handling user input, and structuring external data with JSON,
we created a fully functional quiz system with a leaderboard.

