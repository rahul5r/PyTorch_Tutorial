import nbformat

with open("15. HuggingFace Ecosystem.ipynb" , encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

nb.metadata.pop('widgets', None)

with open("your_notebook_clean.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
