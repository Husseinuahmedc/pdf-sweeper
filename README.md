# pdf-sweeper

A simple cross-platform command-line tool that recursively searches for PDF files and lets you choose what to do with each file.

## Description

`pdf-sweeper` scans a folder for files ending with `.pdf`, displays every found file with its full absolute path, then lets you handle each file one by one.

You can:

- Copy it
- Move it
- Delete it
- Skip it
- Quit processing

The project uses only Python standard libraries.

## Features

- Recursively finds PDF files
- Case-insensitive `.pdf` matching
- Displays full absolute paths
- File-by-file interactive actions
- Copy PDFs to a target folder
- Move PDFs to a target folder
- Delete PDFs only after confirmation
- Avoids overwriting existing files by adding `_1`, `_2`, etc.
- Works without external dependencies

## Supported Systems

- Linux
- Arch Linux
- Windows
- macOS

## Requirements

- Python 3.8 or newer recommended
- No external packages required

## Project Structure

```text
pdf-sweeper/
├── pdf_sweeper.py
├── README.md
├── .gitignore
└── LICENSE
```

## Usage

### Linux / Arch Linux / macOS

```bash
cd pdf-sweeper
python3 pdf_sweeper.py
```

### Windows

```powershell
cd pdf-sweeper
python pdf_sweeper.py
```

## Example Terminal Session

```text
pdf-sweeper
Find PDF files and choose whether to copy, move, delete, or skip them.

Directory to scan (press Enter for current directory):
Scanning: /home/user/Documents

Found PDF files:
1. /home/user/Documents/book.pdf
2. /home/user/Documents/college/lecture.PDF

Target folder (press Enter for /home/user/newfolderforpdfs):

Target folder: /home/user/newfolderforpdfs

[1/2] /home/user/Documents/book.pdf
[c] copy  [m] move  [d] delete  [s] skip  [q] quit
Choose action: c
Copied to: /home/user/newfolderforpdfs/book.pdf

[2/2] /home/user/Documents/college/lecture.PDF
[c] copy  [m] move  [d] delete  [s] skip  [q] quit
Choose action: s
Skipped.

Summary
-------
Copied:  1
Moved:   0
Deleted: 0
Skipped: 1
Errors:  0
```

## Delete Safety Notes

Deleting a file requires confirmation.

To delete a file, you must type:

```text
YES
```

Any other input cancels the delete action and skips the file.

## How Filename Conflicts Are Handled

If the target folder already contains a file with the same name, `pdf-sweeper` does not overwrite it.

Example:

```text
book.pdf
book_1.pdf
book_2.pdf
```

## Future Improvements

- `argparse` support
- Dry-run mode
- File type filters
- Duplicate detection

## License

MIT License
