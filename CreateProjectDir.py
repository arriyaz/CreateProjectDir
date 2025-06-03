#!/usr/bin/env python3

import os
from datetime import datetime

def main():
    # Prompt for user input
    project_name = input("What is the project folder name? ").strip()

    author_name = input("Who is your name (Default: Anisur Rahman)? ").strip()
    if not author_name:
        author_name = "Anisur Rahmna"

    print("What is the purpose of creating this project folder (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    purpose = "\n".join(lines)

    # Create base project folder
    os.makedirs(project_name, exist_ok=True)

    # Define subfolder structure
    subfolders = [
        "00_docs",
        "01_data",
        "02_codes",
        "03_notebooks",
        "04_workflows",
        "05_results",
        "06_temp"
    ]

    # Create subfolders
    for sub in subfolders:
        os.makedirs(os.path.join(project_name, sub), exist_ok=True)

    # Prepare README content
    now = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    readme_content = (
        f"# {project_name}\n\n"
        f"**Author:** {author_name}\n\n"
        f"**Date:** {now}\n\n"
        f"**Description:** {purpose}\n"
    )

    # Write to README.md
    readme_path = os.path.join(project_name, "README.md")
    with open(readme_path, "w") as f:
        f.write(readme_content)

    print(f"Project folder '{project_name}' created successfully with README.md.")

if __name__ == "__main__":
    main()
