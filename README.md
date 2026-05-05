# pdf-sweeper

> Cross-platform Python CLI for finding, copying, moving, deleting, and organizing PDF files.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20Only-orange)

## What it does

`pdf-sweeper` recursively scans a directory, finds every file ending with `.pdf`, prints the full absolute path, then asks what to do with each file.

For each PDF, you can:

- copy it
- move it
- delete it
- skip it
- quit anytime

The tool is intentionally simple, readable, and beginner-friendly.

## Features

- Recursive PDF search
- Case-insensitive `.pdf` detection
- Full absolute path display
- Copy PDFs to a target folder
- Move PDFs to a target folder
- Delete PDFs only after typing `YES`
- Skip individual files
- Quit anytime
- Prevents overwriting by renaming duplicates:
  - `file.pdf`
  - `file_1.pdf`
  - `file_2.pdf`
- Uses only Python standard libraries
- Works on Linux, Arch Linux, Windows, and macOS

## Requirements

- Python 3.8+
- No external dependencies

## Project structure

```text
pdf-sweeper/
├── pdf_sweeper.py
├── README.md
├── .gitignore
└── LICENSE
```

## Usage

Clone the repository:

```bash
git clone https://github.com/Husseinuahmedc/pdf-sweeper.git
cd pdf-sweeper
```

Run the tool:

```bash
python pdf_sweeper.py
```

On Linux/macOS, you can also run:

```bash
python3 pdf_sweeper.py
```

## Example workflow

```text
Found PDF:
  /home/user/Downloads/book.pdf

Choose action:
  [c] copy
  [m] move
  [d] delete
  [s] skip
  [q] quit
```

## Safety notes

Deleting requires exact `YES` confirmation.

Copying and moving will not overwrite existing files. If a file with the same name exists, the tool creates a numbered name automatically.

## Why this project exists

This project is a small practical CLI tool for cleaning scattered PDF files from Downloads, Desktop, project folders, and external drives.

It is also a good beginner Python project because it uses real standard-library modules:

- `pathlib`
- `shutil`
- file traversal
- user input
- safe file operations
- cross-platform paths

## Roadmap

- Add optional command-line arguments
- Add dry-run mode
- Add file size display
- Add modified-date display
- Add test coverage
- Add packaging support

## License

MIT License.
