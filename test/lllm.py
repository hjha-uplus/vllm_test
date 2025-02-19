import litellm 


inference_server_url = "http://localhost:8000/v1"
messages = [
    {
        "role": "user",
        "content": "what llm are you"
    }
]

custom_llm_provider = "hosted_vllm"
model_name = "Qwen/Qwen2-VL-2B-Instruct"

response = litellm.completion(
            model=f"{custom_llm_provider}/{model_name}", # pass the vllm model name
            messages=messages,
            api_base=inference_server_url,
            temperature=0.2,
            max_tokens=80)

print(response)

