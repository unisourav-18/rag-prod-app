# # from openai import OpenAI
# import google.generativeai as genai
# from llama_index.readers.file import PDFReader
# from llama_index.core.node_parser import SentenceSplitter
# from dotenv import load_dotenv
# import os

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# EMBED_MODEL = "text-embedding-004"
# EMBED_DIM = 768
# splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

# def load_and_chunk_pdf(path: str):
#     docs = PDFReader().load_data(file=path)
#     texts = [d.text for d in docs if getattr(d, "text", None)]
#     chunks = []
#     for t in texts:
#         chunks.extend(splitter.split_text(t))
#     return chunks


# def embed_texts(texts: list[str], task_type: str = "retrieval_document") -> list[list[float]]:
#     embeddings = []
#     for text in texts:
#         result = genai.embed_content(
#             model=EMBED_MODEL,
#             content=text,
#             task_type=task_type
#         )
#         embeddings.append(result["embedding"])
#     return embeddings


from google import genai
from google.genai import types
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

EMBED_MODEL = "models/gemini-embedding-001"
EMBED_DIM = 3072  # gemini-embedding-001 outputs 3072 dims

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)


def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks


def embed_texts(texts: list[str], task_type: str = "RETRIEVAL_DOCUMENT") -> list[list[float]]:
    embeddings = []
    for text in texts:
        result = client.models.embed_content(
            model=EMBED_MODEL,
            contents=text,
            config=types.EmbedContentConfig(task_type=task_type)
        )
        embeddings.append(result.embeddings[0].values)
    return embeddings