# AI Risk Assessment Tool

A Python-based educational and portfolio project exploring the intersection of AI risk assessment, ethics and governance.

## Professional Context

This project represents a practical step in my transition from an academic background in philosophy and ethics towards AI governance, AI risk management and responsible AI.

My background combines advanced academic training in philosophy and political philosophy with professional experience in education and an ongoing specialization in Artificial Intelligence.

The project reflects an interdisciplinary approach: applying basic programming skills to questions concerning AI ethics, risk management, human oversight, explainability and responsible use of AI systems.

Particular attention is given to the European regulatory framework for Artificial Intelligence, including the risk-based approach of the EU AI Act, as well as to AI management systems and standards such as ISO/IEC 42001.

The objective is not to build a technically sophisticated AI system, but to demonstrate the ability to connect technical implementation with ethical, regulatory and governance requirements.

## Project Purpose

The goal of this project is to build a simple rule-based tool capable of collecting information about an AI system, evaluating selected risk dimensions and producing an overall risk classification.

The project is also intended as a learning and portfolio project to demonstrate the application of basic Python programming concepts to an AI governance-related use case.

The current assessment considers four dimensions:

- Personal data
- Decision impact
- Explainability
- Human oversight

These dimensions are not intended to reproduce or determine the legal classification of an AI system under the EU AI Act. Rather, they provide a simplified educational framework for exploring how AI-related risks can be translated into operational assessment criteria.

## AI Governance Perspective

The project is informed by several areas of AI governance:

- AI ethics and responsible AI
- Risk identification and assessment
- Human oversight
- Transparency and explainability
- Privacy and personal data
- Regulatory compliance
- The risk-based approach of the EU AI Act
- AI management systems and ISO/IEC 42001

The EU AI Act establishes a risk-based regulatory framework for AI and introduces different obligations according to the level and nature of risk associated with AI systems.

ISO/IEC 42001 provides a management-system framework for organizations that develop, provide or use AI systems, supporting the structured management of AI-related risks and opportunities.

This project explores these ideas at a deliberately simplified technical level.

## How It Works

The tool collects information about an AI system through a series of questions.

It evaluates four basic risk dimensions:

- Personal data - whether the system uses personal data.
- Decision impact - whether the system makes decisions affecting people.
- Explainability - whether the system's decisions can be explained.
- Human oversight - whether human supervision is present.

Each risk factor contributes to an overall risk score.

The final score is classified as:

- LOW - 0 to 1
- MEDIUM - 2 to 3
- HIGH - 4

## Current Features

The current version includes:

- Interactive command-line input
- Input validation for binary questions (0 / 1)
- Error handling for invalid non-numeric input
- Modular functions
- Generic risk evaluation through a reusable valuta_rischio() function
- Individual risk assessment
- Overall risk score calculation
- Final risk assessment report

## Technologies

- Python 3
- Command-line interface
- Functions
- Variables
- Conditional statements
- while loops
- try/except error handling
- User input
- Basic arithmetic

## How to Run

Clone the repository and run the program from the command line:

python main.py

The program will ask the user a series of questions and generate a preliminary AI risk assessment.

## Example Output

```text
AI RISK ASSESSMENT
------------------
Sistema AI: Recruitment AI

PRIVACY RISK: HIGH RISK
DECISION IMPACT: HIGH RISK
EXPLAINABILITY RISK: HIGH RISK
HUMAN OVERSIGHT RISK: LOW RISK

Overall risk: MEDIUM

```text

```text

## Project Structure

AI_Risk_Assessment/
|
|-- main.py
|-- README.md
|-- .gitignore

## Current Version

```text

Version 3

The current version introduces improved input validation, error handling and a more modular approach to risk evaluation.

The risk assessment logic has also been refactored to reduce code duplication through the use of a reusable valuta_rischio() function.

## Future Development

Possible future versions may introduce:

- Additional AI risk dimensions
- More structured risk categories
- Lists and dictionaries for structured data
- JSON or CSV export
- Risk assessment reporting improvements
- More detailed risk scoring
- AI system impact assessment
- A more detailed AI risk and governance framework
- Further alignment with AI governance and regulatory concepts

## Professional Development

This project is part of an ongoing effort to develop practical technical skills alongside an academic and professional background in philosophy, ethics and education.

The broader objective is to develop competencies at the intersection of:

- AI ethics
- AI risk management
- AI governance
- Regulatory compliance
- AI management systems
- Technical implementation

Future iterations will progressively expand the technical complexity of the project while maintaining its focus on responsible and risk-aware AI development and deployment.

## Disclaimer

This tool is a preliminary educational and portfolio project.

It does not constitute a legal, regulatory or professional AI risk assessment and should not be used as a substitute for a formal compliance or risk management process.

The risk categories implemented in this project are simplified educational criteria and do not determine whether an AI system is high-risk, limited-risk or prohibited under the EU AI Act.