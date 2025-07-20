#  Data Science  Chatbot

A simple chatbot built with Hugging Face Transformers and FastAPI that answers questions related to Data Science, AI, and Machine Learning using a pre-trained language model (like GPT-2).

##  Features

- Generate text-based answers to your questions
- Powered by Hugging Face `transformers` pipeline
- Built with `FastAPI` + `Uvicorn` for fast backend API
- Easy to run locally

##  Model

The default model used is [`distilgpt2`](https://huggingface.co/distilgpt2), a lighter and faster version of GPT-2. You can easily change it to a more powerful model like `gpt2`, `gpt2-medium`, or any custom model from Hugging Face Hub.

##  Requirements

Make sure you have Python 3.8+ installed. Then install the dependencies:

```bash
pip install -r requirements.txt
