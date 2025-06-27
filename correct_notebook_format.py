import nbformat

file = "5-sms-spam-classifier\Copy_of_fcc_sms_text_classification.ipynb"
with open(file , encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

nb.metadata.pop('widgets', None)

with open(file, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
