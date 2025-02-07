from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

conversation_history = []

def get_bot_response(user_text: str) -> str:
    model_engine = "gpt-3.5-turbo"

    # Initialize conversation history with a system message
    if len(conversation_history) == 0:
        conversation_history.append({
            "role": "system",
            "content": "You are a helpful assistant specialized in helping developers and newbies with programming-related questions."
        })

    # Append user input to conversation history
    conversation_history.append({"role": "user", "content": user_text})

    # Get the bot response from the OpenAI model
    response = client.chat.completions.create(
        model=model_engine,
        messages=conversation_history,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.9
    )

    # Extract and append the assistant's response
    ai_response = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": ai_response})

    return ai_response
