# SIMPLE CHATGPT CONTAINERISE  ON HUGGING FACE

Basic RAG application in python

## Docker command to build the app

```bash
docker  build -t serarm1/llmops-aispacemaker:rag_pure_python -f src/2_rag_pure_python/Dockerfile .
docker push serarm1/llmops-aispacemaker:rag_pure_python
 docker run -p 7860:7860 -e OPENAI_API_KEY=sk-... -e WANDB_API_KEY=<wandb key> serarm1/llmops-aispacemaker:rag_pure_python
```

[Hugging Face App: RAG IN PURE PYTHON](https://huggingface.co/spaces/Serjesh/rag_pure_python)