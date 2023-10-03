# SIMPLE CHATGPT CONTAINERISE  ON HUGGING FACE

Build, containerize, and deploy your first LLM application with Chainlit, Docker, Hugging Face and OpenAI

## Docker command to build the app

```bash
docker  build . -t serarm1/llmops-aispacemaker:simple-chainlit-app
docker push docker.io/serarm1/llmops-aispacemaker:simple-chainlit-app
docker run -p 7860:7860 -e OPENAI_API_KEY=<OPEN_API_KEY> docker.io/serarm1/llmops-aispacemaker:simple-chainlit-app
```

[Hugging Face App: SIMPLE CHAINLIT APP](https://huggingface.co/spaces/Serjesh/simple_chainlit_app)