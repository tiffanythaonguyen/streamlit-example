import streamlit as st
import fitz  # PyMuPDF
from wordcloud import WordCloud
import requests
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to generate and display word cloud
def generate_word_cloud(pdf_urls):
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
    st.pyplot(plt)  # Display the word cloud in Streamlit

# Main function for the app
def main():
    st.title("PDF Word Cloud Generator")
    st.markdown("Generate a word cloud from open source PDFs.")

    pdf_urls = [
        'https://ocw.mit.edu/courses/15-031j-energy-decisions-markets-and-policies-spring-2012/ba02e762046b99e81578e7d19980bb22_MIT15_031JS12_lec10.pdf',
        'https://ocw.mit.edu/courses/15-433-investments-spring-2003/c5845cd981c2e63f7ff303c92c7d41be_154332random_walk.pdf'
    ]

    generate_word_cloud(pdf_urls)

if __name__ == "__main__":
    main()
