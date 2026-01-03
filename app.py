import streamlit as st
import pickle

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📱",
    layout="centered"
)

# --------------------------------------------------
# LOAD MODEL & VECTORIZER
# --------------------------------------------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# --------------------------------------------------
# THEME STATE
# --------------------------------------------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

st.session_state.dark_mode = st.toggle(
    "🌙 Dark Mode",
    value=st.session_state.dark_mode
)

# --------------------------------------------------
# THEME COLORS
# --------------------------------------------------
if st.session_state.dark_mode:
    bg = "#0e1117"
    card = "#161b22"
    text = "#ffffff"
    input_bg = "#1f2937"
    border = "#30363d"
    button_bg = "#238636"
else:
    bg = "#f5f7fa"
    card = "#ffffff"
    text = "#000000"
    input_bg = "#ffffff"
    border = "#d0d7de"
    button_bg = "#2da44e"

# --------------------------------------------------
# CSS WITH ANIMATION
# --------------------------------------------------
st.markdown(f"""
<style>

/* Remove Streamlit header */
header {{
    background: transparent !important;
}}

/* App animation */
.stApp {{
    background-color: {bg};
    color: {text};
    transition: background-color 0.6s ease, color 0.6s ease;
}}

/* Main container */
div[data-testid="block-container"] {{
    padding-top: 1.5rem;
    animation: fadeScale 0.4s ease;
}}

/* Card animation */
.card {{
    background: {card};
    transition: background-color 0.6s ease, transform 0.4s ease;
}}

/* Text area animation */
textarea {{
    background-color: {input_bg} !important;
    color: {text} !important;
    border: 1px solid {border} !important;
    border-radius: 10px !important;
    font-size: 16px !important;
    transition: background-color 0.5s ease, color 0.5s ease;
}}

textarea::placeholder {{
    color: #9ca3af !important;
}}

/* Button animation */
.stButton > button {{
    background-color: {button_bg};
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-size: 16px;
    transition: background-color 0.4s ease, transform 0.2s ease;
}}

.stButton > button:hover {{
    transform: scale(1.03);
}}

/* Fade + scale animation */
@keyframes fadeScale {{
    from {{
        opacity: 0;
        transform: scale(0.98);
    }}
    to {{
        opacity: 1;
        transform: scale(1);
    }}
}}

/* Hide footer */
footer {{
    visibility: hidden;
}}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER CARD
# --------------------------------------------------
st.markdown(
    f"""
    <div class="card" style="
        padding:30px;
        border-radius:15px;
        box-shadow:0 0 20px rgba(0,0,0,0.3);
        text-align:center;
    ">
        <h1>📱 SMS Spam Detection</h1>
        <p>
            Enter an SMS message and check whether it is
            <b>Spam</b> or <b>Not Spam</b>.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# --------------------------------------------------
# INPUT
# --------------------------------------------------
sms = st.text_area(
    "SMS Message",
    placeholder="Congratulations! You have won a free prize. Click the link now...",
    height=150
)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------
if st.button("🚀 Check SMS"):
    if sms.strip() == "":
        st.warning("⚠️ Please enter an SMS message.")
    else:
        vector = vectorizer.transform([sms])
        prediction = model.predict(vector)

        if prediction[0] == 1:
            st.error("🚨 This SMS is **SPAM**")
        else:
            st.success("✅ This SMS is **NOT SPAM**")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    "<p style='text-align:center;opacity:0.6;'>AI & NLP Based Final Year Project</p>",
    unsafe_allow_html=True
)
