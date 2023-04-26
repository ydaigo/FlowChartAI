from langchain import PromptTemplate, OpenAI, LLMChain

from core import prompt_template


def create_flow_chart(text):
    llm = OpenAI(temperature=0)
    prompt = PromptTemplate(
        input_variables=["input"],
        template=prompt_template.mermaid_template,
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    mermaid = chain.run(input=text)
    mermaid = mermaid.replace("・", " - ")
    return mermaid
