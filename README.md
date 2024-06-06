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

## 🐞 Bugs & 🦸 Contribution

Computer Vision moves fast! Sometimes our notebooks lag a little behind the ever-pushing forward libraries. If you notice that any of the notebooks is not working properly, create a [bug report](https://github.com/semilleroCV/deep-learning-notes/issues/new?assignees=&labels=bug%2Ctriage&projects=&template=bug-report.yml) and let us know.

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

