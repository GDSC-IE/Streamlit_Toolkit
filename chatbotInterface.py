import streamlit as st
from openai import OpenAI
from streamlit_chat import message

client = OpenAI(api_key='ENTER-YOUR-API-KEY')

# Function to interact with the GPT-3.5-turbo model
def generate_response(prompt, chat_history):

    # Initial system message
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    
    # Add chat history to messages
    for chat in chat_history:
        messages.append({"role": "user", "content": chat[0]})
        messages.append({"role": "assistant", "content": chat[1]})
    
    # Add the latest user prompt to messages
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = messages
    )
    
    chat_history.append((prompt, response.choices[0].message.content))
    return response.choices[0].message.content, chat_history

st.title("ChatGPT ChatBot With Streamlit and OpenAI")
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []

if 'openai_response' not in st.session_state:
    st.session_state['openai_response'] = []

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def get_text():
    input_text = st.text_input("write here", key="input")
    return input_text

user_input = get_text()

if user_input:
    output, chat_history = generate_response(user_input, st.session_state.chat_history)
    output = output.lstrip("\n")

    # Store the output
    st.session_state.openai_response.append(user_input)
    st.session_state.user_input.append(output)
    st.session_state.chat_history = chat_history

if st.session_state['user_input']:
    for i in range(len(st.session_state['user_input']) - 1, -1, -1):
        # This function displays user input
        message(st.session_state["user_input"][i], 
                key=str(i),avatar_style="icons")
        # This function displays OpenAI response
        message(st.session_state['openai_response'][i], 
                avatar_style="miniavs",is_user=True,
                key=str(i) + 'data_by_user')