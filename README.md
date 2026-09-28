\# AI Risk Assessment Tool



A simple Python command-line tool for the preliminary assessment of risks associated with an AI system.



\## Project Purpose



This project was developed as a practical exercise to apply basic Python programming concepts to a problem related to AI ethics and risk assessment.



\## How It Works



The tool collects information about an AI system through a series of questions.



It evaluates four basic risk dimensions:



\* \*\*Personal data\*\* — whether the system uses personal data.

\* \*\*Decision impact\*\* — whether the system makes decisions affecting people.

\* \*\*Explainability\*\* — whether the system's decisions can be explained.

\* \*\*Human oversight\*\* — whether human supervision is present.



Each risk factor contributes to an overall risk score.



The final score is classified as:



\* \*\*LOW\*\* — 0–1

\* \*\*MEDIUM\*\* — 2–3

\* \*\*HIGH\*\* — 4



\## Technologies



\* Python 3

\* Command-line interface

\* User input

\* Conditional statements

\* Variables

\* Basic arithmetic



\## How to Run



Clone the repository and run the program from the command line:



```bash

python main.py

```



The program will ask the user a series of questions and generate a preliminary AI risk assessment.

## Example Output

```text
========================================
AI RISK ASSESSMENT REPORT
========================================

System: Recruitment AI

Privacy risk: HIGH
Decision impact: HIGH
Explainability risk: HIGH
Human oversight risk: LOW

Risk score: 3/4
Overall risk: MEDIUM
```

## Current Version

**Version 1.0**

This first version focuses on fundamental Python programming concepts and a simple rule-based approach to AI risk assessment.

## Future Development

Possible future versions may introduce:

* Functions for a more modular code structure
* Input validation and error handling
* Lists and dictionaries for structured data
* JSON or CSV export
* A more detailed risk assessment framework



