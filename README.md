# Projeto Final Aprendizado de Maquinas
By: Vitor Mello

## Setup (linux or macos)
This project utilizes UV for efficient Python dependency management and project installation. UV is a fast, modern Python package installer and resolver, designed as an alternative to pip and pip-tools.

Supported Operating Systems: Linux, macOS

### 1. Install UV (Optional)

Follow the official UV documentation for installation instructions:
- [UV Docs: Installing UV](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)

Example (macOS/Linux via Homebrew):
```
brew install astral-sh/uv/uv
```
### 2. Project Installation

Unlike traditional Python projects that often use requirements.txt or setup.py, this project manages its dependencies directly through .toml file. This means there are no requirements.txt, requirements.in, or setup.py files.

To set up the project and install its dependencies, navigate to the root directory of this repository and run the following command:

```
pip install -e .
```
Explanation:

- `pip install`: This command instructs UV to install Python packages.

- `-e .` (editable install): This flag installs the project in "editable" mode. This is particularly useful for development as it allows you to make changes to the project's source code without needing to reinstall it. Any modifications you make will be immediately reflected when you run the application.