from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Optional, List
from .logos import SHIELD_LOGOS

NOTEBOOKS_ROOT_PATH = "https://github.com/semilleroCV/deep-learning-notes/blob/main/notebooks"
NOTEBOOKS_COLAB_ROOT_PATH = "github/semilleroCV/deep-learning-notes/blob/main/notebooks"

WARNING_HEADER = [
    "<!---",
    "   WARNING: DO NOT EDIT THIS TABLE MANUALLY. IT IS AUTOMATICALLY GENERATED.",
    "   HEAD OVER TO CONTRIBUTING.MD FOR MORE DETAILS ON HOW TO MAKE CHANGES PROPERLY.",
    "-->"
]

TABLE_HEADER = [
    "| **notebook** | **open in colab** | **repository / paper** |",
    "|:------------:|:-----------------:|:----------------------:|"
]

# Update section headers based on your notebook folders
SECTIONS = {
    "architectures": "## 🏗️ Architectures",
    "losses": "## ❌ Loss Functions",
    "metrics": "## 📏 Metrics",
    "modules": "## 🧩 Modules",
    "data_exploration": "## 🔍 Data Exploration"
}

NOTEBOOK_LINK_PATTERN = "[{}]({}/{})"
OPEN_IN_COLAB_BADGE_PATTERN = "[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/{}/{})"
GITHUB_BADGE_PATTERN = "[![GitHub](https://badges.aleen42.com/src/github.svg)]({})"
ARXIV_BADGE_PATTERN = "[![arXiv](https://img.shields.io/badge/arXiv-{}-%23B31B1B.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/{})"
PUBMED_BADGE_PATTERN = "[![PubMed](https://img.shields.io/badge/PubMed-{}-blue.svg?logo=pubmed&logoColor=white)](https://pubmed.ncbi.nlm.nih.gov/{})"
HFACE_BADGE_PATTERN = "[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-{}-yellow.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5NSIgaGVpZ2h0PSI4OCIgZmlsbD0ibm9uZSI+Cgk8cGF0aCBmaWxsPSIjRkZEMjFFIiBkPSJNNDcuMjEgNzYuNWEzNC43NSAzNC43NSAwIDEgMCAwLTY5LjUgMzQuNzUgMzQuNzUgMCAwIDAgMCA2OS41WiIgLz4KCTxwYXRoCgkJZmlsbD0iI0ZGOUQwQiIKCQlkPSJNODEuOTYgNDEuNzVhMzQuNzUgMzQuNzUgMCAxIDAtNjkuNSAwIDM0Ljc1IDM0Ljc1IDAgMCAwIDY5LjUgMFptLTczLjUgMGEzOC43NSAzOC43NSAwIDEgMSA3Ny41IDAgMzguNzUgMzguNzUgMCAwIDEtNzcuNSAwWiIKCS8+Cgk8cGF0aAoJCWZpbGw9IiMzQTNCNDUiCgkJZD0iTTU4LjUgMzIuM2MxLjI4LjQ0IDEuNzggMy4wNiAzLjA3IDIuMzhhNSA1IDAgMSAwLTYuNzYtMi4wN2MuNjEgMS4xNSAyLjU1LS43MiAzLjctLjMyWk0zNC45NSAzMi4zYy0xLjI4LjQ0LTEuNzkgMy4wNi0zLjA3IDIuMzhhNSA1IDAgMSAxIDYuNzYtMi4wN2MtLjYxIDEuMTUtMi41Ni0uNzItMy43LS4zMloiCgkvPgoJPHBhdGgKCQlmaWxsPSIjRkYzMjNEIgoJCWQ9Ik00Ni45NiA1Ni4yOWM5LjgzIDAgMTMtOC43NiAxMy0xMy4yNiAwLTIuMzQtMS41Ny0xLjYtNC4wOS0uMzYtMi4zMyAxLjE1LTUuNDYgMi43NC04LjkgMi43NC03LjE5IDAtMTMtNi44OC0xMy0yLjM4czMuMTYgMTMuMjYgMTMgMTMuMjZaIgoJLz4KCTxwYXRoCgkJZmlsbD0iIzNBM0I0NSIKCQlmaWxsLXJ1bGU9ImV2ZW5vZGQiCgkJZD0iTTM5LjQzIDU0YTguNyA4LjcgMCAwIDEgNS4zLTQuNDljLjQtLjEyLjgxLjU3IDEuMjQgMS4yOC40LjY4LjgyIDEuMzcgMS4yNCAxLjM3LjQ1IDAgLjktLjY4IDEuMzMtMS4zNS40NS0uNy44OS0xLjM4IDEuMzItMS4yNWE4LjYxIDguNjEgMCAwIDEgNSA0LjE3YzMuNzMtMi45NCA1LjEtNy43NCA1LjEtMTAuNyAwLTIuMzQtMS41Ny0xLjYtNC4wOS0uMzZsLS4xNC4wN2MtMi4zMSAxLjE1LTUuMzkgMi42Ny04Ljc3IDIuNjdzLTYuNDUtMS41Mi04Ljc3LTIuNjdjLTIuNi0xLjI5LTQuMjMtMi4xLTQuMjMuMjkgMCAzLjA1IDEuNDYgOC4wNiA1LjQ3IDEwLjk3WiIKCQljbGlwLXJ1bGU9ImV2ZW5vZGQiCgkvPgoJPHBhdGgKCQlmaWxsPSIjRkY5RDBCIgoJCWQ9Ik03MC43MSAzN2EzLjI1IDMuMjUgMCAxIDAgMC02LjUgMy4yNSAzLjI1IDAgMCAwIDAgNi41Wk0yNC4yMSAzN2EzLjI1IDMuMjUgMCAxIDAgMC02LjUgMy4yNSAzLjI1IDAgMCAwIDAgNi41Wk0xNy41MiA0OGMtMS42MiAwLTMuMDYuNjYtNC4wNyAxLjg3YTUuOTcgNS45NyAwIDAgMC0xLjMzIDMuNzYgNy4xIDcuMSAwIDAgMC0xLjk0LS4zYy0xLjU1IDAtMi45NS41OS0zLjk0IDEuNjZhNS44IDUuOCAwIDAgMC0uOCA3IDUuMyA1LjMgMCAwIDAtMS43OSAyLjgyYy0uMjQuOS0uNDggMi44LjggNC43NGE1LjIyIDUuMjIgMCAwIDAtLjM3IDUuMDJjMS4wMiAyLjMyIDMuNTcgNC4xNCA4LjUyIDYuMSAzLjA3IDEuMjIgNS44OSAyIDUuOTEgMi4wMWE0NC4zMyA0NC4zMyAwIDAgMCAxMC45MyAxLjZjNS44NiAwIDEwLjA1LTEuOCAxMi40Ni01LjM0IDMuODgtNS42OSAzLjMzLTEwLjktMS43LTE1LjkyLTIuNzctMi43OC00LjYyLTYuODctNS03Ljc3LS43OC0yLjY2LTIuODQtNS42Mi02LjI1LTUuNjJhNS43IDUuNyAwIDAgMC00LjYgMi40NmMtMS0xLjI2LTEuOTgtMi4yNS0yLjg2LTIuODJBNy40IDcuNCAwIDAgMCAxNy41MiA0OFptMCA0Yy41MSAwIDEuMTQuMjIgMS44Mi42NSAyLjE0IDEuMzYgNi4yNSA4LjQzIDcuNzYgMTEuMTguNS45MiAxLjM3IDEuMzEgMi4xNCAxLjMxIDEuNTUgMCAyLjc1LTEuNTMuMTUtMy40OC0zLjkyLTIuOTMtMi41NS03LjcyLS42OC04LjAxLjA4LS4wMi4xNy0uMDIuMjQtLjAyIDEuNyAwIDIuNDUgMi45MyAyLjQ1IDIuOTNzMi4yIDUuNTIgNS45OCA5LjNjMy43NyAzLjc3IDMuOTcgNi44IDEuMjIgMTAuODMtMS44OCAyLjc1LTUuNDcgMy41OC05LjE2IDMuNTgtMy44MSAwLTcuNzMtLjktOS45Mi0xLjQ2LS4xMS0uMDMtMTMuNDUtMy44LTExLjc2LTcgLjI4LS41NC43NS0uNzYgMS4zNC0uNzYgMi4zOCAwIDYuNyAzLjU0IDguNTcgMy41NC40MSAwIC43LS4xNy44My0uNi43OS0yLjg1LTEyLjA2LTQuMDUtMTAuOTgtOC4xNy4yLS43My43MS0xLjAyIDEuNDQtMS4wMiAzLjE0IDAgMTAuMiA1LjUzIDExLjY4IDUuNTMuMTEgMCAuMi0uMDMuMjQtLjEuNzQtMS4yLjMzLTIuMDQtNC45LTUuMi01LjIxLTMuMTYtOC44OC01LjA2LTYuOC03LjMzLjI0LS4yNi41OC0uMzggMS0uMzggMy4xNyAwIDEwLjY2IDYuODIgMTAuNjYgNi44MnMyLjAyIDIuMSAzLjI1IDIuMWMuMjggMCAuNTItLjEuNjgtLjM4Ljg2LTEuNDYtOC4wNi04LjIyLTguNTYtMTEuMDEtLjM0LTEuOS4yNC0yLjg1IDEuMzEtMi44NVoiCgkvPgoJPHBhdGgKCQlmaWxsPSIjRkZEMjFFIgoJCWQ9Ik0zOC42IDc2LjY5YzIuNzUtNC4wNCAyLjU1LTcuMDctMS4yMi0xMC44NC0zLjc4LTMuNzctNS45OC05LjMtNS45OC05LjNzLS44Mi0zLjItMi42OS0yLjljLTEuODcuMy0zLjI0IDUuMDguNjggOC4wMSAzLjkxIDIuOTMtLjc4IDQuOTItMi4yOSAyLjE3LTEuNS0yLjc1LTUuNjItOS44Mi03Ljc2LTExLjE4LTIuMTMtMS4zNS0zLjYzLS42LTMuMTMgMi4yLjUgMi43OSA5LjQzIDkuNTUgOC41NiAxMS0uODcgMS40Ny0zLjkzLTEuNzEtMy45My0xLjcxcy05LjU3LTguNzEtMTEuNjYtNi40NGMtMi4wOCAyLjI3IDEuNTkgNC4xNyA2LjggNy4zMyA1LjIzIDMuMTYgNS42NCA0IDQuOSA1LjItLjc1IDEuMi0xMi4yOC04LjUzLTEzLjM2LTQuNC0xLjA4IDQuMTEgMTEuNzcgNS4zIDEwLjk4IDguMTUtLjggMi44NS05LjA2LTUuMzgtMTAuNzQtMi4xOC0xLjcgMy4yMSAxMS42NSA2Ljk4IDExLjc2IDcuMDEgNC4zIDEuMTIgMTUuMjUgMy40OSAxOS4wOC0yLjEyWiIKCS8+Cgk8cGF0aAoJCWZpbGw9IiNGRjlEMEIiCgkJZD0iTTc3LjQgNDhjMS42MiAwIDMuMDcuNjYgNC4wNyAxLjg3YTUuOTcgNS45NyAwIDAgMSAxLjMzIDMuNzYgNy4xIDcuMSAwIDAgMSAxLjk1LS4zYzEuNTUgMCAyLjk1LjU5IDMuOTQgMS42NmE1LjggNS44IDAgMCAxIC44IDcgNS4zIDUuMyAwIDAgMSAxLjc4IDIuODJjLjI0LjkuNDggMi44LS44IDQuNzRhNS4yMiA1LjIyIDAgMCAxIC4zNyA1LjAyYy0xLjAyIDIuMzItMy41NyA0LjE0LTguNTEgNi4xLTMuMDggMS4yMi01LjkgMi01LjkyIDIuMDFhNDQuMzMgNDQuMzMgMCAwIDEtMTAuOTMgMS42Yy01Ljg2IDAtMTAuMDUtMS44LTEyLjQ2LTUuMzQtMy44OC01LjY5LTMuMzMtMTAuOSAxLjctMTUuOTIgMi43OC0yLjc4IDQuNjMtNi44NyA1LjAxLTcuNzcuNzgtMi42NiAyLjgzLTUuNjIgNi4yNC01LjYyYTUuNyA1LjcgMCAwIDEgNC42IDIuNDZjMS0xLjI2IDEuOTgtMi4yNSAyLjg3LTIuODJBNy40IDcuNCAwIDAgMSA3Ny40IDQ4Wm0wIDRjLS41MSAwLTEuMTMuMjItMS44Mi42NS0yLjEzIDEuMzYtNi4yNSA4LjQzLTcuNzYgMTEuMThhMi40MyAyLjQzIDAgMCAxLTIuMTQgMS4zMWMtMS41NCAwLTIuNzUtMS41My0uMTQtMy40OCAzLjkxLTIuOTMgMi41NC03LjcyLjY3LTguMDFhMS41NCAxLjU0IDAgMCAwLS4yNC0uMDJjLTEuNyAwLTIuNDUgMi45My0yLjQ1IDIuOTNzLTIuMiA1LjUyLTUuOTcgOS4zYy0zLjc4IDMuNzctMy45OCA2LjgtMS4yMiAxMC44MyAxLjg3IDIuNzUgNS40NyAzLjU4IDkuMTUgMy41OCAzLjgyIDAgNy43My0uOSA5LjkzLTEuNDYuMS0uMDMgMTMuNDUtMy44IDExLjc2LTctLjI5LS41NC0uNzUtLjc2LTEuMzQtLjc2LTIuMzggMC02LjcxIDMuNTQtOC41NyAzLjU0LS40MiAwLS43MS0uMTctLjgzLS42LS44LTIuODUgMTIuMDUtNC4wNSAxMC45Ny04LjE3LS4xOS0uNzMtLjctMS4wMi0xLjQ0LTEuMDItMy4xNCAwLTEwLjIgNS41My0xMS42OCA1LjUzLS4xIDAtLjE5LS4wMy0uMjMtLjEtLjc0LTEuMi0uMzQtMi4wNCA0Ljg4LTUuMiA1LjIzLTMuMTYgOC45LTUuMDYgNi44LTcuMzMtLjIzLS4yNi0uNTctLjM4LS45OC0uMzgtMy4xOCAwLTEwLjY3IDYuODItMTAuNjcgNi44MnMtMi4wMiAyLjEtMy4yNCAyLjFhLjc0Ljc0IDAgMCAxLS42OC0uMzhjLS44Ny0xLjQ2IDguMDUtOC4yMiA4LjU1LTExLjAxLjM0LTEuOS0uMjQtMi44NS0xLjMxLTIuODVaIgoJLz4KCTxwYXRoCgkJZmlsbD0iI0ZGRDIxRSIKCQlkPSJNNTYuMzMgNzYuNjljLTIuNzUtNC4wNC0yLjU2LTcuMDcgMS4yMi0xMC44NCAzLjc3LTMuNzcgNS45Ny05LjMgNS45Ny05LjNzLjgyLTMuMiAyLjctMi45YzEuODYuMyAzLjIzIDUuMDgtLjY4IDguMDEtMy45MiAyLjkzLjc4IDQuOTIgMi4yOCAyLjE3IDEuNTEtMi43NSA1LjYzLTkuODIgNy43Ni0xMS4xOCAyLjEzLTEuMzUgMy42NC0uNiAzLjEzIDIuMi0uNSAyLjc5LTkuNDIgOS41NS04LjU1IDExIC44NiAxLjQ3IDMuOTItMS43MSAzLjkyLTEuNzFzOS41OC04LjcxIDExLjY2LTYuNDRjMi4wOCAyLjI3LTEuNTggNC4xNy02LjggNy4zMy01LjIzIDMuMTYtNS42MyA0LTQuOSA1LjIuNzUgMS4yIDEyLjI4LTguNTMgMTMuMzYtNC40IDEuMDggNC4xMS0xMS43NiA1LjMtMTAuOTcgOC4xNS44IDIuODUgOS4wNS01LjM4IDEwLjc0LTIuMTggMS42OSAzLjIxLTExLjY1IDYuOTgtMTEuNzYgNy4wMS00LjMxIDEuMTItMTUuMjYgMy40OS0xOS4wOC0yLjEyWiIKCS8+Cjwvc3ZnPgo=)](https://huggingface.co/papers/{})"
GENERIC_PAPER_BADGE_PATTERN = "[![Paper](https://img.shields.io/badge/📜-Link%20to%20paper-blue)]({})"



