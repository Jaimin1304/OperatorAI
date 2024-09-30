import os
import httpx
import base64
from openai import OpenAI
from dotenv import load_dotenv


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to image
image_path = "F:\codebase\OperatorAI\screenshots\screenshot_20240916-175756.jpg"
# Getting the base64 string
base64_image = encode_image(image_path)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
proxy_url = os.environ.get("OPENAI_PROXY_URL")

print(api_key)
print(proxy_url)

client = (
    OpenAI(api_key=api_key)
    if proxy_url is None or proxy_url == ""
    else OpenAI(api_key=api_key, http_client=httpx.Client(proxy=proxy_url))
)


def chat_openai(system_content, user_content, base64_image=None):
    messages = [
        {
            "role": "system",
            "content": system_content,
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": user_content}],
        },
    ]

    if base64_image:
        messages[1]["content"].append(
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            }
        )

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    return completion


def run():
    completion = chat_openai(
        system_content="You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        user_content="Explain what is in the image",
        base64_image=base64_image,
    )
    print(completion.choices[0].message.content)


if __name__ == "__main__":
    run()
