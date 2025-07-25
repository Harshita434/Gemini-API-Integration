import google.generativeai as genai
from google.generativeai import GenerativeModel
from serpapi import GoogleSearch
genai.configure(api_key="AIzaSyC-OvPAikdVBWmakdhJRjXUMJzUZa-01GM")
model= GenerativeModel('gemini-2.5-pro')
serpapi_key = "323a1c9aa808f8cc4d9291bf5c98ab48b5e38186dc5f74af72fee41ace2ff7cc"
def google_search(query):
    param={
        "q":query,
        "hl":"en",
        "api_key": serpapi_key
    }
    search = GoogleSearch(param)
    results = search.get_dict()
    if "organic_results" in results:
        return "\n" .join ([res["snippet"] for res in results["organic_results"][:5]])
    return "No result found"
def chat_with_gemini(query):
    search_result = google_search(query)
    prompt=f""" I searched google for "{query}" and found the following information:
    {search_result}
    
    Based on this, please give me a concise and to the point answer."""
    response = model.generate_content(prompt)
    return response.text
user = input("prompt: ")
print(chat_with_gemini(user))