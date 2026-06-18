from openai import OpenAI
from init import settings

llm = OpenAI(base_url=str(settings.llm_base_url), api_key="example")

response = llm.chat.completions.create(
    model=settings.llm_model, messages=[{"role": "user", "content": "tell me a joke"}]
)

print(response.choices[0].message.content)
