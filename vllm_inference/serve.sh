# vllm serve shell command

uv run vllm serve \
    /data/private/data/for_ln/huggingface/hub/models--Qwen--Qwen2-VL-2B-Instruct-AWQ/snapshots/4f6ea6d22fcf0f8c1ed64d1d2a3d722d4d7bbcea/ \
    --port 8000 \
    --host 0.0.0.0 >> serve.log 2>&1