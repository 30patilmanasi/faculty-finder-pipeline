import sqlite3
import os
from sentence_transformers import SentenceTransformer, util

def perform_search():
    # --------------------------------------------------
    # 0. Check if database exists
    # --------------------------------------------------
    db_path = "faculty_data.db"
    if not os.path.exists(db_path):
        print(f"❌ Error: '{db_path}' not found!")
        print("Please run your scraper/storage scripts first to create the database.")
        return

    # --------------------------------------------------
    # 1. Load AI model
    # --------------------------------------------------
    print("🚀 Loading AI Model (all-MiniLM-L6-v2)...")
    # This model is lightweight and excellent for name/topic matching
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # --------------------------------------------------
    # 2. Connect to database and fetch data
    # --------------------------------------------------
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT name, research, specialization FROM faculty")
        rows = cursor.fetchall()
    except sqlite3.OperationalError:
        print("❌ Error: Table 'faculty' does not exist in the database.")
        return
    finally:
        conn.close()

    if not rows:
        print("⚠️ No faculty data found in the database.")
        return

    # --------------------------------------------------
    # 3. Prepare search corpus (Crucial Change Here)
    # --------------------------------------------------
    names = []
    search_corpus = []

    for name, research, specialization in rows:
        names.append(name)

        # Handle null values
        r_text = research if research and "Data is not available" not in research else ""
        s_text = specialization if specialization and "Data is not available" not in specialization else ""

        # WE ADD THE NAME TO THE TEXT: This allows the AI to "read" the name during search
        # Format: "Name: Abhishek Gupta. Research: Robotics. Specialization: AI"
        combined_text = f"Name: {name}. {r_text} {s_text}".strip()
        
        search_corpus.append(combined_text if combined_text else f"Name: {name}")

    # --------------------------------------------------
    # 4. Generate embeddings (The Index)
    # --------------------------------------------------
    print(f"📊 Indexing {len(search_corpus)} faculty profiles. Please wait...")
    corpus_embeddings = model.encode(
        search_corpus,
        convert_to_tensor=True,
        show_progress_bar=True
    )

    # --------------------------------------------------
    # 5. Interactive search loop
    # --------------------------------------------------
    print("\n✅ Semantic Search Engine Ready!")
    print("-----------------------------------------")
    print("💡 You can search by:")
    print("  • Full Names (e.g., 'Abhishek Gupta')")
    print("  • Topics (e.g., 'machine learning expert')")
    print("  • Keywords (e.g., 'who works in VLSI')")
    print("Type 'exit' to quit.")

    while True:
        query = input("\n🔎 Enter search query: ").strip()

        if not query:
            continue
        if query.lower() in ["exit", "quit", "q"]:
            print("👋 Exiting search engine. Goodbye!")
            break

        # Encode the user's query
        query_embedding = model.encode(query, convert_to_tensor=True)

        # Perform semantic search
        hits = util.semantic_search(
            query_embedding,
            corpus_embeddings,
            top_k=3
        )[0]

        print(f"\nResults for: '{query}'")
        print("-" * 30)

        found_any = False
        for i, hit in enumerate(hits, start=1):
            idx = hit["corpus_id"]
            score = hit["score"] * 100  # Convert to percentage

            # Filter out very low-quality matches (Threshold)
            if score < 35:
                continue
            
            found_any = True
            print(f"{i}. 👤 {names[idx]}")
            print(f"   📊 Match Confidence: {score:.2f}%")
            
            # Show a snippet of the context found
            snippet = search_corpus[idx]
            if len(snippet) > 160:
                snippet = snippet[:157] + "..."
            print(f"   🔬 Context: {snippet}\n")

        if not found_any:
            print("❌ No confident matches found. Try different keywords.")

if __name__ == "__main__":
    try:
        perform_search()
    except KeyboardInterrupt:
        print("\n\nStopped by user.")