import streamlit as st
from openai import OpenAI
from streamlit_chat import message

api_key = st.text_input("Enter your OpenAI API key", key="OpenAI API key", type="password")
client = OpenAI(api_key=api_key)

# Function to interact with the GPT-3.5-turbo model
def generate_response(prompt, chat_history):
    """
    This function interacts with the GPT-3.5-turbo model to generate a response.

    Parameters:
    prompt (str): The prompt that will be sent to the GPT-3.5-turbo model.
    chat_history (str): The history of the chat that will be used by the model to generate a response.

    Returns:
    response (str): The generated response from the GPT-3.5-turbo model.
    chat_history (list(tuples)): The updated chat history.
    """

    # Initial system message
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    
    # Add chat history to messages 
    # (we append last 10 messages to avoid exceeding max tokens, just in case. Feel free to modify this)
    for chat in chat_history[-10:]:
        messages.append({"role": "user", "content": chat[0]})
        messages.append({"role": "assistant", "content": chat[1]})
    
    # Add the latest user prompt to messages
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = messages
    )
    
    # Extract content from response
    response = response.choices[0].message.content
    
    # append to beginning of chat history
    chat_history.insert(0, (prompt, response))
    
    # return response and chat history
    return response, chat_history

# Function to get user input
def get_text():
    input_text = st.text_input("Write here", key="input")
    return input_text

# Main application logic
def main():
    # Set up Streamlit app title
    st.title("ChatGPT ChatBot With Streamlit and OpenAI")

    # Initialize session state variables if not present
    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = []

    if 'openai_response' not in st.session_state:
        st.session_state['openai_response'] = []

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    user_input = get_text()

    if user_input:
        output, chat_history = generate_response(user_input, st.session_state.chat_history)
        output = output.lstrip("\n")

        # Store the output in session state (session state is explained in another python file in this repo)
        st.session_state.openai_response.append(user_input)
        st.session_state.user_input.append(output)
        st.session_state.chat_history = chat_history

    if st.session_state['user_input']:
        for i in range(len(st.session_state['user_input']) - 1, -1, -1):
            # Display user input messages
            message(st.session_state["user_input"][i], 
                    key=str(i), avatar_style="icons")
            # Display OpenAI response messages
            message(st.session_state['openai_response'][i], 
                    avatar_style="miniavs", is_user=True,
                    key=str(i) + 'data_by_user')

# Run the application
if __name__ == "__main__":
    main()