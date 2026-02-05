import os
import streamlit as st
import sqlite3
from sentence_transformers import SentenceTransformer, util

# --- ENVIRONMENT CONFIG ---
os.environ["STREAMLIT_SERVER_PORT"] = "7860"
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"

# --- PAGE CONFIG ---
st.set_page_config(page_title="Faculty Finder AI", page_icon="🎓", layout="wide")

# --- LOAD MODEL (Cached) ---
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# --- DATABASE REPAIR & DATA FETCHING ---
def get_clean_data():
    if not os.path.exists("faculty_data.db"):
        return []
    
    conn = sqlite3.connect("faculty_data.db")
    conn.row_factory = sqlite3.Row  # Crucial for accessing row['column_name']
    cursor = conn.cursor()
    
    # 1. Automatic Schema Repair: Add missing columns if they don't exist
    required_cols = [
        "profile_url", "education", "email", "phone", "address", 
        "faculty_web", "biography", "specialization", "teaching", 
        "publications", "research"
    ]
    
    cursor.execute("PRAGMA table_info(faculty)")
    existing_cols = [col[1] for col in cursor.fetchall()]
    
    for col in required_cols:
        if col not in existing_cols:
            try:
                cursor.execute(f"ALTER TABLE faculty ADD COLUMN {col} TEXT")
            except:
                pass
    conn.commit()

    # 2. Fetch all rows
    cursor.execute("SELECT * FROM faculty")
    rows = cursor.fetchall()
    conn.close()
    return rows

# --- UI INTERFACE ---
st.title("🎓 Faculty Recommender System")
st.markdown("Search by research topic, name, or specialization.")

# Fetch data once for the app session
data = get_clean_data()

# Sidebar Debug Info (Optional - helps you see if data is loaded)
with st.sidebar:
    st.header("📊 Database Status")
    if data:
        st.success(f"Connected: {len(data)} faculty members found.")
    else:
        st.error("No data found. Please check faculty_data.db")

query = st.text_input("Search (e.g., 'Arpit Rana' or 'Machine Learning')", placeholder="Type here...")

if query and data:
    # Prepare text for AI matching
    search_corpus = []
    for r in data:
        # We join Name, Research, and Specialization so the AI can "read" them
        text = f"{r['name'] or ''} {r['research'] or ''} {r['specialization'] or ''}"
        search_corpus.append(text)
    
    with st.spinner("Analyzing faculty profiles..."):
        corpus_embeddings = model.encode(search_corpus, convert_to_tensor=True)
        query_embedding = model.encode(query, convert_to_tensor=True)
        hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=5)[0]

    st.subheader(f"Top Matches for '{query}'")
    
    for hit in hits:
        idx = hit['corpus_id']
        score = hit['score'] * 100
        row = data[idx]
        
        # Lowered threshold to 10% to ensure results like 'Arpit Rana' show up
        if score > 10: 
            with st.container():
                col_score, col_info = st.columns([1, 5])
                
                with col_score:
                    st.metric("Match Score", f"{score:.1f}%")
                
                with col_info:
                    st.markdown(f"### {row['name'] or 'Unknown Name'}")
                    
                    # Display all fields line-by-line with "N/A" fallback
                    st.write(f"**📧 Email:** {row['email'] or 'N/A'}")
                    st.write(f"**📞 Phone:** {row['phone'] or 'N/A'}")
                    st.write(f"**📍 Address:** {row['address'] or 'N/A'}")
                    st.write(f"**🎓 Education:** {row['education'] or 'N/A'}")
                    st.write(f"**🌟 Specialization:** {row['specialization'] or 'N/A'}")
                    st.write(f"**📖 Biography:** {row['biography'] or 'No biography provided.'}")
                    st.write(f"**👨‍🏫 Teaching:** {row['teaching'] or 'No teaching info available.'}")
                    st.write(f"**🔬 Research:** {row['research'] or 'N/A'}")
                    st.write(f"**📚 Publications:** {row['publications'] or 'N/A'}")
                    
                    if row['profile_url']:
                        st.link_button("🌐 View Full Profile", row['profile_url'])
                
                st.divider()
elif query:
    st.warning("Please upload the database file to see results.")