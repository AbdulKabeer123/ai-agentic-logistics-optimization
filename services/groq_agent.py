import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def agent_decision(vehicles_data):

    prompt = f"""
    Here is the current fleet status:
    {vehicles_data}

    Which vehicle should be prioritized and why?
    Is rerouting needed?

    Respond in 2-3 short professional sentences.
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3,
                "max_tokens": 150
            },
            timeout=20
        )

        if response.status_code != 200:
            print("Groq API Error:", response.text)
            return "⚠️ Groq API error. Unable to generate recommendation."

        content = response.json()["choices"][0]["message"]["content"].strip()

        return content

    except Exception as e:
        print("Connection Error:", e)
        return "⚠️ Connection failed. Unable to contact Groq API."