from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
completion = client.completions.create(model="/data/private/data/for_ln/huggingface/hub/models--Qwen--Qwen2-VL-2B-Instruct-AWQ/snapshots/4f6ea6d22fcf0f8c1ed64d1d2a3d722d4d7bbcea/",
                                    prompt="San Francisco is a")
print("Completion result:", completion)