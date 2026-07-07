# 🤖 AI Todoist Assistant

An intelligent command-line AI assistant built using LangChain, Google Gemini, and the Todoist API. This assistant understands natural language, allowing users to create and manage Todoist tasks through conversational commands.


## 🚀 Features

📝 Add new tasks to Todoist

📋 View all existing Todoist tasks

🤖 Natural language conversation powered by Google Gemini

💬 Maintains conversation history

🔧 Uses LangChain Agents and Tools

🔐 Secure API key management with .env



## 🛠️ Technologies Used
Python

LangChain

Google Gemini API

Todoist API

python-dotenv

Pydantic



## 📂 Project Structure
AI-Todoist-Assistant/
│

├── main.py 

├── .env         

├── requirements.txt

├── README.md

└── screenshots/

    └── demo.png


    
## ⚙️ Installation



### 1. Clone the Repository

git clone https://github.com/RajshreeGholase/AI-Todoist-Assistant.git

cd AI-Todoist-Assistant



### 3. Create a Virtual Environment (Optional)

python -m venv .venv


Activate it:

Windows

.venv\Scripts\activate

Linux/Mac

source .venv/bin/activate



### 3. Install Dependencies
   
pip install -r requirements.txt




### 🔑 Environment Variables

Create a .env file in the project root.

GEMINI_API_KEY=your_gemini_api_key

TODOIST_API_KEY=your_todoist_api_key




### ▶️ Run the Project

python main.py



## 💬 Example Usage

You: Add a task to complete my Python assignment.

Assistant:

Task added successfully.

You: Show my tasks.

Assistant:

• Complete my Python assignment

• Submit resume

• Buy groceries



## 🧠 How It Works

Loads API keys from the .env file.

Initializes the Google Gemini language model.

Connects to the Todoist API.

Creates LangChain tools for task management.

Uses a LangChain Agent to decide which tool to call.

Maintains conversation history for context-aware responses.



## 📦 Required Packages

langchain

langchain-core

langchain-google-genai

python-dotenv

todoist-api-python

pydantic



## You can generate a requirements.txt using:

pip freeze > requirements.txt



## 🎯 Future Improvements

✅ Delete tasks

✏️ Update existing tasks

📅 Set due dates

🔔 Task reminders

🎙️ Voice input support

🌐 Streamlit web interface

📊 Task prioritization

📁 Project-based task organization



## 👩‍💻 Author

Rajshree Nandkumar Gholase

B.Tech – Artificial Intelligence & Data Science

Python | Machine Learning | AI | LangChain | Generative AI



## ⭐ Support

If you found this project useful, please consider giving it a ⭐ Star on GitHub!
