from openai import OpenAI
# from  base.settings import BASE_DIR
import os

def get_pickup_line():
    client = OpenAI(
        base_url="https://api.aimlapi.com/v1",

        api_key="83e289d30aaf406cafb1dafdd72c8050",  
    )
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant who create cringy pick up lines new everytime when start is told, nothing is in response other than the pickup line, Also give emojees at the end",
            },
            {
                "role": "user",
                "content": "start"
            },
        ],
    )

    message = response.choices[0].message.content
    print(message)
    return message