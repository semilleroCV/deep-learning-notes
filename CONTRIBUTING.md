# Contributing to Deep Learning Notes

We are thrilled to have you contribute to the Deep Learning Notes repository! Whether you're proposing a new notebook, reporting an issue, or enhancing existing content, your input is valuable to ensure the repository remains a valuable resource for the community. Follow these simple steps to make your contribution.

## 📝 Before You Begin

- Review existing notebooks in the repository to avoid duplications. If a notebook on your topic already exists, consider [improving it](https://github.com/semilleroCV/deep-learning-notes/issues/new?assignees=&labels=enhancement&projects=&template=feature-report.yml) rather than creating a new one.

## 🔄 Contribution Process

### 1. Clone the Repository
```sh
git clone https://github.com/semilleroCV/deep-learning-notes.git
cd deep-learning-notes
```
### 2. Create a New Branch 🌿
Name your branch according to the type of contribution:

- **Feature**: `feat/topic-name`, e.g., `feat/focal-loss`
- **Enhancement**: `enh/notebook-name`, e.g., `enh/xception-module`
- **Bug Fix**: `fix/notebook-name`, e.g., `fix/mnist`
```sh
git checkout -b type/branch-name
```
### 3. Make Your Changes
- Edit or add your notebook in the appropriate directory under `notebooks/`.
- Ensure your notebook is fully executed and adheres to good coding practices.
- Include a list of libraries and their versions at the top of your notebook ([example](https://github.com/semilleroCV/deep-learning-notes/blob/feat/automation-table/notebooks/_template.ipynb)).
- Name your notebook clearly, must be in lowercase. e.g., `cross-entropy-loss.ipynb`.
- Be simple and precise, if your notebook explains a module of a network, e.g. Xception module, focus only on the Xception module.
### 4. Update the CSV
Add the relevant information about your notebook to the `automation/notebooks-table-data.csv`.
- `display_name` corresponds to the name by which your notebook will appear in the main readme, e.g., `Focal Loss`.
- `notebook_name` where your notebook is located, e.g., `losses/focal-loss.ipynb`
- (Optional) `github_repository_path` link to the source code of the document that you are covering.
- (Optional) `paper_url` URL of the document you are covering, e.g., `https://arxiv.org/abs/1708.02002`.
### 5. Commit and Push Your Changes
```sh
git add .
git commit -m "Add/enh/fix notebook on topic-name"
git push origin type/branch-name
```
### 6. Open a Pull Request
- Go to the repository on GitHub.
- Click "Compare & pull request" next to your branch.

## 🐞 Reporting Issues

If you encounter any issues or have suggestions, please create a [bug report](https://github.com/semilleroCV/deep-learning-notes/issues/new?assignees=&labels=bug%2Ctriage&projects=&template=bug-report.yml) in the repository detailing the problem and its impact.

## 💬 Stay Engaged

Join our [community](https://discord.gg/MkCpdsHZzJ) and share your insights to help drive the project forward. Your involvement is key to the continual improvement of the repository.

Thank you for helping us improve the Deep Learning Notes repository!
