# Initialize session state for the file
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# File uploader
uploaded_file = st.file_uploader("Choose a file")

# If a file is uploaded, store it in session state
if uploaded_file is not None:
    st.session_state.uploaded_file = uploaded_file

# Button to display file name
if st.button('Show file name'):
    if st.session_state.uploaded_file is not None:
        st.write("Filename:", st.session_state.uploaded_file.name)
    else:
        st.write("No file uploaded yet.")
