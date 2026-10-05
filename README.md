AI Risk Assessment Tool

A simple Python command-line tool for the preliminary assessment of risks associated with an AI system.

Project Purpose

This project is a practical Python project developed around a real-world problem related to AI ethics, risk assessment and AI governance.

The goal is to build a simple rule-based tool capable of collecting information about an AI system, evaluating selected risk dimensions and producing an overall risk classification.

The project is also intended as a learning and portfolio project to demonstrate the application of basic Python programming concepts to an AI governance-related use case.

How It Works

The tool collects information about an AI system through a series of questions.

It evaluates four basic risk dimensions:

Personal data — whether the system uses personal data.

Decision impact — whether the system makes decisions affecting people.

Explainability — whether the system's decisions can be explained.

Human oversight — whether human supervision is present.

Each risk factor contributes to an overall risk score.

The final score is classified as:

LOW — 0–1

MEDIUM — 2–3

HIGH — 4

Current Features

The current version includes:

Interactive command-line input

Input validation for binary questions (0 / 1)

Error handling for invalid non-numeric input

Modular functions

Generic risk evaluation through a reusable valuta_rischio() function

Individual risk assessment

Overall risk score calculation

Final risk assessment report

Technologies

Python 3

Command-line interface

Functions

Variables

Conditional statements

while loops

try/except error handling

User input

Basic arithmetic

How to Run

Clone the repository and run the program from the command line:

python main.py

The program will ask the user a series of questions and generate a preliminary AI risk assessment.

Example Output

======================================
AI RISK ASSESSMENT
======================================
Sistema AI: Recruitment AI

PRIVACY RISK: HIGH RISK
DECISION IMPACT: HIGH RISK
EXPLAINABILITY RISK: HIGH RISK
HUMAN OVERSIGHT RISK: LOW RISK
Overall risk: MEDIUM
======================================

Project Structure

AI_Risk_Assessment/
│
├── main.py
├── README.md
└── .gitignore

Current Version

Version 3

The current version introduces improved input validation, error handling and a more modular approach to risk evaluation.

The risk assessment logic has also been refactored to reduce code duplication through the use of a reusable risk evaluation function.

Future Development

Possible future versions may introduce:

Additional AI risk dimensions

More structured risk categories

Lists and dictionaries for structured data

JSON or CSV export

Risk assessment reporting improvements

A more detailed AI risk and governance framework

Alignment with relevant AI governance and regulatory concepts

Disclaimer

This tool is a preliminary educational and portfolio project. It does not constitute a legal, regulatory or professional AI risk assessment and should not be used as a substitute for a formal compliance or risk management process.