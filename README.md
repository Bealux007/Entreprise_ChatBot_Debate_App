# Entreprise_ChatBot_Debate_App
**Streamlit Debate App**

A Streamlit-based AI debate system featuring Steve Jobs vs. Elon Musk, where:
AI bots simulate Steve Jobs (GPT-4o-mini) and Elon Musk (LLAMA 3.2 via Groq API).
Each bot engages in a structured debate on technology's impact on society.
A Referee AI summarizes and declares a winner based on argument quality.

**📂 Project Structure**

streamlit-debate-app
├── app.py              # Main Streamlit application
├── bots/
│   ├── steve.py        # Steve Jobs bot (GPT-4o-mini)
│   ├── elon.py         # Elon Musk bot (LLAMA 3.2 via Groq API)
├── referee.py          # Referee bot for summarizing & judging debate
├── types/
│   ├── index.py        # Custom data types
├── requirements.txt    # Project dependencies
├── .env                # API keys (OpenAI, Groq)
├── README.md           # Project documentation

**📜 Key Features**
✅ AI-Powered Debate: Simulates a structured discussion between Steve Jobs and Elon Musk.
✅ Realistic AI Personalities: Each bot mimics the speaking style of the real figures.
✅ Automated Summarization & Winner Selection: A Referee AI analyzes responses.
✅ PDF Report Generation: The debate transcript & results are exported as a PDF.
✅ Streamlit UI: Interactive web app for users to input debate topics.

**📂 Detailed File Breakdown**
📌 app.py (Main Streamlit App)
📌 Purpose:
Provides a web interface for users to start and view the debate.
Handles session management, AI responses, and PDF generation.

**📌 Key Functionalities:**
✅ Allows users to input a debate topic.
✅ Manages turn-based debate between Steve Jobs & Elon Musk.
✅ Uses Referee AI to summarize & pick a winner.
✅ Generates a PDF report of the debate.


**📌 steve.py (Steve Jobs Bot - GPT-4o-mini)**
**📌 Purpose:**

Uses GPT-4o-mini to simulate Steve Jobs' visionary thinking.
📌 Key Features:
✅ Mimics Steve Jobs' speaking style.
✅ Generates insightful responses based on input.
✅ Provides follow-up questions.

**📌 elon.py (Elon Musk Bot - LLAMA 3.2 via Groq API)**
**📌 Purpose:**

Uses LLAMA 3.2 via Groq API to simulate Elon Musk’s perspective.
📌 Key Features:
✅ Mimics Elon Musk’s conversational style.
✅ Fetches responses from Groq API.
✅ Responds to tech & innovation debates.

**📌 referee.py (Referee AI - GPT-4o-mini)**
**📌 Purpose:**

Summarizes the debate & selects a winner.
📌 Key Features:
✅ Ensures one clear winner (Steve or Elon).
✅ Validates debate quality before deciding.
✅ Enforces strict decision rules.

**🛠 Installation & Setup**
1️⃣ Clone the Repository
git clone https://github.com/Bealux007/Streamlit-Debate-App.git
cd Streamlit-Debate-App
2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Up API Keys
Create a .env file and add:
GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions
GROQ_API_KEY=your-api-key
OPENAI_API_KEY=your-api-key
5️⃣ Run the Streamlit App
streamlit run app.py

**Deployment**
To deploy on a cloud server:
Use Streamlit Cloud:
Upload files to GitHub.
Deploy using Streamlit Community Cloud.

**📜 License**
MIT License. Free to use and modify!

**🔗 Contribute**
Pull requests are welcome! If you find a bug, open an issue.

