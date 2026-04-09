import os
import streamlit as st
import sqlite3
from sentence_transformers import SentenceTransformer, util

# 🎨 UI STYLE
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Stars */
.stApp::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background-image: radial-gradient(white 1px, transparent 1px);
    background-size: 50px 50px;
    opacity: 0.15;
    animation: moveStars 60s linear infinite;
    z-index: 0;
}

@keyframes moveStars {
    from {transform: translateY(0);}
    to {transform: translateY(-100px);}
}

/* Card */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 15px;
    border: 1.5px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    margin-top: 20px;
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    border: 1.5px solid #00f2fe;
    transform: scale(1.01);
}

/* Input */
.stTextInput input {
    background: white;
    color: black !important;
}

/* Score */
.score-text {
    color: white;
    font-size: 40px;
    font-weight: bold;
}

.score-label {
    color: #ccc;
    font-size: 14px;
}

/* Round image (future use) */
img {
    border-radius: 50%;
}
</style>
""", unsafe_allow_html=True)

# CONFIG
os.environ["STREAMLIT_SERVER_PORT"] = "7860"
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"

st.set_page_config(page_title="Faculty Finder AI", page_icon="🎓", layout="wide")

# 🤖 MODEL
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# 📂 DATABASE
def get_clean_data():
    if not os.path.exists("faculty_data.db"):
        return []

    conn = sqlite3.connect("faculty_data.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faculty")
    rows = cursor.fetchall()
    conn.close()
    return rows

# 🎯 UI HEADER
st.title("🎓 Faculty Recommender System ✨")
st.markdown("🔍 Search by research topic, name, or specialization.")

data = get_clean_data()

# 📊 SIDEBAR
with st.sidebar:
    st.header("📊 Database Status")
    if data:
        st.success(f"Connected: {len(data)} faculty members found.")
    else:
        st.error("No data found")

# 🔍 SEARCH
query = st.text_input("Search (e.g., 'Arpit Rana')")
query = query.lower()

# 🚀 SEARCH LOGIC
if query and data:

    search_corpus = []
    for r in data:
        text = f"{r['name'] or ''} {r['name'] or ''} {r['research'] or ''} {r['specialization'] or ''}"
        search_corpus.append(text.lower())

    with st.spinner("🔎 Searching..."):
        corpus_embeddings = model.encode(search_corpus, convert_to_tensor=True)
        query_embedding = model.encode(query, convert_to_tensor=True)
        hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=5)[0]

    st.subheader(f"🎯 Top Matches for '{query}'")

    for hit in hits:
        idx = hit['corpus_id']
        score = hit['score'] * 100
        row = data[idx]

        # ⭐ EXACT MATCH = 100%
        if query.strip() == (row['name'] or "").lower():
            score = 100

        if score > 10:

            # ✅ CARD START
            st.markdown('<div class="card">', unsafe_allow_html=True)

            col1, col2 = st.columns([1, 4])

            # 🏆 SCORE
            with col1:
                st.markdown(f"""
                <div class="score-label">🏆 Match Score</div>
                <div class="score-text">{score:.1f}%</div>
                """, unsafe_allow_html=True)

            # 👤 DETAILS
            with col2:
                st.markdown(f"### 👤 {row['name'] or 'Unknown'}")
                st.markdown(f"📧 **Email:** {row['email'] or 'Not Defined'}")
                st.markdown(f"📞 **Phone:** {row['phone'] or 'Not Defined'}")
                st.markdown(f"📍 **Address:** {row['address'] or 'Not Defined'}")
                st.markdown(f"🎓 **Education:** {row['education'] or 'Not Defined'}")
                st.markdown(f"🌟 **Specialization:** {row['specialization'] or 'Not Defined'}")

                if row['profile_url']:
                    st.link_button("🔗 View Full Profile", row['profile_url'])

            # ✅ CARD END
            st.markdown('</div>', unsafe_allow_html=True)

elif query:
    st.warning("⚠️ No database data found.")