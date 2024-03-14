import streamlit as st
from streamlit_option_menu import option_menu
import time 

# Function to load quiz questions and answers (Cached)
@st.cache_data()
def get_quiz_data():
    return [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"question": "What element has the chemical symbol 'O'?", "options": ["Oxygen", "Gold", "Osmium", "Olivine"], "answer": "Oxygen"},
        {"question": "Which gas is most abundant in the Earth's atmosphere?", "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "answer": "Nitrogen"},
        {"question": "In what year did the first human land on the Moon?", "options": ["1959", "1969", "1979", "1989"], "answer": "1969"},
        {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"},
        {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"], "answer": "Leonardo da Vinci"}
    ]


# Initialize session state variables if they don't exist
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

def display_question(quiz_data):
    st.title("Simple Quiz App")

    # Allows users to restart the quiz
    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        
    # Retrieve and display the current question and options
    question = quiz_data[st.session_state.current_question]
    st.markdown('\n')
    st.write(question["question"])
    for option in question["options"]:
        st.button(option, on_click=lambda opt=option: (
            (st.session_state.__setitem__('score', st.session_state.score + 1), st.success("Correct!")) if opt == question["answer"] else st.error("Wrong answer!"),
            # Increment question index or display completion message
            st.session_state.__setitem__('current_question', st.session_state.current_question + 1) if st.session_state.current_question < len(quiz_data) - 1 else st.info("Congrats, you finished the quiz! Check your score in the Score tab!")
        ))

# Function to display the user's score after completing the quiz
def show_results():
    st.title("Your current Score")
    st.write(f"Quiz completed! Your score is {st.session_state.score}/{len(get_quiz_data())}.")
    
# Function to present the main advantages of session_state and caching
def example():
    # Initialize or increment the counter in the session state
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    def increment_counter():
        st.session_state.counter += 1

    st.header('Session State Counter Demo')

    increment = 0
    if st.button('Increment without session_state'):
        increment += 1
    if st.button('Increment with session_state'):
        increment_counter()

    # Display the current count
    st.write(f'Count without session_state: {increment}')
    st.write(f'Count: {st.session_state.counter}')
    
    # Define a function that simulates a time-consuming operation
    def expensive_operation():
        time.sleep(5)  # Wait for 5 seconds
        return "Operation completed!"

    # Define a cached version of the same function
    @st.cache_data
    def cached_expensive_operation():
        time.sleep(5)  # Wait for 5 seconds
        return "Cached operation completed!"

    st.header('Caching Demo')

    # Button to perform the expensive operation without caching
    if st.button('Perform Expensive Operation'):
        result = expensive_operation()
        st.write(result)

    # Button to perform the expensive operation with caching
    if st.button('Perform Cached Expensive Operation'):
        cached_result = cached_expensive_operation()
        st.write(cached_result)
        

def main():
    st.title("Session_State and Caching")
    
    # Render the option menu
    selected = option_menu(
        menu_title=None,  # Menu title is optional
        options=["Test", "Quiz", "Score"],  # Required
        icons=['', 'sunglasses', 'graph-up'],  # Optional
        menu_icon="cast",  # Optional
        default_index=0,  # Optional
        orientation="horizontal",
    )

    quiz_data = get_quiz_data()  # Load the quiz data once

    if selected == "Test":
        example()        
    elif selected == "Quiz":
        display_question(quiz_data)
    elif selected == "Score":
        show_results()

if __name__ == "__main__":
    main()
