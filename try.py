# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="georgesung/llama2_7b_chat_uncensored")