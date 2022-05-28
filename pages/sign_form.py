
import streamlit as st

def app():
    st.title("Welcome")
    flag = True
    with st.form("my_form"):
        st.write("Sign In")
        first_name = st.text_input("Imienie")
        surname = st.text_input("Nazwisko")
        checkbox_val = st.checkbox("consent )))")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            all_check = True
            if len(first_name) < 3:
                st.write("<font color='red'> Imie za krótkie (min 3 symbola) </font>", unsafe_allow_html=True)
                all_check = False

            if len(surname) < 3:
                st.write("<font color='red'> Nazwisko za krótkie (min 3 symbola) </font>", unsafe_allow_html=True)
                all_check = False

            if checkbox_val and all_check:
                st.write("<font size=10 color='green'> Success </font>", unsafe_allow_html=True)
                st.write("Hi ", first_name, surname, "checkbox", checkbox_val)
                flag = False
            elif not checkbox_val:
                st.write("<font color='red'> Consent is mandatory </font>", unsafe_allow_html=True)


    