import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",

    # Insert your AIML API Key in the quotation marks instead of <YOUR_API_KEY>.
    api_key="83e289d30aaf406cafb1dafdd72c8050",  
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant who create cringy pick up lines new everytime when start is told, nothing is in response other than the pickup line",
        },
        {
            "role": "user",
            "content": "start"
        },
    ],
)

message = response.choices[0].message.content

print(f"Assistant: {message}")
