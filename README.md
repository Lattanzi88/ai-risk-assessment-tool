# AI Risk Assessment Tool

A Python-based educational and portfolio project exploring the intersection of AI risk assessment, ethics and governance.

## Professional Context

This project represents a practical step in my transition from an academic background in philosophy and ethics towards AI governance, AI risk management and responsible AI.

My background combines advanced academic training in philosophy and political philosophy, professional experience in education, and ongoing specialization in Artificial Intelligence.

The project reflects an interdisciplinary approach: applying programming skills to questions concerning AI ethics, risk identification, human oversight, explainability and responsible use of AI systems.

Particular attention is given to the European regulatory framework for Artificial Intelligence, including the risk-based approach of the **EU AI Act**, and to AI management systems such as **ISO/IEC 42001**.

The objective is to demonstrate the ability to connect basic technical implementation with ethical, regulatory and governance considerations.

## Project Purpose

The goal is to build a simple, rule-based tool that collects information about an AI system, evaluates selected risk indicators and generates a preliminary risk assessment report.

The project also serves as a learning portfolio, demonstrating the application of Python programming concepts to an AI governance-related use case.

## Risk Dimensions

The current prototype evaluates four dimensions:

- **Privacy:** whether the system processes sensitive data.
- **Human Impact:** whether the system makes decisions affecting people.
- **Human Oversight:** whether human supervision is absent.
- **Explainability:** whether the system's decisions are difficult to explain.

Each dimension has an assigned severity weight. The tool calculates a cumulative score based on the risk indicators activated by the user's answers.

### Scoring Methodology

The current prototype uses the following weights:

| Risk dimension | Weight |
|---|---:|
| Privacy | 3 |
| Human Impact | 2 |
| Human Oversight | 2 |
| Explainability | 1 |

The maximum possible score is 8.

The overall score is classified according to these project-defined thresholds:

- **LOW:** 0–2
- **MEDIUM:** 3–5
- **HIGH:** 6–8

These weights and thresholds are heuristic design choices created for educational purposes. They are not official EU AI Act risk categories or regulatory thresholds.

## How It Works

1. The user enters the name of the AI system.
2. The program collects four binary answers (`1` or `0`).
3. The answers are converted into risk indicators.
4. The program calculates the cumulative risk score.
5. The overall score determines a preliminary risk level.
6. A recommendation is generated according to the overall level.
7. A structured report is saved as `assessment_report.json`, including the system name, risk indicators, score, recommendation and generation timestamp.

The tool also displays the assessment results in the command line.

## Current Features

- Interactive command-line interface
- Input validation for binary questions
- Error handling for invalid input
- Modular functions
- Dictionary-based representation of risk factors
- Weighted risk score calculation
- Overall risk classification
- Risk summary and preliminary recommendations
- JSON report generation
- Timestamped assessment reports

## Technologies and Concepts

- Python 3
- Variables and data types
- Dictionaries and nested data structures
- Functions and parameters
- Conditional statements
- `while` loops
- `try/except` error handling
- File handling
- JSON serialization
- Basic arithmetic and rule-based logic

## How to Run

Make sure Python 3 is installed, then run the program from the project directory:

```bash
python main.py
```

Follow the prompts and enter `1` for yes or `0` for no.

The program displays the results and generates or updates `assessment_report.json` in the current working directory.

## Example Output

For a test system named `Matrix`, with sensitive data processing and human impact enabled, and with human supervision and explainability present:

```text
AI RISK ASSESSMENT

Sistema AI: Matrix

Privacy : HIGH RISK - Data Protection
Human Impact : HIGH RISK - Human Impact
Human Oversight : LOW RISK - Human Oversight
Explainability : LOW RISK - Transparency

RISK SCORE: 5/8
OVERALL RISK: MEDIUM
Rischi attivi: 2
Gravità totale: 5
Rischio massimo MEDIUM

Raccomandazione:
Definire misure di mitigazione e monitoraggio
```

*Note: the current command-line output contains some Italian labels and descriptions.*

## AI Governance Perspective

The project explores concepts related to:

- AI ethics and responsible AI
- Risk identification and assessment
- Human oversight
- Transparency and explainability
- Data protection
- Regulatory compliance
- AI management systems

The EU AI Act establishes a risk-based regulatory framework with obligations that depend on the type of AI system and its intended use.

ISO/IEC 42001 provides requirements for an AI management system, supporting organizations in establishing and continually improving processes for the responsible management of AI systems.

This project uses these areas as conceptual reference points. It does not implement the complete requirements of either framework.

## Project Structure

```text
ai-risk-assessment-tool/
├── main.py
├── README.md
├── .gitignore
└── assessment_report.json  # Generated when the program runs
```

The JSON report is a generated output and does not necessarily need to be committed to the repository.

## Limitations

This prototype uses a simplified, deterministic scoring model based on four binary indicators and manually assigned weights.

It does not currently assess the full context, intended purpose, deployment conditions, affected populations or all applicable legal obligations of an AI system.

The model's overall score should be interpreted as an internal educational indicator, not as a validated measure of actual risk.

In particular, the output does not determine whether a system is prohibited, high-risk or subject to specific obligations under the EU AI Act.

## Future Development

Possible improvements include:

- Refining the assessment methodology and documenting the rationale for each weight
- Distinguishing risk indicators from risk severity classifications
- Adding more contextual assessment questions
- Improving report readability and traceability
- Introducing structured risk mitigation measures
- Developing test cases for input validation and scoring logic
- Exploring how the assessment could support, but not replace, an AI management system aligned with ISO/IEC 42001

## Professional Development

This project is part of an ongoing effort to develop practical technical skills alongside an academic and professional background in philosophy, ethics and education.

Its broader objective is to build competencies at the intersection of AI ethics, AI risk management, AI governance, regulatory compliance and technical implementation.

The project will evolve progressively, with an emphasis on methodological transparency, responsible use of AI and the ability to explain both the rationale and limitations of an assessment tool.

## Disclaimer

This tool is a preliminary educational and portfolio project.

It does not constitute legal advice, a formal regulatory assessment, a certified risk assessment or evidence of compliance with the EU AI Act or ISO/IEC 42001.

The risk indicators, weights and thresholds are simplified design choices intended to demonstrate basic programming and risk assessment concepts. They should not be used as a substitute for a formal, context-specific risk management or compliance process.