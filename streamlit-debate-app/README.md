# Streamlit Debate App

This project is a Streamlit application that features a debate between two AI bots, Steve and Elon. The bots engage in a discussion on the topic: "Who has contributed more to the greater advancement of Technology in society?" over 50 conversations, with each bot posing relevant follow-up questions. At the end of the debate, a referee bot summarizes the discussion and declares a winner.

## Project Structure

```
streamlit-debate-app
├── src
│   ├── app.py          # Main entry point of the Streamlit application
│   ├── bots
│   │   ├── steve.py    # Implementation of the Steve bot (OpenAI GPT-4o-mini)
│   │   └── elon.py     # Implementation of the Elon bot (LLAMA 3.2 via Groq API)
│   ├── referee.py       # Referee bot for summarizing and declaring a winner
│   └── types
│       └── index.py     # Custom types and interfaces for the application
├── .env                 # Environment variables for API keys and sensitive information
├── requirements.txt     # Project dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-debate-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file. You will need API keys for OpenAI and Groq.

## Usage Guidelines

To run the Streamlit application, execute the following command:
```
streamlit run src/app.py
```

## Overview of Bots

- **Steve Bot**: Mimics Steve Jobs and utilizes OpenAI's GPT-4o-mini to generate responses and follow-up questions.
  
- **Elon Bot**: Mimics Elon Musk and integrates with LLAMA 3.2 via the Groq API to provide its perspective.

- **Referee Bot**: Analyzes the debate, summarizes key points, and determines the winner based on the arguments presented.

Enjoy the debate!