AUTOGENERATED_NOTEBOOKS_TABLE_TOKEN = "<!--- AUTOGENERATED-NOTEBOOKS-TABLE -->"

@dataclass(frozen=True)
class TableEntry:
    display_name: str
    notebook_name: str
    github_repository_path: Optional[str]
    paper_url: Optional[str]

    @classmethod
    def from_csv_line(cls, csv_line: str) -> TableEntry:
        csv_fields = [
            field.strip()
            for field
            in csv_line.split(",")
        ]
        if len(csv_fields) != 4:
            raise Exception("Every csv line must contain 4 fields")
        return TableEntry(
            display_name=csv_fields[0],
            notebook_name=csv_fields[1],
            github_repository_path=csv_fields[2],
            paper_url=csv_fields[3]
        )

    def format(self) -> str:
        section = self.notebook_name.split('/')[0]
        notebook_link = NOTEBOOK_LINK_PATTERN.format(self.display_name, NOTEBOOKS_ROOT_PATH, self.notebook_name)
        open_in_colab_badge = OPEN_IN_COLAB_BADGE_PATTERN.format(NOTEBOOKS_COLAB_ROOT_PATH, self.notebook_name)
        github_badge = GITHUB_BADGE_PATTERN.format(self.github_repository_path) if self.github_repository_path else ""
        paper_badge = ""

        if self.paper_url:
            if "arxiv.org" in self.paper_url:
                arxiv_id = self.paper_url.split("/")[-1]
                # paper_badge = f"[![arXiv]({SHIELD_LOGOS['arxiv']})](https://arxiv.org/abs/{arxiv_id})"
                paper_badge = ARXIV_BADGE_PATTERN.format(arxiv_id, arxiv_id) if arxiv_id else ""
            elif "cvf" in self.paper_url:
                paper_badge = f"[![CVF]({SHIELD_LOGOS['cvf']})]({self.paper_url})"
            elif "researchgate" in self.paper_url:
                paper_badge = f"[![ResearchGate]({SHIELD_LOGOS['researchgate']})]({self.paper_url})"
            elif "sciencedirect" in self.paper_url:
                paper_badge = f"[![ScienceDirect]({SHIELD_LOGOS['sciencedirect']})]({self.paper_url})"
            elif "pubmed" in self.paper_url:
                pm_id = self.paper_url.split("/")[-2]
                paper_badge = PUBMED_BADGE_PATTERN.format(pm_id, pm_id) if pm_id else ""
                # paper_badge = f"[![PubMed]({SHIELD_LOGOS['pubmed']})](https://pubmed.ncbi.nlm.nih.gov/{pm_id})"
            elif "webofscience" in self.paper_url:
                paper_badge = f"[![Web of Science]({SHIELD_LOGOS['webofscience']})]({self.paper_url})"
            elif "spiedigitallibrary" in self.paper_url:
                paper_badge = f"[![SPIE]({SHIELD_LOGOS['spie']})]({self.paper_url})"
            elif "ieeexplore" in self.paper_url:
                paper_badge = f"[![IEEE Xplore]({SHIELD_LOGOS['ieee']})]({self.paper_url})"
            elif "huggingface" in self.paper_url:
                hface_id = self.paper_url.split("/")[-1]
                # paper_badge = f"[![Hugging Face]({SHIELD_LOGOS['huggingface']})]({self.paper_url})"
                paper_badge = HFACE_BADGE_PATTERN.format(hface_id, hface_id) if hface_id else ""
            elif "spie" in self.paper_url:
                paper_badge = f"[![SPIE]({SHIELD_LOGOS['spie']})]({self.paper_url})"
            elif "nlp.stanford.edu" in self.paper_url:
                paper_badge = f"[![NLP Stanford]({SHIELD_LOGOS['nlp-stanford']})]({self.paper_url})"
            elif "nature" in self.paper_url:
                paper_badge = f"[![Nature]({SHIELD_LOGOS['nature']})]({self.paper_url})"
            else:
                paper_badge = GENERIC_PAPER_BADGE_PATTERN.format(self.paper_url)
        
        return section, f"| {notebook_link} | {open_in_colab_badge} | {github_badge} {paper_badge} |"

