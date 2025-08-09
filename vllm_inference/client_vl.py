# uv run python vllm_inference/client_vl.py
from openai import OpenAI
import base64

# Path to your local image
image_path = "t.png"
page_path = "이미지.png"

# Read and base64-encode your image
def img2base64(image_path):
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")
    return image_b64

image_b64 = img2base64(image_path)
page_b64 = img2base64(page_path)

# Set up OpenAI client for vLLM
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# Compose the vision-language message
completion = client.chat.completions.create(
    model="/data/private/data/for_ln/huggingface/hub/models--Qwen--Qwen2-VL-2B-Instruct-AWQ/snapshots/4f6ea6d22fcf0f8c1ed64d1d2a3d722d4d7bbcea/",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Choose class between ['Text', 'Title', 'Picture'] for this image. image:"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
                {"type": "text", "text": "whole page:"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{page_b64}"}},
            ]
        }
    ],
    max_tokens=20,
)

print("Completion result:", completion.choices[0].message.content)