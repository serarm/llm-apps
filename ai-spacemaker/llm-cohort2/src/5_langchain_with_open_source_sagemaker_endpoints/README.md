# Week 3: Tuesday Session

In today's assignment, we'll be creating an Open Source LLM-powered LangChain RAG Application.

There are 3 main sections to this assignment:

## Build 🏗️

### Build Task 1: Deploy LLM and Embedding Model to SageMaker Endpoint Through Hugging Face

Select "Inference Endpoint" from the "Solutions" button in Hugging Face:

![image](https://i.imgur.com/6KC9TCD.png)

Create a "+ New Endpoint" from the Inference Endpoints dashboard.

![image](https://i.imgur.com/G6Bq9KC.png)

Select the `meta-llama/Llama-2-7b-chat-hf` model repository and name your endpoint. Select N. Virginia as your region (`us-east-1`). Give your endpoint an appropriate name.

Select the following settings for your `Advanced Configuration`.

![image](https://i.imgur.com/c0HQ7g1.png)

Create a `Protected` endpoint.

![image](https://i.imgur.com/Ak8kchZ.png)

If you were successful, you should see the following screen:

![image](https://i.imgur.com/IBYG3wm.png)

> #### NOTE: PLEASE SHUTDOWN YOUR INSTANCES WHEN YOU HAVE COMPLETED THE ASSIGNMENT TO PREVENT UNESSECARY CHARGES.

### Terminating Your Resources

Please head to the settings of each endpoint and select `Delete Endpoint`. You will need to type the name of the endpoint to delete the resources.

### Build Task 2: 

Following the provided notebook - you'll build an open-source LLM-powered Retrieval Augmented Generation Application using:

- LangChain
- [Meta's Llama 2](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)
- [Sentence Transformers All MPNET Base V2 Embedding Model](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)

This will take you through three major steps: 

1. Creating a CustomLLM to interface with your SageMaker endpoints.
2. Constructing a typical RAG application.

### Deliverables

- Completed Notebook
- Screenshot of endpoint usage

Example Screen Shot:

![image](https://i.imgur.com/qfbcVpS.png)

## Ship 🚢

Create a Hugging Face Space powered by a SageMaker Endpoint!

### Deliverables

- A short Loom of the space, and a 1min. walkthrough of the application in full

## Share 🚀

Make a social media post about your final application!

### Deliverables

- Make a post on any social media platform about what you built!

Here's a template to get you started:

```
🚀 Exciting News! 🚀

I am thrilled to announce that I have just built and shipped a open-source LLM-powered Retrieval Augmented Generation Application with LangChain! 🎉🤖

🔍 Three Key Takeaways:
1️⃣ 
2️⃣ 
3️⃣ 

Let's continue pushing the boundaries of what's possible in the world of AI and question-answering. Here's to many more innovations! 🚀
Shout out to @AIMakerspace !

#LangChain #QuestionAnswering #RetrievalAugmented #Innovation #AI #TechMilestone

Feel free to reach out if you're curious or would like to collaborate on similar projects! 🤝🔥
```

> #### NOTE: PLEASE SHUTDOWN YOUR INSTANCES WHEN YOU HAVE COMPLETED THE ASSIGNMENT TO PREVENT UNESSECARY CHARGES.