def read_lines_from_file(path: str) -> List[str]:
    with open(path) as file:
        return [line.rstrip() for line in file]

def save_lines_to_file(path: str, lines: List[str]) -> None:
    with open(path, "w") as f:
        for line in lines:
            f.write("%s\n" % line)

def parse_csv_lines(csv_lines: List[str]) -> List[TableEntry]:
    return [
        TableEntry.from_csv_line(csv_line=csv_line)
        for csv_line
        in csv_lines
    ]

def search_lines_with_token(lines: List[str], token: str) -> List[int]:
    result = []
    for line_index, line in enumerate(lines):
        if token in line:
            result.append(line_index)
    return result

def inject_markdown_table_into_readme(readme_lines: List[str], table_lines: List[str]) -> List[str]:
    lines_with_token_indexes = search_lines_with_token(lines=readme_lines, token=AUTOGENERATED_NOTEBOOKS_TABLE_TOKEN)
    if len(lines_with_token_indexes) != 2:
        raise Exception(f"Please inject two {AUTOGENERATED_NOTEBOOKS_TABLE_TOKEN} "
                        f"tokens to signal start and end of autogenerated table.")

    [table_start_line_index, table_end_line_index] = lines_with_token_indexes
    return readme_lines[:table_start_line_index + 1] + table_lines + readme_lines[table_end_line_index:]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data_path', default='automation/notebooks-table-data.csv')
    parser.add_argument('-r', '--readme_path', default='README.md')
    args = parser.parse_args()

    csv_lines = read_lines_from_file(path=args.data_path)[1:]
    readme_lines = read_lines_from_file(path=args.readme_path)
    table_entries = parse_csv_lines(csv_lines=csv_lines)

    section_entries = {section: [] for section in SECTIONS.keys()}
    for entry in table_entries:
        section, formatted_entry = entry.format()
        if section in section_entries:
            section_entries[section].append(formatted_entry)
    
    table_lines = WARNING_HEADER
    for section, header in SECTIONS.items():
        section_lines = section_entries.get(section, [])
        if section_lines:
            table_lines += [header + f" ({len(section_lines)} notebooks)"] + TABLE_HEADER + section_lines

    readme_lines = inject_markdown_table_into_readme(readme_lines=readme_lines, table_lines=table_lines)
    save_lines_to_file(path=args.readme_path, lines=readme_lines)
