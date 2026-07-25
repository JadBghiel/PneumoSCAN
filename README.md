# PneumoSCAN

A machine-learning project exploring both **supervised** and **unsupervised** learning
on medical data. It combines an image-classification pipeline that detects pneumonia
from chest X-ray imagery with an unsupervised clustering study over free-text symptom
descriptions.

The work is organized as two self-contained Jupyter notebooks, each documented inline
with explanations, visualizations, and model comparisons.

---

## Overview

| Part | Task | Approach |
|------|------|----------|
| **Supervised**   | Classify chest X-ray images (normal vs. pneumonia) | Multiple classification models trained and compared on the same dataset |
| **Unsupervised** | Group free-text symptom reports into clusters | Text vectorization + K-Means clustering, with cluster-count justification |

## Repository layout

```
.
├── Supervised/
│   └── image_classification_pneumonia&blood.ipynb   image classification models
├── Unsupervised/
│   └── Unsupervised_first.ipynb                      text clustering study
├── extract_dataset.py        unpacks .npy image/label arrays into per-class PNG folders
├── clean_student_dataset.py  normalizes the raw symptom-text CSV
└── rsrc/                      datasets (student symptom CSVs, Iris reference set)
```

## Supervised — pneumonia detection

The supervised notebook trains and compares several classification models on the same
chest X-ray dataset, then discusses model selection: not only accuracy but also the
loss function, training/inference speed, and the trade-offs behind the chosen model.
It provides medical context on the condition being detected and situates the results
against published work on the same problem.

`extract_dataset.py` prepares the image data — it loads `train_images.npy` /
`train_labels.npy`, maps labels to class names (`normal`, `pneumonia`), and writes the
images out as PNGs into per-class folders suitable for image-classification pipelines.

## Unsupervised — symptom clustering

The unsupervised notebook groups free-text symptom descriptions into clusters using text
vectorization and K-Means. It measures cluster quality (e.g. silhouette score) to justify
the number of clusters rather than picking one arbitrarily, presents the improvements made
during experimentation, and tests the clustering by assigning unseen reports to the
learned clusters.

`clean_student_dataset.py` preprocesses the raw symptom CSV (`rsrc/Student_Dataset.csv`)
into a cleaned version (`rsrc/Student_Dataset_Clean.csv`) by stripping placeholder tokens
and normalizing each row.

## Getting started

The project uses the standard Python data-science stack.

```bash
pip install numpy pandas pillow scikit-learn matplotlib jupyter

# prepare data (supervised part, expects the .npy arrays under dataset/)
python extract_dataset.py

# clean the symptom text data (unsupervised part)
python clean_student_dataset.py

# then open the notebooks
jupyter notebook
```

Open the notebook for the part you want to explore:
- `Supervised/image_classification_pneumonia&blood.ipynb`
- `Unsupervised/Unsupervised_first.ipynb`

## Project context

Developed as part of the EPITECH curriculum (second year). The goal is to demonstrate a
full workflow for both learning paradigms: data preparation, model training and
comparison, quantitative evaluation, and interpretation of the results in the context of
the underlying medical problem.
