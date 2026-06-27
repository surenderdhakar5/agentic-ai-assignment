import streamlit as st
from agent import run_agent

st.set_page_config(
    page_title="AI Customer Support Agent",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e3a8a,#312e81);
}

.main-container{
max-width:1000px;
margin:auto;
margin-top:30px;
background:rgba(255,255,255,.08);
padding:40px;
border-radius:25px;
backdrop-filter:blur(20px);
box-shadow:0 10px 40px rgba(0,0,0,.35);
}

h1{
color:white !important;
text-align:center;
font-size:52px;
font-weight:800;
margin-bottom:10px;
}

.subtitle{
color:#dbeafe;
text-align:center;
font-size:20px;
margin-bottom:30px;
}

.stTextInput input{
background:white;
border-radius:15px;
padding:18px;
font-size:18px;
border:2px solid #3b82f6;
}

.stButton>button{
background:linear-gradient(90deg,#2563eb,#7c3aed);
color:white;
border:none;
border-radius:12px;
padding:12px 30px;
font-size:18px;
font-weight:bold;
width:100%;
transition:0.3s ease;
cursor:pointer;
}

.stButton>button:hover{
box-shadow:0 0 25px #2563eb;
transform:scale(1.05);
transition:.3s;
background:#1d4ed8;
}



div[data-testid="stSidebar"]{
background:#0b1120;
}

div[data-testid="stSidebar"] *{
color:white;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("🤖 AI Agent")
st.sidebar.markdown("---")

st.sidebar.info("""
### 🚀 AI Customer Support

✅ Order Tracking

✅ Product Details

✅ Product Search

✅ Cheaper Alternatives

✅ Gemini AI

---

👨‍💻 Developed by

**Surendra Nagar**
""")

st.sidebar.success("Features")



st.markdown('<div class="main-container">',unsafe_allow_html=True)

st.markdown("""
<h1>
🤖 AI Customer Support Agent
</h1>

<h3 style='text-align:center;color:#93c5fd;'>
Fast • Smart • Powered by Gemini
</h3>
""",unsafe_allow_html=True)

st.markdown(
'''
<p class="subtitle">
🚀 Smart AI Assistant powered by <b>Gemini AI</b> + Tool Calling
</p>
''',
unsafe_allow_html=True
)
st.markdown("""
<div style="
background:rgba(255,255,255,0.08);
padding:25px;
border-radius:20px;
margin-top:20px;
box-shadow:0 8px 30px rgba(0,0,0,.25);
">
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "🎯 Quick Examples",
    [
        "🏠 Home",
        "📦 Order Status",
        "🛒 Product Details",
        "🔍 Product Search",
        "💰 Cheaper Alternatives",
        "🧠 Gemini AI"
    ]
)

default_question = ""

if menu == "📦 Order Status":
    default_question = "ORD-1001"

elif menu == "🛒 Product Details":
    default_question = "P101"

elif menu == "🔍 Product Search":
    default_question = "Search Shoes"

elif menu == "💰 Cheaper Alternatives":
    default_question = "Cheaper than P101"

elif menu == "🧠 Gemini AI":
    default_question = "What is Artificial Intelligence?"

question = st.text_input(
    "",
    value=default_question,
    placeholder="💬 Ask about Order, Product or AI..."
)

col1, col2, col3 = st.columns([2,1,2])

with col2:
    submit = st.button("🚀 Ask AI")

if submit:

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        answer = run_agent(question)

        st.markdown("## ✨ AI Response")

        st.code(answer)