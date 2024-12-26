# PapercodeAnalyzer agentic RAG

Welcome to the PapercodeAnalyzer Agentic RAG. 

Here is your README reformatted in standard Markdown for easy copying:

```markdown
# README

## Overview

This repository contains a simple project that uses a **FastAPI** backend and a **Streamlit** frontend to query documents (PDF, Arxiv URLs, or code paths) via a team of agents built using the [phi](https://github.com/phistore/phi) library. The system allows you to:

1. **Upload PDFs** to extract and query information from them.
2. **Analyze Arxiv papers** and incorporate their findings into the knowledge base.
3. **Analyze code** or code repositories (planned or partially supported).
4. **Answer queries** using a combination of local PDF knowledge, Arxiv retrieval, and code analysis.

## Project Structure

```plaintext
.
├── app/
│   ├── arxiv_downloaded/      # Directory to store downloaded Arxiv files
│   ├── __pycache__/           # Compiled Python files (auto-generated)
│   ├── Agents.py              # Contains the definitions of multiple agents
│   ├── app.py                 # FastAPI main server (entry point for the backend)
├── .gitignore                 # Git ignore file for unnecessary files
├── docker-compose.yml         # Docker Compose configuration
├── dockerfile                 # Docker configuration for the app
├── interface.py               # Streamlit interface (frontend)
├── LICENSE                    # License for the repository
├── README.md                  # This readme file
└── requirements.txt           # Python dependencies

## Requirements and Installation

1. **Clone this repository** (or download the code) to your local machine.

2. **Install required packages**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   - **Tip for Windows users**: Ensure you have the latest version of Visual Studio Build Tools installed if you encounter any compilation issues (for example, when installing some Python libraries that require C++ build tools).

3. **Set up PostgreSQL**:
   - The code expects a PostgreSQL database running locally (`db_url="postgresql+psycopg://ai:ai@localhost:5432/ai"`).
   - Make sure you have PostgreSQL installed and running, and create the database `ai` (or use another name, but be sure to update the code accordingly).
   - Create a user named `ai` with the password `ai` (or update the code if you have different credentials).

4. **Check your environment**:
   - Ensure that you have the necessary environment variables set (if any).
   - Confirm that you have the correct Python version (3.9+ recommended).

## Running the Project

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server on `http://localhost:8000`.

2. **Start the Streamlit interface**:
   ```bash
   streamlit run interface.py
   ```
   This will open a local server (usually `http://localhost:8501`) where you can interact with the frontend UI.

3. **Interacting with the App**:
   - **PDF Upload**: In the Streamlit sidebar, you can upload a PDF file. The file will be temporarily stored on the server for analysis.
   - **Arxiv URL**: You can paste an Arxiv URL if you want the system to fetch and analyze the paper from Arxiv.
   - **Code Path**: Provide a local path or GitHub URL (depending on how you plan to implement code analysis) for code analysis.
   - **Query**: Type in your query in the text field and click “Send Query” to get a response.

## Additional Tips for Windows Users

- Make sure long file paths are enabled if you run into path issues when using the ephemeral PDF or Arxiv downloads. You can enable them via the Windows Registry or group policy.
- If you need additional build dependencies, install them using:
  ```bash
  pip install --upgrade setuptools wheel
  ```
  and ensure that you have the Windows C++ Build Tools.

## Updating Requirements

Whenever you install a new package, remember to update your `requirements.txt` by running:
```bash
pip freeze > requirements.txt
```
This helps keep your environment reproducible.



## License

This project is provided under an open-source license (MIT, Apache, etc. as you prefer). Include your license details here.
```