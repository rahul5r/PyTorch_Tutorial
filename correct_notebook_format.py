import nbformat

with open("16. Fine Tuning of T5 Transformer (Text Summarization).ipynb" , encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

nb.metadata.pop('widgets', None)

with open("your_notebook_clean.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
