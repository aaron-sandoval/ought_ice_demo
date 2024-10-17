# %%
import os
from pathlib import Path

from ice.recipe import recipe
from fvalues import F

REPO_DIR = Path(__file__).parent

# %%
# Hello world
async def say_hello():
    hola = await say_hola()
    return f"Hello world! {hola}"

async def say_hola():
    return "Hola mundo!"

# recipe.main(say_hello)
# %%
# Q&A
def make_qa_prompt(question: str) -> str:
    return F(
        f"""Answer the following question:

    Question: "{question}"
    Answer: "
    """
    ).strip()


async def answer(question: str = "What is happening on 9/9/2022?"):
    prompt = make_qa_prompt(question)
    answer = await recipe.agent().complete(prompt=prompt, stop='"')
    return answer

recipe.main(answer)
# %%
