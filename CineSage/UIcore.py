import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# -------------------- SETUP --------------------
st.set_page_config(
    page_title="🎬 Movie Info Extractor", page_icon="🎬", layout="centered"
)

# Initialize model
model = ChatMistralAI(model="mistral-small-2603", max_tokens=15)

# -------------------- PROMPT --------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """  
You are an expert Information Extraction and Data Structuring AI. 
Your ONLY task is to analyze the user-provided text and extract structured movie information.

### STRICT RULES:
1. **ACCURACY:** Only extract information that is explicitly present or very strongly implied in the text. Do NOT invent, assume, or hallucinate any data.
2. **MISSING DATA:** If a specific field is not mentioned, leave it as `null`, `None`, or an empty array `[]`. Do not guess.
3. **LANGUAGE:** Keep the original language of the names. (e.g., If it's a Hindi movie, keep the actor names in Hindi transliteration).

### REQUIRED FIELDS TO EXTRACT:
- **movie_name**: The official title of the movie.
- **cast**: A list of all prominent actors/actresses mentioned.
- **genre**: A list of all genres mentioned (e.g., ["Sci-Fi", "Drama"]).
- **director**: The name of the director.
- **release_year**: The year the movie was released (as an integer, if available).
- **rating**: The IMDb or average rating (as a float).
- **language**: The primary language of the movie.
- **duration**: The runtime of the movie (e.g., "2h 49min").
- **plot_summary**: A concise summary of the paragraph in exactly ONE sentence (maximum 25 words).""",
        ),
        ("human", """Extract info from:{para}"""),
    ]
)

# -------------------- UI --------------------
st.title("🎬 Movie Information Extractor")
st.caption(
    "Paste any movie description and the AI will convert it into structured data."
)

# User input
para = st.text_area(
    "Enter Movie Paragraph",
    height=200,
    placeholder="Type or paste the movie description here...",
)

# -------------------- BUTTON & LOGIC --------------------
if st.button("Extract Data"):
    if not para.strip():
        st.warning("Please enter a paragraph first.")
    else:
        with st.spinner("Analyzing movie..."):
            try:
                # Create final prompt
                final_prompt = prompt.invoke({"para": para})

                # Get response
                response = model.invoke(final_prompt)

                # Display the structured output
                st.subheader("📊 Extracted Information")
                st.code(response.content, language="json")

            except Exception as e:
                st.error("Failed to process the paragraph. Please try again.")
                st.exception(e)


# st.button
# st.text_area(height,placeholder)
# st.spinner
# st.subheader,st.code(language)
# """
# Great question! Here is exactly what `if not para.strip():` means, broken down simply:

# ---

# ### 🧠 The Breakdown:

# 1. **`para`**: This is the text the user typed in the box (your input).
# 2. **`.strip()`**: This is a Python method that **removes all the empty spaces** from the beginning and the end of the text. (It doesn't remove spaces from the middle).
#    - Example: `"   Hello World   "` becomes `"Hello World"`.
#    - Example: `"   "` (just spaces) becomes `""` (completely empty).
# 3. **`not`**: This flips the result.
#    - If the text is **empty** (`""`), `not` makes it **`True`**.
#    - If the text is **not empty** (like `"Hello"`), `not` makes it **`False`**.

# ---

# ### 💡 Why is this used?
# It checks if the user has **really** typed something, or if they just pressed the spacebar multiple times.
# """
