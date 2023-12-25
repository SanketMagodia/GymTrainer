import streamlit as st 

st.set_page_config(page_title = "Gym Buddy", layout = "wide")


with st.container():
    # st.subheader("hey")
    st.title("Lets Workout")
    st.write("I can be your trainer")
    st.write("Show me what you got")
    st.write("Select the workout you want me to monitor from the sidebar..")


with st.container():
    st.write("---")