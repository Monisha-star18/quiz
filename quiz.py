import streamlit as st
import time

# Sample quiz_data with 10 questions
quiz_data = [
    {
        "question_number": 1,
        "question": "Who captained the OAU MFT to their only NUGA Gold medal under Chike Egbunu-Olimene?",
        "options": ["Seyi Olumofe", "Yengibiri Henry", "Addah Obubo", "Ayotunde Faleti"],
        "correct_answer": "Ayotunde Faleti",
        "explanation": "Ayotunde Faleti captained the OAU MFT to their only NUGA Gold medal under Chike Egbunu-Olimene in 2014."
    },
    {
        "question_number": 2,
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "correct_answer": "Paris",
        "explanation": "Paris is the capital city of France."
    },
    {
        "question_number": 3,
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
        "explanation": "Mars is known as the Red Planet due to its reddish appearance."
    },
    {
        "question_number": 4,
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "correct_answer": "Pacific Ocean",
        "explanation": "The Pacific Ocean is the largest ocean on Earth."
    },
    {
        "question_number": 5,
        "question": "Who wrote 'Pride and Prejudice'?",
        "options": ["Charlotte Bronte", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "correct_answer": "Jane Austen",
        "explanation": "'Pride and Prejudice' was written by Jane Austen."
    },
    {
        "question_number": 6,
        "question": "What is the chemical symbol for Gold?",
        "options": ["Au", "Ag", "Gd", "Pt"],
        "correct_answer": "Au",
        "explanation": "The chemical symbol for Gold is Au."
    },
    {
        "question_number": 7,
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "correct_answer": "2",
        "explanation": "The smallest prime number is 2."
    },
    {
        "question_number": 8,
        "question": "Who was the first President of the United States?",
        "options": ["Thomas Jefferson", "John Adams", "Abraham Lincoln", "George Washington"],
        "correct_answer": "George Washington",
        "explanation": "The first President of the United States was George Washington."
    },
    {
        "question_number": 9,
        "question": "What is the speed of light in vacuum?",
        "options": ["300,000 km/s", "150,000 km/s", "299,792 km/s", "299,792,458 m/s"],
        "correct_answer": "299,792,458 m/s",
        "explanation": "The speed of light in vacuum is 299,792,458 meters per second."
    },
    {
        "question_number": 10,
        "question": "What is the largest planet in our Solar System?",
        "options": ["Earth", "Jupiter", "Saturn", "Neptune"],
        "correct_answer": "Jupiter",
        "explanation": "The largest planet in our Solar System is Jupiter."
    }
]

# Function to display the current question and options
def show_question():
    question = quiz_data[st.session_state.current_question]
    st.write(f"Question {question['question_number']}: {question['question']}")
    selected_option = st.radio("Select your answer:", question['options'], key=f"option_{st.session_state.current_question}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Previous"):
            previous_question()
    with col2:
        if st.button("Submit"):
            check_answer(selected_option)
    with col3:
        if st.button("Next"):
            next_question()
    with col4:
        if st.button("Complete Quiz"):
            complete_quiz()

    if 'start_time' not in st.session_state:
        st.session_state.start_time = time.time()

    elapsed_time = time.time() - st.session_state.start_time
    remaining_time = 60 - int(elapsed_time)
    st.sidebar.write(f"Time remaining: {remaining_time} seconds")

    if remaining_time <= 0:
        st.write("Time is up!")
        next_question()

# Function to check the selected answer and provide feedback
def check_answer(selected_option):
    question = quiz_data[st.session_state.current_question]
    if selected_option == question["correct_answer"]:
        st.write("Correct!")
        st.balloons()
        if f"answered_{st.session_state.current_question}" not in st.session_state:
            st.session_state.score += 1
        st.session_state[f"answered_{st.session_state.current_question}"] = True
    else:
        st.write("Incorrect!")
    st.write(f"Explanation: {question['explanation']}")

# Function to move onto the next question
def next_question():
    st.session_state.current_question += 1
    if st.session_state.current_question >= len(quiz_data):
        st.session_state.current_question = len(quiz_data) - 1
    st.session_state.start_time = time.time()
    st.session_state.show_question = True

# Function to move to the previous question
def previous_question():
    st.session_state.current_question -= 1
    if st.session_state.current_question < 0:
        st.session_state.current_question = 0
    st.session_state.start_time = time.time()
    st.session_state.show_question = True

# Function to complete the quiz
def complete_quiz():
    st.session_state.show_question = False

# Function to display a welcome popup after successful login
def show_welcome_popup():
    st.session_state.show_popup = True
    st.write(f"Welcome {st.session_state.name}!")
    st.balloons()

# Main function - initializing the session state variables
def main():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'show_question' not in st.session_state:
        st.session_state.show_question = True
    if 'name' not in st.session_state:
        st.session_state.name = ""
    if 'gender' not in st.session_state:
        st.session_state.gender = ""
    if 'age' not in st.session_state:
        st.session_state.age = ""
    if 'email' not in st.session_state:
        st.session_state.email = ""
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'show_popup' not in st.session_state:
        st.session_state.show_popup = False

    if not st.session_state.logged_in:
        st.title("Welcome to Our Quiz Page")
        with st.form(key='login_form'):
            st.session_state.name = st.text_input("Name")
            st.session_state.gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            st.session_state.age = st.number_input("Age", min_value=1, max_value=100, step=1)
            st.session_state.email = st.text_input("Email")
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if st.session_state.name and st.session_state.gender and st.session_state.age and st.session_state.email:
                st.session_state.logged_in = True
                show_welcome_popup()
            else:
                st.warning("Please fill in all fields")

    if st.session_state.logged_in:
        if st.session_state.show_popup:
            st.success(f"Welcome {st.session_state.name}!")

        st.sidebar.write(f"Name: {st.session_state.name}")
        st.sidebar.write(f"Gender: {st.session_state.gender}")
        st.sidebar.write(f"Age: {st.session_state.age}")
        st.sidebar.write(f"Email: {st.session_state.email}")

        if st.session_state.show_question:
            show_question()
        else:
            st.success(f"Quiz Complete! Your Score: {st.session_state.score}/{len(quiz_data)}")

if __name__ == "__main__":
    main()
