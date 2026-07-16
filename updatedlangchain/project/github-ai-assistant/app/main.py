from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

from app.config import GROQ_API_KEY
load_dotenv()


model = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq",
)

response = model.invoke(
    "Introduce yourself in one sentence."
)

print(type(response))
print(response.content)