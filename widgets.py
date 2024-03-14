import streamlit as st

def widgets():
    st.title("🍒Interactive Input Widgets")

    # Move Color Picker to the top
    color = st.color_picker('Pick A Color', '#00f900')
    st.markdown(f'<p style="color:{color};">This text changes color dynamically!</p>', unsafe_allow_html=True)

    # List of fruits for options
    fruit_options = ['Apple', 'Banana', 'Cherry', 'Orange']

    # Button
    if st.button('Click Me'):
        st.success("Button clicked!")

    # Checkbox
    check = st.checkbox('Check for Yes')
    if check:
        st.write("Checked!")

    # Radio Buttons
    radio_option = st.radio("Choose a fruit:", fruit_options)
    st.write(f"{radio_option} is overrated")

    # Selectbox
    select_option = st.selectbox("Select a fruit:", fruit_options)
    st.write(f"Now I think {select_option} is overrated")

    # Multiselect
    multi_select_options = st.multiselect("Select multiple fruits:", fruit_options)
    st.write(f"I love {multi_select_options}")

    # Slider
    slider_val = st.slider("Select a value", 0, 100, 25)
    st.write(f"I have {slider_val} siblings")

    # Select Slider
    select_slider_option = st.select_slider("Select a fruit", options=fruit_options)
    st.write(f"Why are {select_slider_option} so delicious?")

    # Text Input
    text_input = st.text_input("Enter some text")
    if text_input:
        st.write(f"You entered: {text_input}")

    # File Uploader
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.write("File uploaded successfully!")

# Run the app
if __name__ == "__main__":
    widgets()
