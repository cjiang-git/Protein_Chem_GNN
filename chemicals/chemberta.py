from transformers import AutoTokenizer, AutoModel
import torch
import pandas as pd

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")
model = AutoModel.from_pretrained("seyonec/ChemBERTa-zinc-base-v1").to(device)

def embed_smile(smile, model):
    inputs = tokenizer(smile, return_tensors="pt", padding=True, truncation=True, max_length=180).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)  # Averaging over token embeddings
    return embeddings

df_chemicals = pd.read_csv("/content/drive/MyDrive/cs224w/chemicals.v5.0.filtered.tsv", sep = "\t", header = None)

smiles = df_chemicals[3]
chunks = [smiles[x:x+100].to_list() for x in range(0, len(smiles), 100)]
for i, chunk in enumerate(chunks):
  embeddings = embed_smile(chunk, model)
  torch.save(embeddings, f"/content/drive/MyDrive/cs224w/chemical_embeddings/chunk_{i}.pt")


