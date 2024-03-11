# Named Entity Recognition (NER) Explorer:
# Task: Develop an app that highlights entities (names, dates, locations) in user-provided text.
# Focus: Using NLP libraries (e.g., spaCy) with Streamlit.

# Importing libraries
import streamlit as st
import spacy
from spacy import displacy
#import spacy_streamlit

# Title
st.title("Named Entity Recognition (NER) Explorer")

# Description
st.write("This app highlights entities (names, dates, locations) in user-provided text.")

# Input text
text = st.text_area("Enter text here")

# Load model
nlp = spacy.load("en_core_web_sm")

# Process text
doc = nlp(text)

models = ["en_core_web_sm", "en_core_web_md"]

# Display entities
if st.button("Show entities"):
    html = displacy.render(doc, style="ent")

    # Using st.write with unsafe_allow_html to render HTML content
    st.write(html, unsafe_allow_html=True)

    # Display the entities in a table for better readability
    #entities = [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    #st.table(entities)

    # Visualize entities using spacy_streamlit
    #spacy_streamlit.visualize(models, text)


# Footer
#st.write("Built with spaCy and Streamlit by the GDSC team.")
