# Streamlit_Toolkit
A repository demonstrating examples of using a Streamlit library for different tasks.

In order to try using all the different functionalities (without the struggle of installing different libraries one at a time), we suggest you run
```
pip install -r requirements.txt
```
  
## Chatbot Interface (genAI):
An interactive chatbot using Streamlit and OpenAI. Users type messages, and the chatbot responds with dynamically generated answers.
- Focus: Real-time conversational UI with genAI
**UI**
<img src="https://github.com/GDSC-IE/Streamlit_Toolkit/assets/64359365/4a95f110-4358-4369-9ca8-cffc00f0144f" width="500" height="600">

To use it run
```
streamlit run chatbot_interface.py
```

## Named Entity Recognition (NER) Explorer CESAR:
- [ ] Task: Develop an app that highlights entities (names, dates, locations) in user-provided text.
- Focus: Using NLP libraries (e.g., spaCy) with Streamlit.

## Sentiment Analysis Dashboard INIGO:
An app that predicts sentiment (positive, negative, neutral) from user input text.
- Focus: Integrating sentiment analysis libraries (e.g., TextBlob) with Streamlit.
<img src="https://github.com/GDSC-IE/Streamlit_Toolkit/assets/64359365/c547da14-1237-49fa-9690-cf12e81f9ee4" width="700" height="600">

To use it run
```
streamlit run sentiment_analysis.py
```

## Image Capturing and Hand detection:
Extending Streamlit to handle images. Users upload an image, and the app detects hand landmark. Can be repurposed to process images in any other way.
- Focus: Image processing and display.
<img src="https://github.com/GDSC-IE/Streamlit_Toolkit/assets/64359365/d62b9a39-42fc-43cc-9f30-1a1ff61b02d7" width="500" height="600">

To use it run
```
streamlit run image_capturing_hand_detection.py
```

## Interactive Widgets:
Showcasing Streamlit widgets (sliders, dropdowns). Users interact with widgets to adjust values.
- Focus: Creating responsive user interfaces.
- 
<img src="https://github.com/GDSC-IE/Streamlit_Toolkit/assets/64359365/b7a25143-4e8d-49d3-8dc6-a1d39ec59b09" width="500" height="1000">

To use it run
```
streamlit run widgets.py
```


## Markdown and HTML Elements:
Introducing Markdown and HTML support. Add headers, bullet points, and images to provide context.
Enhancing app content.

<img src="https://github.com/GDSC-IE/Streamlit_Toolkit/assets/64359365/aac8f33a-e1b9-49d4-9dec-9b5a96af6710" width="500" height="900">

To use it run
```
streamlit run markdown_and_html.py
```

## Session State and caching (several tabs open):
Keeping session state variables.

<img src="https://github.com/GDSC-IE/Streamlit_Toolkit/assets/64359365/dab2055d-4221-4afe-b57f-f95373d4e129" width="500" height="500">
<img src="https://github.com/GDSC-IE/Streamlit_Toolkit/assets/64359365/fde1c6a3-cd05-4af2-92a8-36c5ee510578" width="500" height="500">
<img src="https://github.com/GDSC-IE/Streamlit_Toolkit/assets/64359365/5edcc67e-5e4a-4b7f-80f5-16c86ea5b02c" width="500" height="200">

To use it run
```
streamlit run session_state_and_chaching.py
```
