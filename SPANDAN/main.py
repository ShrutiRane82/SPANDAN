import streamlit as st
from a import predict_heart_failure
from b import provide_feedback

def main():
    page = st.sidebar.radio("Navigation", ["Prediction", "Feedback"])

    if page == "Prediction":
        predict_heart_failure()

    elif page == "Feedback":
        provide_feedback()

if __name__ == "__main__":
    main()
