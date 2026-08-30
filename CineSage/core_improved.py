from dotenv import load_dotenv

load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

# lets make schema also having optional
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


# SCHEMA CREATED
# class ke andar another class inherit karunga toh its pydantic schema-BaseModel
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    # movie can be science fiction+comedy-multiple genre
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


# PYDANTIC PARSER
parser = PydanticOutputParser(pydantic_object=Movie)

model = ChatMistralAI(model="mistral-small-2603", max_tokens=15)

# prompt is runnable-jisko run and invoke kar skte ho
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """Extract movie information from the paragraph {format_instructions}""",
        ),
        ("human", """{paragraph}"""),
    ]
)

para = input("Give me a paragraph:")

final_prompt = prompt.invoke(
    {"format_instructions": parser.get_format_instructions(), "paragraph": para}
)
# Raw model output
response = model.invoke(final_prompt)
# structured output
# structure form mai karne ke liye parser.parse
movie_data = parser.parse(response.content)

print(movie_data)

#  2004 Bollywood action thriller dhoom
# ```json
# {
#   "title": "Dhoom"
# }
