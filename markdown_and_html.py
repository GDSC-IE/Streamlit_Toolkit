import streamlit as st

st.title("Markdown Example")

# Display a markdown header
st.header("This is a Header")

# Display a markdown paragraph
st.markdown("Streamlit is **awesome** for creating interactive web apps.")

# Display a list
st.markdown("- Item 1\n- Item 2\n- Item 3")

# Display an image with a caption
st.image("https://via.placeholder.com/150", caption="Placeholder Image")

st.title("HTML Example")

# Display an HTML header
st.write("<h1 style='color: blue;'>This is an HTML Header</h1>", unsafe_allow_html=True)

# Display an HTML paragraph
st.write("<p>Streamlit can also render <strong>HTML</strong> content.</p>", unsafe_allow_html=True)

# Display an HTML list
st.write("<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>", unsafe_allow_html=True)

# Display an HTML image
st.write("<img src='https://via.placeholder.com/150' alt='Placeholder Image'>", unsafe_allow_html=True)