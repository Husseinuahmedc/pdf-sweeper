# pdf-sweeper

A simple cross-platform Python CLI tool for finding and organizing PDF files.

`pdf-sweeper` recursively scans a directory, finds every `.pdf` file, shows the full path, then lets you decide what to do with each file: copy, move, delete, skip, or quit.

## Features

- Recursively search for PDF files
- Case-insensitive `.pdf` detection
- Shows full absolute file paths
- Copy PDFs to a target folder
- Move PDFs to a target folder
- Delete PDFs with `YES` confirmation
- Skip files safely
- Quit anytime
- Prevents overwriting by renaming duplicates:
  - `file.pdf`
  - `file_1.pdf`
  - `file_2.pdf`
- Works with Python standard library only

## Supported Systems

- Linux
- Arch Linux
- Windows
- macOS

## Requirements

- Python 3.8+
- No external dependencies

## Project Structure

```text
pdf-sweeper/
├── pdf_sweeper.py
├── README.md
├── .gitignore
└── LICENSE
