import streamlit as st
from textblob import TextBlob

# Run -> streamlit run sentiment_analysis.py

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text and returns the sentiment description
    (Positive, Neutral, Negative) along with a sentiment code (positive, neutral, negative).
    
    Parameters:
    - text (str): The input text to analyze.
    
    Returns:
    - tuple: (sentiment description, sentiment code)
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'Positive', 'positive'
    elif polarity == 0:
        return 'Neutral', 'neutral'
    else:
        return 'Negative', 'negative'

def color_based_on_sentiment(sentiment):
    """
    Determines the background color based on the sentiment code.
    
    Parameters:
    - sentiment (str): The sentiment code.
    
    Returns:
    - str: CSS style string for the background color.
    """
    if sentiment == 'positive':
        color = '#98FB98'
    elif sentiment == 'negative':
        color = '#FF6347'
    else:
        color = '#FFD700' 
    return f'background-color: {color};'

def main():
    """
    Main function to run the Streamlit app.
    """
    st.title("Sentiment Analysis Dashboard")

    user_input = st.text_area("Type your text...")

    if st.button("Analyze"):
        sentiment, sentiment_code = analyze_sentiment(user_input)
        st.markdown(f"<h1 style='text-align: center; color: black; {color_based_on_sentiment(sentiment_code)}'>\
                    {sentiment}</h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
