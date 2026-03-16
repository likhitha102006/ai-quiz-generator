import streamlit as st
import random

# 🎨 Background Styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/thumbnails/007/393/526/small/q-and-a-discussion-faq-support-question-and-answer-help-service-business-concept-photo.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* Dark overlay for readability */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.6);
        z-index: -1;
    }

    /* Make text white */
    h1, h2, h3, h4, h5, h6, p, label, div {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title(" Quiz Generator")

st.write("Enter study material and generate MCQ questions.")

text_input = st.text_area("Enter Study Material")
num_questions = st.slider("Number of Questions", 1, 5, 3)

def split_sentences(text):
    sentences = text.replace("!", ".").replace("?", ".").split(".")
    return [s.strip() for s in sentences if s.strip()]

if st.button("Generate Quiz"):

    if text_input.strip() == "":
        st.warning("Please enter study material.")
    else:

        sentences = split_sentences(text_input)
        all_words = text_input.split()

        questions = []

        for sentence in sentences:
            words = sentence.split()

            if len(words) > 4:
                answer = random.choice(words)
                question = sentence.replace(answer, "_____")

                wrong = random.sample(all_words, min(3, len(all_words)))
                options = wrong + [answer]
                random.shuffle(options)

                questions.append((question, answer, options))

        questions = questions[:num_questions]

        with st.form("quiz_form"):

            user_answers = []

            for i, (q, ans, opts) in enumerate(questions):

                st.write(f"**Q{i+1}: {q}**")

                choice = st.radio(
                    "Select answer:",
                    opts,
                    key=f"q{i}"
                )

                user_answers.append((choice, ans))

            submit = st.form_submit_button("Submit Answers")

        if submit:

            score = 0

            for i, (user, correct) in enumerate(user_answers):

                if user == correct:
                    st.success(f"Q{i+1}: Correct ✅")
                    score += 1
                else:
                    st.error(f"Q{i+1}: Wrong ❌ Correct answer: {correct}")

            st.subheader(f"🎯 Your Score: {score}/{len(user_answers)}")