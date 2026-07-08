import os
from collections import defaultdict
import streamlit as st

from rag.rag_pipeline import RAGPipeline

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------------------
# Initialize RAG Pipeline
# ---------------------------------------------------

@st.cache_resource
def get_pipeline():
    return RAGPipeline()

pipeline = get_pipeline()

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.header("📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=[
            "pdf",
            "docx",
            "txt",
            "rtf",
            "csv",
            "xlsx",
            "png",
            "jpg",
            "jpeg"
        ]
    )

    if uploaded_file is not None:

        upload_folder = "data/uploads"

        os.makedirs(upload_folder, exist_ok=True)

        file_path = os.path.join(
            upload_folder,
            uploaded_file.name
        )

        # Save uploaded file
        with open(file_path, "wb") as file:

            file.write(uploaded_file.getbuffer())

        with st.spinner("Processing document..."):

            chunks = pipeline.ingest_document(file_path)

        st.session_state.document_uploaded = True

        st.success(f"✅ {uploaded_file.name} uploaded successfully!")
        st.caption(f"Chunks created: {chunks}")

    st.divider()

    st.subheader("Supported Formats")

    st.markdown("""
- 📄 PDF
- 📝 DOCX
- 📃 TXT / RTF
- 📊 CSV / Excel
- 🖼️ PNG / JPG
""")

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("📄 Enterprise RAG Assistant")

st.markdown(
    """
Ask questions about your documents using Retrieval-Augmented Generation (RAG).

Upload a document, and the AI will answer questions based only on its contents.
"""
)

st.divider()

# ---------------------------------------------------
# Chat Interface
# ---------------------------------------------------

# Display previous conversation
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# Show chat only after document upload
if st.session_state.document_uploaded:

    question = st.chat_input(
        "Ask a question about your document..."
    )

    if question:

        # Display user message
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):

            st.markdown(question)

        with st.spinner("Thinking..."):

            # Build conversation history
            chat_history = "\n".join(

                f"{message['role'].capitalize()}: {message['content']}"

                for message in st.session_state.messages
            )

            response = pipeline.ask(
                question=question,
                chat_history=chat_history
            )

        answer = response["answer"]

        with st.chat_message("assistant"):

            st.markdown(answer)

            if response["sources"]:

                grouped_sources = defaultdict(set)

                for source in response["sources"]:

                    metadata = source["metadata"]

                    grouped_sources[
                        metadata["source"]
                    ].add(
                        int(metadata["page"])
                    )

                st.markdown("#### 📚 Sources")

                for document, pages in grouped_sources.items():

                    page_list = ", ".join(
                        str(page)
                        for page in sorted(pages)
                    )

                    st.markdown(
                        f"""
📄 **{document}**

Pages: **{page_list}**
"""
                    )

        st.session_state.messages.append({

            "role": "assistant",

            "content": answer

        })

else:

    st.info(
        "👈 Upload a document from the sidebar to begin."
    )