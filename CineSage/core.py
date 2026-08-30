from dotenv import load_dotenv

load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model="mistral-small-2603", max_tokens=15)

# prompt is runnable-jisko run and invoke kar skte ho
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

para = input("Give me your paragraph: ")

final_prompt = prompt.invoke({"paragraph": para})
"""
response = model.invoke(
    "1. earth dying dust storms food running out nobody cares about science anymore.2. old pilot matt mcconaughey gets recruited secretly by nasa to fly through a wormhole near saturn.3. he leaves his little daughter murph behind crying saying the ghost in her room is actually him.4. he lands on water planet where 1 hour equals 7 years on earth his daughter grows up to be jessica chastain.5. he falls into a black hole ends up inside a 5d bookshelf talking to her through gravity time love is the 5th dimension they save humanity the end (sort of) Can you provide me summaryand info of movie "
)
"""
response = model.invoke(final_prompt)

print(response.content)


# https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate
# hello pls create a good prompt template for my langchain product and that is extraction of useful information.i am going to give a paragraph like this: and i want to extract useful info like cast,movie_name,genre etc think yourself what else is needed and also generate a quick summaryof paragraph
# Prompt Template.from_template if not chatbot
# """    """:multiple lines ke liye
# {paragraph}:placeholder for para
# hum from langchain_core.messages ka use ni kar rahe AIMessage,SystemMessage,HumanMessage kyunki hum prompts ka use kr rhe yhi roles defined h
# prompt.invoke and add dict in it of placeholders
# now create proper streamlit Ui and dont add any other functionality
