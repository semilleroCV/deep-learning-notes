# deep-learning-notes


<p align="center">
<img src="./assets/logo.png" alt="Deep Learning Notes" width="1600">
<p align="center">


Welcome to the Deep Learning Notes repository! This repository serves as a comprehensive resource for deep learning enthusiasts, providing detailed notebooks, modular implementations, and in-depth analyses related to various aspects of deep learning. Below is the structure and a brief description of each directory within the repository:

## Project Organization

```
├── assets             <- Static files like images and badges.
│
├── automation
│   │
│   └── autogenerate_notebooks_table.py Script that performs the update of the main readme based on
│        notebooks-table-data.csv
│
├── core <- Common utility functions used across notebooks.
│    │
│    ├── __init__.py   <- Makes core a Python module
│    │
│    └── utils.py      <- Useful functions
│
├── notebooks          <- Jupyter notebooks. Naming convention is a short `-` delimited description,
│   │                    e.g. `cross-entropy-loss`.
│   │
│   ├── architectures  <- Implementations of architectures, e.g. UNET.
│   │
│   ├── losses         <- Examples of loss functions, e.g. NLLLoss.
│   │
│   ├── metrics        <- Demonstrations of metrics, e.g. IoU
│   │
│   ├── modules        <- Implementations of a module, e.g. Xception module.
│   │
│   └── data_exploration    <- Exploration of a dataset, e.g. MNIST.
│
├── papers             <- Markdown articles about important deep learning papers.
│
├── CONTRIBUTING.md    <- How to contribute to the project.
│
├── LICENSE            <- Open-source license (MIT)
│
└── README.md          <- Overview of the repository.
```

<!--- AUTOGENERATED-NOTEBOOKS-TABLE -->
<!---
   WARNING: DO NOT EDIT THIS TABLE MANUALLY. IT IS AUTOMATICALLY GENERATED.
   HEAD OVER TO CONTRIBUTING.MD FOR MORE DETAILS ON HOW TO MAKE CHANGES PROPERLY.
