import streamlit as st
import requests

st.title("Run Twitter Sentiment Analysis Code from GitHub")

# URL of the raw code file on GitHub
github_url = "https://raw.githubusercontent.com/YourUsername/YourRepoName/main/twitter_sentiment.py"  # Replace with your actual GitHub raw URL

if st.button("Fetch and Run Code"):
    try:
        # Fetch the code from GitHub
        response = requests.get(github_url)
        response.raise_for_status()  # Check for errors in fetching

        # Get the code content as a string
        code_content = response.text

        # Display the fetched code for reference
        st.subheader("Fetched Code from GitHub")
        st.code(code_content, language="python")

        # Execute the code
        exec(code_content)

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching the file: {e}")
    except Exception as exec_error:
        st.error(f"Error executing the code: {exec_error}")
