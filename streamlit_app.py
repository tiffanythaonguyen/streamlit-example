import streamlit as st
import re  # Importing the regular expression library
import fitz  # PyMuPDF
from wordcloud import WordCloud
import requests
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to identify numerical values and the next two words or any key after each value
def identify_numerical_values(doc):
    dollar_values = re.findall(r'(\$\d{1,3}(?:,\d{3})*)(?:\s+([\w\s\W]{1,20}))?', doc)
    percent_values = re.findall(r'(\d{1,3}%)(?:\s+([\w\s\W]{1,20}))?', doc)
    whole_numbers = re.findall(r'(\b\d{1,3}(?:,\d{3})*\b)(?!%)(?:\s+([\w\s\W]{1,20}))?', doc)
    decimal_numbers = re.findall(r'(\b\d+\.\d{1,2}\b)(?:\s+([\w\s\W]{1,20}))?', doc)
    months = re.findall(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', doc)
    years = re.findall(r'\b\d{4}\b', doc)
    
    return dollar_values, percent_values, whole_numbers, decimal_numbers, months, years

# Main function
def main():
    st.title("Business Analysis")
    
    st.markdown("## 📌 Paste Document")
    
    doc = st.text_area("Paste your text below (max 500 words)", height=200)
    
    if st.button("Analyze Text"):
        dollar_values, percent_values, whole_numbers, decimal_numbers, months, years = identify_numerical_values(doc)
        
        st.write(f"Identified dollar values: {dollar_values}")
        st.write(f"Identified percent values: {percent_values}")
        st.write(f"Identified whole numbers: {whole_numbers}")
        st.write(f"Identified decimal numbers: {decimal_numbers}")
        st.write(f"Identified months: {months}")
        st.write(f"Identified years: {years}")

# Function to add object detection dataframe table
def object_detection_page():
    st.title("Object Detection Dataframe Table")
    # Create a sample dataframe
    import pandas as pd
    data = {
        "Layout": [1, 2, 3],
        "Index": [101, 102, 103],
        "Image": ["img1.jpg", "img2.jpg", "img3.jpg"],
        "Background": ["Blue", "Green", "Red"],
        "Objectives": ["Obj1", "Obj2", "Obj3"],
        "Goals": ["Goal1", "Goal2", "Goal3"],
        "Timestamp": ["2023-09-01", "2023-09-02", "2023-09-03"],
        "URL": ["url1", "url2", "url3"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

# Function to generate Word Cloud
def generate_word_cloud():
    pdf_urls = [
        'https://ocw.mit.edu/courses/15-031j-energy-decisions-markets-and-policies-spring-2012/ba02e762046b99e81578e7d19980bb22_MIT15_031JS12_lec10.pdf',
        'https://ocw.mit.edu/courses/15-433-investments-spring-2003/c5845cd981c2e63f7ff303c92c7d41be_154332random_walk.pdf'
    ]
    
    combined_text = ''
    
    for pdf_url in pdf_urls:
        response = requests.get(pdf_url)
        pdf_content = response.content
        pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
        num_pages = pdf_document.page_count
        for page_num in range(num_pages):
            page = pdf_document.load_page(page_num)
            combined_text += page.get_text("text")
        pdf_document.close()

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([combined_text])

    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title("Combined Word Cloud for Open Source PDFs")
    plt.axis('off')
    plt.show()

# App navigation
app_pages = {
    "📊 Business Analysis": main,
    "🔍 Object Detection": object_detection_page,
    "🌟 Word Cloud": generate_word_cloud
}

selected_page = st.sidebar.selectbox("Select a page", list(app_pages.keys()))
app_pages[selected_page]()

if __name__ == "__main__":
    main()
