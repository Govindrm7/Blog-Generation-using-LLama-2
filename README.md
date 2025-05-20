# Blog-Generation-using-LLama-2
This GitHub repository provides a comprehensive, step-by-step guide for building a blog generation application leveraging Meta’s open-source LLaMA 2 large language model, integrated with LangChain for orchestration and Streamlit for the web-based user interface.

Use Case – This project is designed to offer users a convenient, high-quality, and supportive tool for generating blog content, allowing them to dedicate more time to other aspects of blog management. Additionally, the application serves as a source of inspiration, fostering creativity and enabling content customization.

Topics covered: Generative AI, LLama2, LangChain, Streamlit, Python, HuggingFace, conda virtual enviroments, App Deployment

If you like this project, please follow my Github account, or click on the 'star' icon for the repo!

## 🖼️ Application Screenshot

![App Screenshot](<img width="1348" alt="Screenshot 2025-05-20 at 12 07 35 PM" src="https://github.com/user-attachments/assets/40dd4b94-416b-4af1-b20b-cb1bb202ec83" />
)
## Getting Started

Here’s a more technical, professional, and straightforward version of your sentence:

hese instructions will help you set up the project on your local machine for development and testing. For details on deploying the project to a live environment, refer to the deployment section.


### Installing

Please fork the repo for your local development and testing.

### Prerequisites

To install the conda virtual environment for the project, run the following commands;

```
conda create -p venv python==3.9 --y
conda activate venv
```
Run the following command to install requirements and dependencies for the project.

```
pip install -r requirements.txt
```

## Running the Application

Run the following command to run the application on your local webpage.

```
streamlit run app.py
```

## Deployment

Additionally, you can deploy your Streamlit app on Streamlit Community Cloud by clicking on the Deploy button on the top right corner of your local running application.

## Built With

* [LLaMA 2: Open Foundation and Fine-Tuned Chat Models](https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/) – The official research publication by Meta introducing LLaMA 2, an open large language model series designed for both foundational and chat-based tasks.

* [LLaMA 2 GGML Model (HuggingFace)](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML?source=post_page-----fcb0a3c55278--------------------------------) – A quantized version of the LLaMA 2 7B Chat model hosted on HuggingFace, optimized for local CPU/GPU inference.

* [LangChain + CTransformers Integration](https://python.langchain.com/docs/integrations/providers/ctransformers/) – Enables seamless use of GGML models within LangChain through the `ctransformers` provider.


## Version of the Deployed App

