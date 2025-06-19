    model="mistralai/Mistral-7B-Instruct-v0.2",
        task="conversational",
        provider="hf-inference",
        huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    )