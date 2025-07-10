import base64
from openai import OpenAI


client = OpenAI(base_url="http://localhost:8000/v1", api_key="not-needed")

with open("image.png", "rb") as image_file:
    b64_image = base64.b64encode(image_file.read()).decode("utf-8")

response = client.chat.completions.create(
    model="Qwen2.5-VL-3B-Instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{b64_image}"
                    }
                },
                {
                    "type": "text",
                    "text": "请用中文描述这张图片"
                }
            ]
        }
    ],
    stream=True
)
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

