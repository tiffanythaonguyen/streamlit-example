import streamlit as st
import pandas as pd
from transformers import BartForConditionalGeneration, BartTokenizer

# Initialize the BART summarizer and tokenizer
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

def get_data(data):
    content = ""
    if '.csv' in data.name:
        df = pd.read_csv(data)
        content = '\n'.join(df.head().apply(lambda x: ', '.join(x.dropna().astype(str)), axis=1))
    elif '.pdf' in data.name:
        # Extract text using PyPDF2 or your preferred method
        content = "PDF text extraction not implemented here."  # Placeholder
    elif '.xlsx' in data.name:
        df = pd.read_excel(data, engine='openpyxl')
        content = '\n'.join(df.head().apply(lambda x: ', '.join(x.dropna().astype(str)), axis=1))
    return content

def generate_questions(content):
    # Basic heuristic: Extract key sentences and turn them into questions
    # This is a simple example and might not work perfectly on all content
    sentences = content.split('. ')
    questions = []

    for sentence in sentences:
        if " is " in sentence:
            questions.append(sentence.replace(" is ", " is what? "))
        elif " are " in sentence:
            questions.append(sentence.replace(" are ", " are what? "))
        elif " have " in sentence:
            questions.append(sentence.replace(" have ", " have what? "))

    # Return the first three questions, or fewer if not enough were generated
    return questions[:3]

def main():
    st.title("FinanceEconTool")
    
    class_option = st.selectbox("Choose your class:", ["Math for Finance and Analytics with R", "Analytics for Finance", "Database Management Systems - SQL", "Data Science with Python", "Econometrics"])
    
    uploaded_files = st.file_uploader("Upload your class notes or materials", type=['csv', 'xlsx', 'pdf'], accept_multiple_files=True)
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            content = get_data(uploaded_file)
            st.write(f"### Questions for file: {uploaded_file.name}")
            questions = generate_questions(content)
            for q in questions:
                st.write("- " + q)

if __name__ == '__main__':
    main()
