# deep-learning-notes

Welcome to the Deep Learning Notes repository! This repository serves as a comprehensive resource for deep learning enthusiasts, providing detailed notebooks, modular implementations, and in-depth analyses related to various aspects of deep learning. Below is the structure and a brief description of each directory within the repository:

## Project Organization

```
├── LICENSE            <- Open-source license (MIT)
├── README.md          <- The top-level README for this project.
│
├── CONTRIBUTING.md    <- How to contribute to the project.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a short `-` delimited description, e.g. `cross-entropy-loss`.
│   │
│   ├── architectures  <- Implementations of architectures, e.g. UNET.
│   │
│   ├── losses         <- Examples of a loss function, e.g. NLLLoss.
│   │
│   ├── metrics        <- Demonstrations of metrics, e.g. IoU
│   │
│   ├── modules        <- Implementations of a module, e.g. Xception module.
│   │
│   └── data_exploration    <- Exploration of a dataset, e.g. MNIST.
│ 
├── papers             <- Articles about important deep learning papers.
│
├── automation 
│   │
│   └── autogenerate_notebooks_table.py Script that performs the update of the main readme based on notebooks-table-data.csv    
│
├── requirements.txt   <- The requirements file for reproducing the basic environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── core <- Source code for use in this project.
    │
    ├── __init__.py    <- Makes core a Python module
    │
    └── utils.py    <- Useful functions
```

## 🐞 Bugs & 🦸 Contribution

Computer Vision moves fast! Sometimes our notebooks lag a tad behind the ever-pushing forward libraries. If you notice that any of the notebooks is not working properly, create a [bug report]() and let us know.

If you'd like to add a new notebook or improve an existing one, please take a peek at our [contribution guide](https://github.com/semilleroCV/deep-learning-notes/blob/main/CONTRIBUTING.md). There you can find all the information you need.

We are here for you, so don't hesitate to [reach out](https://discord.gg/MkCpdsHZzJ).

## 💻 Run Locally

We try to make it as easy as possible to run our Notebooks in Colab. However, if you prefer to run them locally using a Conda environment, follow the instructions below.

```console
# Clone the repository and navigate to the root directory:
git clone git@github.com:semilleroCV/deep-learning-notes.git
cd deep-learning-notes

# Set up the Conda environment by executing the following commands in your terminal, 
# this will create a Conda environment named deep-learning-notes with Python version
# 3.10 and install the necessary dependencies:
make create_environment

# Activate the Conda environment:
conda activate deep-learning-notes
make requirements

# Run Jupyter Notebook:
jupyter notebook
```

This will open Jupyter Notebook in your default web browser, allowing you to access and run the notebooks locally.

--------

