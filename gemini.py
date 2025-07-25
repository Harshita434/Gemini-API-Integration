import google.generativeai as genai
from google.generativeai import GenerativeModel
genai.configure(api_key="AIzaSyC-OvPAikdVBWmakdhJRjXUMJzUZa-01GM")
model= GenerativeModel('gemini-2.5-pro')
chat_history = []

while True:
    q= input("You: ")
    chat_history.append(f"user:{q}")
    prompt= "\n".join(chat_history) + "\nAI:"
    response = model.generate_content(prompt)
    chat_history.append(f"AI: {response.text}")
    print(f"AI: {response.text}")
    if q.lower() == "exit":
        break
    print(chat_history)