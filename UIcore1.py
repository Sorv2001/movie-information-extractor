import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# ── Page Config ────────────────────────────────────
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

# ── Force Dark Theme (IMPORTANT 🔥) ────────────────
st.markdown("""
<style>
    body { background-color: #0E1117; color: white; }
    .stApp { background-color: #0E1117; }
    .stTextArea textarea {
        background-color: #1E1E1E;
        color: white;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #7F77DD;
        color: white;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        font-size: 16px;
        width: 100%;
        border: none;
    }
    .stButton button:hover {
        background-color: #534AB7;
    }
</style>
""", unsafe_allow_html=True)

# ── Model ──────────────────────────────────────────
model = ChatMistralAI(model="mistral-large-latest")

# ── Pydantic Model ─────────────────────────────────
class MovieInfo(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# ── Parser ─────────────────────────────────────────
parser = PydanticOutputParser(pydantic_object=MovieInfo)

# ── Prompt ─────────────────────────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a Movie Information Extractor.
Extract movie information from the paragraph.

{format_instructions}
"""),
    ("human", "{paragraph}")
])

# ── UI Header ──────────────────────────────────────
st.markdown("## 🎬 Movie Information Extractor")
st.caption("Paste a movie paragraph and get structured output like JSON.")
st.divider()

# ── Input ──────────────────────────────────────────
para = st.text_area(
    "Enter your movie paragraph:",
    height=150,
    placeholder="e.g. 3 Idiots is a critically acclaimed Bollywood film..."
)

# ── Button ─────────────────────────────────────────
if st.button("Extract Data"):
    if para.strip():
        with st.spinner("Extracting..."):

            final_prompt = prompt.invoke({
                "paragraph": para,
                "format_instructions": parser.get_format_instructions()
            })

            response = model.invoke(final_prompt)

            raw_output = response.content
            result = parser.parse(raw_output)

        st.divider()

        # ── RAW MODEL OUTPUT ────────────────────────
        st.markdown("### Raw Model Output")
        st.code(raw_output, language="json")

        st.divider()

        # ── STRUCTURED OUTPUT (LIKE VIDEO 🔥) ───────
        st.markdown("### Structured Output")

        # 👉 This creates expandable JSON UI
        st.json(result.model_dump())

    else:
        st.warning("Please enter a movie paragraph first.")