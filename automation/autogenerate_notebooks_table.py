from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Optional, List
from logos import SHIELD_LOGOS

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
HFACE_BADGE_PATTERN = "[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-{}-yellow.svg?logo=data:image/png;base64,,iVBORw0KGgoAAAANSUhEUgAAAA4AAAANCAMAAACuAq9NAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAGtUExURQAAAP+dC/+aCv+uEf+mDv+cC///MP+sEP+lDv//af8AAP+eC/+fC/+XCf+fDP+kDv+kDv+fDP+XCf+OBv+gDP+xEv/BGP/IGv/AGP+wEv+fDP+FAv+hDP+6Ff+4Ff+fDP+aCv+0E/+yEv+YCf+jDf/EGf/CGP+hDf9xAP+qEP+nD/96AP+rEP+oD/+WCP+gDP+fDP+WCP+eC/+rEP+rEP+eC/+fDP+0E/++F//DGP+/F/+0E/+fDP+gDP+3FP/EGf/QHf/EGf+3FP+gDP+dC/+qEP+4Ff/EGf/GGv+2FP+oD/+3FP+qEP+dC/+QBv+cC/+hDP+jDf+eC/+VCP+VCP+eC/+cC/+QB//RHf/UHv/THv/VHv/QHf/SHuS9JN+5JPzQH9ezJu3FIv/DGZuDMZaCM/3RHvLIIX9wN7qaK//FGP/MHP/EGe/DIPLHIf/UHe3EIvPGH//KG//LG/HGIZF6NLCSLqiMMJuBM/rNH//JG/+wEv+4Ffu4F5t1M5c6QZQ9QK2GL/+7Fv+3FP+4FPy2Gf+mJ/+qJv26GP/DGP/HGv+6Ff/KGv/UH////0r1xdkAAABYdFJOUwAAAAAAAAAAAAAAAAAiZpOQYB0EXc/2/PXJVAJm7utaK9zTIXb9+2UEpZQFqpoGoJEEReLgRHL0+f7383F69fX+8vR5Lajk+fzryOunLAs8bXxJFBNIPQvP5D+ZAAAAAWJLR0SOggWzbwAAAAd0SU1FB+gICgIjBj1AntAAAADISURBVAjXY2BgZGLm5eMXEBRiYWJkAPKERUTFxMUlJKWkgXxWNhnZiMioqOgYOXl2VgZGBcXYuPjYhMSkCCVlRgZmFdXklNS09IzMLDV1DgYNzeyc3Lz8qILCnCItTgZtneKoktKy8orKqCpdLgY9/eqa2rr6hsammmoDQwYj4+bmlta29o6amhYTUwYzc4vOru6enu4uSytrGwZbO3uH3q6mpq5eB0cnZwYXVzd3D08vL28PdzcfXwZuP/+AwKDgkNDAgLBwHgAYAjML/ivY0AAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyNC0wOC0xMFQwMjozNTowMyswMDowMPBFIacAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjQtMDgtMTBUMDI6MzU6MDMrMDA6MDCBGJkbAAAAKHRFWHRkYXRlOnRpbWVzdGFtcAAyMDI0LTA4LTEwVDAyOjM1OjA2KzAwOjAwhDWXYwAAAABJRU5ErkJggg==)](https://huggingface.co/papers/{})"
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