-->
## 🏗️ Architectures (7 notebooks)
| **notebook** | **open in colab** | **repository / paper** |
|:------------:|:-----------------:|:----------------------:|
| [Network In Network](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/network-in-network.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/network-in-network.ipynb) |  [![arXiv](https://img.shields.io/badge/arXiv-1312.4400-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/1312.4400) |
| [Xception](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/xception.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/xception.ipynb) |  [![arXiv](https://img.shields.io/badge/arXiv-1610.02357v3-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/1610.02357v3) |
| [U-Net](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/unet.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/unet.ipynb) |  [![arXiv](https://img.shields.io/badge/arXiv-1505.04597-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/1505.04597) |
| [DenseNet](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/densenet.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/densenet.ipynb) |  [![arXiv](https://img.shields.io/badge/arXiv-1608.06993v5-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/1608.06993v5) |
| [Mobilenet V1](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/mobilenetv1.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/mobilenetv1.ipynb) |  [![arXiv](https://img.shields.io/badge/arXiv-1704.04861-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/1704.04861) |
| [Inception V1](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/inceptionv1.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/inceptionv1.ipynb) |  [![arXiv](https://img.shields.io/badge/arXiv-1409.4842-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/1409.4842) |
| [MLP Mixer](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/mlp-mixer.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/architectures/mlp-mixer.ipynb) |  [![arXiv](https://img.shields.io/badge/arXiv-2105.01601-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2105.01601) |
## ❌ Loss Functions (2 notebooks)
| **notebook** | **open in colab** | **repository / paper** |
|:------------:|:-----------------:|:----------------------:|
| [Focal Loss](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/losses/focal-loss.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/losses/focal-loss.ipynb) | [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/facebookresearch/Detectron) [![arXiv](https://img.shields.io/badge/arXiv-1708.02002-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/1708.02002) |
| [CELoss vs NLLLoss](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/losses/celoss-vs-nllloss.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/losses/celoss-vs-nllloss.ipynb) |   |
## 📏 Metrics (1 notebooks)
| **notebook** | **open in colab** | **repository / paper** |
|:------------:|:-----------------:|:----------------------:|
| [Intersection Over Union (IoU)](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/metrics/intersection-over-union.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/metrics/intersection-over-union.ipynb) |  [![arXiv](https://img.shields.io/badge/arXiv-1902.09630-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/1902.09630) |
## 🧩 Modules (1 notebooks)
| **notebook** | **open in colab** | **repository / paper** |
|:------------:|:-----------------:|:----------------------:|
| [Pixel Shuffle](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/modules/pixel-shuffle.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/modules/pixel-shuffle.ipynb) |  [![arXiv](https://img.shields.io/badge/arXiv-1609.05158-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/1609.05158) |
## 🔍 Data Exploration (1 notebooks)
| **notebook** | **open in colab** | **repository / paper** |
|:------------:|:-----------------:|:----------------------:|
| [GloVe Word Embeddings](https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks/data_exploration/glove-word-embeddings.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/semilleroCV/deep-learning-notes/blob/main/notebooks/data_exploration/glove-word-embeddings.ipynb) | [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/stanfordnlp/GloVe) [![NLP Stanford](https://img.shields.io/badge/NLP%20Stanford-white.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MDAiIGhlaWdodD0iNDAwIj48ZyBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxwYXRoIGZpbGw9IiM4NDA0ODQiIGQ9Ik0wIDMwNi4zNzdWNDAwaDM3LjJsLjA2Ni00My45Yy4wNDQtMjkuMjgyLjE2My00MC4zNy4zNTctMzMuMy40MTkgMTUuMjgzLS43MTkgMTQuMTI1IDE0LjE1OCAxNC40bDEwLjgxOS4yLjIgMjMuNGMuMTUzIDE3LjkwOC4zMiAyMy42MDkuNzA5IDI0LjI5MSAxLjAyNyAxLjc5NiAxLjcxMSAxLjkwMiAxMy4xOTEgMi4wNDJsMTAuOS4xMzRWNDAwaDQ5LjYxbC0uMTA1LTkyLjExOGMtLjExNy0xMDIuMjMzLjExNi05My44MTMtMi42MS05NC41NzYtMi42MjMtLjczMy00My40NTctLjM1NC00NC42MzEuNDE1LTIuMTM1IDEuNC0yLjA1LS41MjQtMi4yNTIgNTAuODc5LS4xMDQgMjYuNC0uMjg0IDQzLjEzMi0uNCAzNy4xODEtLjI5Mi0xNC44OTUuODQzLTEzLjc3OC0xNC4zMTItMTQuMDgzbC0xMC41LS4yMS0uMDExLTIwLjA0NGMtLjAxMi0yMS45NTQtLjI4NS0yNy4xMTgtMS41LTI4LjMzMy0xLjAxOS0xLjAxOS01Ljk5MS0xLjQ4Ni0xNS45NTYtMS41bC03LjY2Ni0uMDExLS4xMzQtMTAuOWMtLjE0LTExLjQ4LS4yNDYtMTIuMTY0LTIuMDQyLTEzLjE5MS0uNjczLS4zODUtNS4wNjktLjUzOS0xNy45OTEtLjYzMkwwIDIxMi43NTN2OTMuNjI0bTE2Ni4yNzMtOTMuMTk4Yy0xLjk3OC4zOTQtMi42ODkgMS4xNDYtMy4xMDIgMy4yODItLjE4NS45NTYtLjM0NCA0Mi42NDQtLjM1NCA5Mi42MzlMMTYyLjggNDAwaDEyNC40NDdsLS4xMjQtMTcuMWMtLjEzLTE4LjA4NS0uMTU1LTE4LjMxOC0yLjAzMi0xOS4zOTEtLjY5OS0uMzk5LTguNjI0LS41MzMtMzYuNzc5LS42MjFsLTM1Ljg4Ny0uMTEyLS4xMTMtNzMuMDg4Yy0uMTItNzguMzU5LS4wMTEtNzQuNTQ4LTIuMTc2LTc1Ljk2Ny0xLjE4LS43NzQtNDAuMjcyLTEuMjU3LTQzLjg2My0uNTQybTEyNC45NzkuMDE2Yy0zLjg0OS45MjMtMy41OTgtNS44NDgtMy42MjcgOTcuNzA1TDI4Ny42IDQwMGg0OS41OTVsLjEwMy0zMS4zLjEwMi0zMS4zIDIzLjQtLjJjMTcuOTA4LS4xNTMgMjMuNjA5LS4zMiAyNC4yOTEtLjcwOSAxLjc5Ni0xLjAyNyAxLjkwMi0xLjcxMSAyLjA0Mi0xMy4xOTFsLjEzNC0xMC45SDQwMHYtNzQuOGgtMTIuNzMzbC0uMTM0LTEwLjljLS4xNC0xMS40OC0uMjQ2LTEyLjE2NC0yLjA0Mi0xMy4xOTEtMS4wMzEtLjU4OS05MS40MzEtLjg5MS05My44MzktLjMxNE0zNjIuOCAyNzV2MTIuNmgtMjUuNnYtMjUuMmgyNS42VjI3NSIvPjxwYXRoIGZpbGw9IiNmZTAwMDEiIGQ9Ik0xOTQuNzE5IDEyLjc0MmMtNy40NjIuMzUxLTcuMDc1LS40NS03LjEwMiAxNC43MjVsLS4wMTcgMTAuMDY4LTExLjMuMTUxYy02LjIxNS4wODQtMTEuNjI5LjMwMy0xMi4wMzEuNDg4LTEuMjM5LjU2OS0xLjM5MiAxLjc0OS0xLjY5MSAxMy4xMDZsLS4yOSAxMS4wMDgtMTEuMDA4LjI5Yy0xMS4zNTcuMjk5LTEyLjUzNy40NTItMTMuMTA2IDEuNjkxLS4xODUuNDAyLS40MDQgNS44MDEtLjQ4NyAxMS45OTlsLS4xNTEgMTEuMjY4LTExLjI2OC4xNTFjLTYuMTk4LjA4My0xMS41OTcuMzAyLTExLjk5OS40ODctMS4yMzkuNTY5LTEuMzkyIDEuNzQ5LTEuNjkxIDEzLjEwNmwtLjI5IDExLjAwOC0xMS4wMDguMjljLTExLjM1Ny4yOTktMTIuNTM3LjQ1Mi0xMy4xMDYgMS42OTEtLjE4NS40MDItLjQwNCA1LjgwMS0uNDg3IDExLjk5OWwtLjE1MSAxMS4yNjgtMTEuMjY4LjE1MWMtNi4xOTguMDgzLTExLjU5Ny4zMDItMTEuOTk5LjQ4Ny0xLjIzOS41NjktMS4zOTIgMS43NDktMS42OTEgMTMuMTA2bC0uMjkgMTEuMDA4LTExLjAwOC4yOWMtMTEuOTMxLjMxNS0xMi43MDIuNDM4LTEzLjE2OSAyLjEwOC0uMTcxLjYxMy0uMzExIDExLjE0NC0uMzExIDIzLjQwM3YyMi4yODlsLjkxMS45MTEuOTExLjkxMWgyMi4yODljMTIuMjU5IDAgMjIuNzktLjE0IDIzLjQwMy0uMzExIDEuNjctLjQ2NyAxLjc5My0xLjIzOCAyLjEwOC0xMy4xNjlsLjI5LTExLjAwOCAxMS4wMDgtLjI5YzExLjM1Ny0uMjk5IDEyLjUzNy0uNDUyIDEzLjEwNi0xLjY5MS4xODUtLjQwMi40MDQtNS44MTYuNDg4LTEyLjAzMWwuMTUxLTExLjMgMTAuMDY4LS4wMTdjMTUuMTkzLS4wMjcgMTQuMzk1LjM2IDE0LjY2Ny03LjEwMmwuMi01LjQ4MS4yMzYgNS4zMjRjLjMzOCA3LjY0NS0uNzc0IDcuMDQ0IDEzLjMxOSA3LjIwOGwxMS4zMzQuMTMyLjI5MyAxMS4yNjVjLjE2MSA2LjE5NS40NiAxMS41NzcuNjY1IDExLjk1OC42OTQgMS4yOTcgMS43NTIgMS40MzggMTMuMDI0IDEuNzMxbDExLjI2NS4yOTMuMTMyIDExLjMwM2MuMTQ3IDEyLjU3Mi4yMTYgMTIuODg0IDIuODk0IDEzLjA3NC42ODEuMDQ4LTIuNDUyLjE5Ni02Ljk2Mi4zMy00LjUxLjEzMyA0LjIyLjE3OCAxOS40LjEgMjkuMDUzLS4xNDkgMzIuMDc5LS4yNDkgMzMuMjQ5LTEuMTA0IDEuMzU2LS45OTIgMS44NjMtNDQuNTYzLjU0Ni00Ny4wMjMtLjc0MS0xLjM4NS0xLjY2MS0xLjUxMi0xMy4wNjYtMS44MDlsLTExLjI2NS0uMjkzLS4xMzItMTEuMzM0Yy0uMTcyLTE0LjczIDEuNDUtMTMuMTE1LTEzLjM0My0xMy4yODhsLTExLjM4OS0uMTMydi0zLjUwM2MwLTEuOTI3LS4xMi03LjA4LS4yNjYtMTEuNDUyLS4zNDQtMTAuMjcyLjA0Ni05Ljc1NC03LjQxNi05Ljg0NGwtNS4zMTgtLjA2NSA1LS4yNjdjOC4xMDYtLjQzMyA3LjQ0Mi43MjggNy44MjItMTMuNjg0bC4yOS0xMS4wMDggMTEuMDA4LS4yOWMxNC40MTItLjM4IDEzLjI1MS4yODQgMTMuNjg0LTcuODIybC4yNjctNSAuMDY1IDUuMzE4Yy4wOSA3LjQ2Mi0uNDI4IDcuMDcyIDkuODQ0IDcuNDE2IDQuMzcyLjE0NiA5LjUyNS4yNjYgMTEuNDUyLjI2NmgzLjUwM2wuMTMyIDExLjM4OWMuMTczIDE0Ljc5My0xLjQ0MiAxMy4xNzEgMTMuMjg4IDEzLjM0M2wxMS4zMzQuMTMyLjI5MyAxMS4yNjVjLjE2MSA2LjE5NS40NiAxMS41NzcuNjY1IDExLjk1OC42OTQgMS4yOTcgMS43NTIgMS40MzggMTMuMDI0IDEuNzMxbDExLjI2NS4yOTMuMTMyIDExLjMzNGMuMTcyIDE0LjcyOC0xLjQ0MSAxMy4xMTUgMTMuMjg3IDEzLjI4N2wxMS4zMzQuMTMyLjI5MyAxMS4yNjVjLjI5MyAxMS4yNzIuNDM0IDEyLjMzIDEuNzMxIDEzLjAyNC4zODEuMjA1IDUuNzYzLjUwNCAxMS45NTguNjY1bDExLjI2NS4yOTMuMTMyIDExLjMwM2MuMTQ3IDEyLjU3MS4yMTQgMTIuODc2IDIuODk0IDEzLjA4MS42ODEuMDUyLTguMjEyLjE4OS0xOS43NjIuMzA1LTE4LjU5MS4xODctMTYuODI0LjIyIDE1LjQuMjkgNDguMTg1LjEwNSA1MC4yNTYtLjAxNyA1MC44NzgtMi45OTUuNTUyLTIuNjQ1LjM2OC00NC4xNjQtLjIwMS00NS4xODYtLjg0NS0xLjUxOS0xLjU2OS0xLjYyNi0xMy4xNDgtMS45MjdsLTExLjI2NS0uMjkzLS4xMzItMTEuMzM0Yy0uMTcyLTE0LjcyOCAxLjQ0MS0xMy4xMTUtMTMuMjg3LTEzLjI4N2wtMTEuMzM0LS4xMzItLjI5My0xMS4yNjVjLS4yOTMtMTEuMjcyLS40MzQtMTIuMzMtMS43MzEtMTMuMDI0LS4zODEtLjIwNS01Ljc2My0uNTA0LTExLjk1OC0uNjY1bC0xMS4yNjUtLjI5My0uMTMyLTExLjMzNGMtLjE3Mi0xNC43MjggMS40NDEtMTMuMTE1LTEzLjI4Ny0xMy4yODdsLTExLjMzNC0uMTMyLS4yOTMtMTEuMjY1Yy0uMTYxLTYuMTk1LS40Ni0xMS41NzctLjY2NS0xMS45NTgtLjY5NC0xLjI5Ny0xLjc1Mi0xLjQzOC0xMy4wMjQtMS43MzFsLTExLjI2NS0uMjkzLS4xMzItMTEuMzM0Yy0uMTcyLTE0LjcyOCAxLjQ0MS0xMy4xMTUtMTMuMjg3LTEzLjI4N2wtMTEuMzM0LS4xMzItLjI5My0xMS4yNjVjLS4yOTgtMTEuNDUzLS40MjEtMTIuMzIzLTEuODM5LTEzLjA4Mi0uOTQ0LS41MDUtMzIuMzI5LS44NDktNDAuODYtLjQ0N002LjEgMjEyLjY5OWMzLjQ2NS4wNjcgOS4xMzUuMDY3IDEyLjYgMCAzLjQ2NS0uMDY2LjYzLS4xMjEtNi4zLS4xMjFzLTkuNzY1LjA1NS02LjMuMTIxbTEwMCAwYzMuNDY1LjA2NyA5LjEzNS4wNjcgMTIuNiAwIDMuNDY1LS4wNjYuNjMtLjEyMS02LjMtLjEyMXMtOS43NjUuMDU1LTYuMy4xMjFtLTcyLjM3My40ODhjMS45MjkuMzc0IDIuNzEyIDEuMTU3IDMuMDg2IDMuMDg2bC4yOTUgMS41MjcuMDQ2LTEuNTE4Yy4wNjQtMi4wOTctMS4zMzktMy41LTMuNDM2LTMuNDM2bC0xLjUxOC4wNDYgMS41MjcuMjk1bTU1LjU4NS4wMjFjLS44NjQuMzQ4LTEuNjU4IDIuMTgtMS4xNiAyLjY3Ny4xMzYuMTM3LjI0OC0uMDI0LjI0OC0uMzU2IDAtLjg3MyAxLjM2LTEuOTc0IDIuODg0LTIuMzM1bDEuMzE2LS4zMTItMS4yLS4wMTZjLS42Ni0uMDA4LTEuNi4xNDYtMi4wODguMzQybTQ0LjQxNS0uMDIxYzEuOTI5LjM3NCAyLjcxMiAxLjE1NyAzLjA4NiAzLjA4NmwuMjk1IDEuNTI3LjA0Ni0xLjUxOGMuMDY0LTIuMDk3LTEuMzM5LTMuNS0zLjQzNi0zLjQzNmwtMS41MTguMDQ2IDEuNTI3LjI5NW0zMC4wNTUuNTk1Yy0uNzI0LjcyMy0uOTcgMS4zODEtLjkzNiAyLjVsLjA0NiAxLjUxOC4yOTUtMS41MjdjLjM3NC0xLjkyOSAxLjE1Ny0yLjcxMiAzLjA4Ni0zLjA4NmwxLjUyNy0uMjk1LTEuNTE4LS4wNDZjLTEuMTE5LS4wMzQtMS43NzcuMjEyLTIuNS45MzZtNDQuOTE2LS42MjVjMS41MzkuNDA1IDIuNDcgMS4xMTUgMi45MjEgMi4yMjlsLjMzLjgxNC4wMjYtLjgyNGMuMDQzLTEuNDItLjg4Ni0yLjIxOC0yLjc4OS0yLjM5NS0xLjU3OS0uMTQ2LTEuNjM2LS4xMjYtLjQ4OC4xNzZtODAuNjE0LjA1MWMtLjg2NC4zNDgtMS42NTggMi4xOC0xLjE2IDIuNjc3LjEzNi4xMzcuMjQ4LS4wMjQuMjQ4LS4zNTYgMC0uODczIDEuMzYtMS45NzQgMi44ODQtMi4zMzVsMS4zMTYtLjMxMi0xLjItLjAxNmMtLjY2LS4wMDgtMS42LjE0Ni0yLjA4OC4zNDJtOTQuNDE1LS4wMjFjLjg0LjE2MyAxLjgxMS41OCAyLjE1OS45MjcuMzQ3LjM0OC43NjQgMS4zMTkuOTI3IDIuMTU5bC4yOTUgMS41MjcuMDQ2LTEuNTE4Yy4wMzQtMS4xMTktLjIxMi0xLjc3Ny0uOTM2LTIuNS0uNzIzLS43MjQtMS4zODEtLjk3LTIuNS0uOTM2bC0xLjUxOC4wNDYgMS41MjcuMjk1TTg3LjcyIDIxOC44YzAgMS4yMS4wNzUgMS43MDUuMTY3IDEuMWE4Ljg5OSA4Ljg5OSAwIDAgMCAwLTIuMmMtLjA5Mi0uNjA1LS4xNjctLjExLS4xNjcgMS4xbTEyNC40IDBjMCAxLjIxLjA3NSAxLjcwNS4xNjcgMS4xYTguODk5IDguODk5IDAgMCAwIDAtMi4yYy0uMDkyLS42MDUtLjE2Ny0uMTEtLjE2NyAxLjFtNzUuNiAwYzAgMS4yMS4wNzUgMS43MDUuMTY3IDEuMWE4Ljg5OSA4Ljg5OSAwIDAgMCAwLTIuMmMtLjA5Mi0uNjA1LS4xNjctLjExLS4xNjcgMS4xTTM3LjM2MiAyMzEuNGMwIDMuNTIuMDYyIDQuOTA2LjEzNiAzLjA4MS4wNzQtMS44MjUuMDc0LTQuNzA1LS4wMDEtNi40LS4wNzUtMS42OTUtLjEzNi0uMjAxLS4xMzUgMy4zMTltMTAwLjAzNCA4MS4yYzAgNDguMTguMDQ3IDY3Ljk0OS4xMDQgNDMuOTMyLjA1Ny0yNC4wMTcuMDU3LTYzLjQzNyAwLTg3LjYtLjA1Ny0yNC4xNjMtLjEwNC00LjUxMi0uMTA0IDQzLjY2OG0yNS4yIDBjMCA0OC4xOC4wNDcgNjcuOTQ5LjEwNCA0My45MzIuMDU3LTI0LjAxNy4wNTctNjMuNDM3IDAtODcuNi0uMDU3LTI0LjE2My0uMTA0LTQuNTEyLS4xMDQgNDMuNjY4bTIyNC43NjYtODEuMmMwIDMuNTIuMDYyIDQuOTA2LjEzNiAzLjA4MS4wNzQtMS44MjUuMDc0LTQuNzA1LS4wMDEtNi40LS4wNzUtMS42OTUtLjEzNi0uMjAxLS4xMzUgMy4zMTltLTMzMi4yNTUgNi40OWMuNzE5LjA4OSAxLjc5OS4wODcgMi40LS4wMDRzLjAxMy0uMTY0LTEuMzA3LS4xNjJjLTEuMzIuMDAyLTEuODEyLjA3Ny0xLjA5My4xNjZtNC4zNTEuMzg3YzEuMDA5LjE5NyAxLjk4IDEuMTk4IDIuMjU0IDIuMzIzLjE1Ni42NC4yMDUuNTkyLjI0Mi0uMjM4LjA1Ny0xLjI3NS0xLjA4Ni0yLjM4MS0yLjM4NS0yLjMwOC0uODgxLjA1LS44OTEuMDctLjExMS4yMjNtMi42NjYgNS41MjNjLjAwMiAxLjMyLjA3NyAxLjgxMi4xNjYgMS4wOTMuMDg5LS43MTkuMDg3LTEuNzk5LS4wMDQtMi40cy0uMTY0LS4wMTMtLjE2MiAxLjMwN00zMzcuMzc4IDI3NWMuMDAxIDcuMDQuMDU1IDkuODY0LjEyMSA2LjI3NWE0MDcuNTYgNDA3LjU2IDAgMCAwIDAtMTIuOGMtLjA2Ni0zLjQ1MS0uMTIxLS41MTUtLjEyMSA2LjUyNW0yNS4yIDBjLjAwMSA3LjA0LjA1NSA5Ljg2NC4xMjEgNi4yNzVhNDA3LjU2IDQwNy41NiAwIDAgMCAwLTEyLjhjLS4wNjYtMy40NTEtLjEyMS0uNTE1LS4xMjEgNi41MjVNODAuMSAyODcuODg3YTguODk5IDguODk5IDAgMCAwIDIuMiAwYy42MDUtLjA5Mi4xMS0uMTY3LTEuMS0uMTY3LTEuMjEgMC0xLjcwNS4wNzUtMS4xLjE2N200LjUxNC40OTRjMS4xMTQuNDUxIDEuODI0IDEuMzgyIDIuMjI5IDIuOTIxLjMwMiAxLjE0OC4zMjIgMS4wOTEuMTc2LS40ODgtLjE3Ny0xLjkwMy0uOTc1LTIuODMyLTIuMzk1LTIuNzg5bC0uODI0LjAyNi44MTQuMzNtMi43NDggMTcuODE5YzAgMy41Mi4wNjIgNC45MDYuMTM2IDMuMDgxLjA3NC0xLjgyNS4wNzQtNC43MDUtLjAwMS02LjQtLjA3NS0xLjY5NS0uMTM2LS4yMDEtLjEzNSAzLjMxOW0tNDkuOTkyIDUwIC4wMDcgNDQgLjIxMi0zNWMuMTE2LTE5LjI1LjExMy0zOS4wNS0uMDA3LTQ0LS4xMi00Ljk1LS4yMTUgMTAuOC0uMjEyIDM1bTM0OS45OTItMzcuNmMwIDMuNTIuMDYyIDQuOTA2LjEzNiAzLjA4MS4wNzQtMS44MjUuMDc0LTQuNzA1LS4wMDEtNi40LS4wNzUtMS42OTUtLjEzNi0uMjAxLS4xMzUgMy4zMTltLS41NjIgMTQuOTU2YzAgMS42MjYtMS4xOCAyLjg5NC0zLjAyNSAzLjI0OWwtMS41NzUuMzAzIDEuNTE4LjA0NmMyLjAyMi4wNjEgMy40ODItMS4zMzcgMy40ODItMy4zMzYgMC0uNzgtLjA5LTEuNDE4LS4yLTEuNDE4LS4xMSAwLS4yLjUyLS4yIDEuMTU2bS0zNDguNzc1IDEuMDY4Yy0uMDQzIDEuNDIuODg2IDIuMjE4IDIuNzg5IDIuMzk1IDEuNTc5LjE0NiAxLjYzNi4xMjYuNDg4LS4xNzYtMS41MzktLjQwNS0yLjQ3LTEuMTE1LTIuOTIxLTIuMjI5bC0uMzMtLjgxNC0uMDI2LjgyNG0xOC4xNzEgMi44NyA2LjE5Ni4xMjYuMTEgMTguNjkuMTEgMTguNjktLjAwNi0xOC44LS4wMDYtMTguOC02LjMtLjAxNi02LjMwMS0uMDE1IDYuMTk3LjEyNW0yODEuMTg4LjIwNmMtLjEwNS4yNzUtLjE0MyAxNC40NS0uMDg1IDMxLjVsLjEwNiAzMSAuMDk4LTMxLjI5Ni4wOTctMzEuMjk2IDE4LjctLjEwOCAxOC43LS4xMDgtMTguNzEzLS4wOTZjLTE0LjY3Mi0uMDc1LTE4Ljc1My4wMTItMTguOTAzLjQwNG0tMTA5LjQ4NCAyNWM4LjYzNS4wNiAyMi43NjUuMDYgMzEuNCAwIDguNjM1LS4wNiAxLjU3LS4xMS0xNS43LS4xMXMtMjQuMzM1LjA1LTE1LjcuMTFtNTUuODI3LjQ4N2MuODQuMTYzIDEuODExLjU4IDIuMTU5LjkyNy4zNDcuMzQ4Ljc2NCAxLjMxOS45MjcgMi4xNTlsLjI5NSAxLjUyNy4wNDYtMS41MThjLjAzNC0xLjExOS0uMjEyLTEuNzc3LS45MzYtMi41LS43MjMtLjcyNC0xLjM4MS0uOTctMi41LS45MzZsLTEuNTE4LjA0NiAxLjUyNy4yOTVtMy42NTEgMjQuNDEzYzAgNi45My4wNTUgOS43NjUuMTIxIDYuM2EzOTQuOTUgMzk0Ljk1IDAgMCAwIDAtMTIuNmMtLjA2Ni0zLjQ2NS0uMTIxLS42My0uMTIxIDYuM20tMjI0LjUzMi0zLjg4MmMtLjA2NCAyLjA5NyAxLjMzOSAzLjUgMy40MzYgMy40MzZsMS41MTgtLjA0Ni0xLjUyNy0uMjk1Yy0xLjkyOS0uMzc0LTIuNzEyLTEuMTU3LTMuMDg2LTMuMDg2bC0uMjk1LTEuNTI3LS4wNDYgMS41MThtMTUuNDczIDMuNzhjMS44MjUuMDc0IDQuNzA1LjA3NCA2LjQtLjAwMSAxLjY5NS0uMDc1LjIwMS0uMTM2LTMuMzE5LS4xMzUtMy41MiAwLTQuOTA2LjA2Mi0zLjA4MS4xMzYiLz48L2c+PC9zdmc+)](https://nlp.stanford.edu/pubs/glove.pdf) |
<!--- AUTOGENERATED-NOTEBOOKS-TABLE -->

## 🐞 Bugs & 🦸 Contribution

Computer Vision progresses rapidly! Occasionally, our notebooks may lag a little behind the constantly advancing libraries. If you encounter any issues with the functionality of our notebooks, please create a [bug report](https://github.com/semilleroCV/deep-learning-notes/issues/new?assignees=&labels=bug%2Ctriage&projects=&template=bug-report.yml) to inform us.

If you'd like to add a new notebook or improve an existing one, please take a peek at our [contribution guide](https://github.com/semilleroCV/deep-learning-notes/blob/main/CONTRIBUTING.md). There you can find all the information you need.

We are here for you, so don't hesitate to [reach out](https://discord.gg/MkCpdsHZzJ).

## 💻 Run Locally

We try to make it as easy as possible to run our Notebooks in Colab. However, if you prefer to run them locally follow the instructions below. We recommend not to install the dependencies globally, use [virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

```console
# Clone the repository and navigate to the root directory:
git clone git@github.com:semilleroCV/deep-learning-notes.git
cd deep-learning-notes

# Set up the Python virtual environment and activate it:
python3 -m venv venv
# For Unix-based systems (Linux/Mac)
source venv/bin/activate
# For Windows systems
# venv\Scripts\activate

# (Optional) Install and run jupyter notebook:
pip install notebook
jupyter notebook
```
--------

