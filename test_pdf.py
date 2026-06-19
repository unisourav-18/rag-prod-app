from data_loader import load_and_chunk_pdf

path = r"C:\Users\theso\Downloads\dmh-developer-trial-task.pdf"

print("Testing:", path)

chunks = load_and_chunk_pdf(path)

print("Chunks:", len(chunks))