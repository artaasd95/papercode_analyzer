import streamlit as st
import requests
import tempfile

def main():
    st.set_page_config(page_title="FastAPI Streamlit Demo", layout="centered")
    st.title("Query Your Documents")

    st.sidebar.header("Configuration")
    pdf_file = st.sidebar.file_uploader("Upload PDF file", type=["pdf"])
    arxiv_url = st.sidebar.text_input("Arxiv URL")
    code_path = st.sidebar.text_input("Code Path")

    st.write("## Enter your query")
    query = st.text_area("", help="Type your query here")

    if st.button("Send Query"):
        # If user uploaded a PDF, save it to a temp file so the FastAPI server
        # can access it. The server will get the path to the temp file.
        pdf_path = None
        if pdf_file is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(pdf_file.read())
                pdf_path = tmp.name  # This is the local path to the uploaded PDF

        # Prepare the payload for the FastAPI endpoint
        payload = {
            "query": query,
            "pdf_path": pdf_path,
            "arxiv_path": arxiv_url,
            "code_path": code_path
        }

        # Send POST request to FastAPI
        try:
            response = requests.post("http://localhost:8000/query", json=payload)
            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Connection error: {e}")

if __name__ == "__main__":
    main()
