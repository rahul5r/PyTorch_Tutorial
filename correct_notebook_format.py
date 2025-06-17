import nbformat

with open("18. GPT2 FineTuning (Text Generation).ipynb" , encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

nb.metadata.pop('widgets', None)

with open("18. GPT2 FineTuning (Text Generation).ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
