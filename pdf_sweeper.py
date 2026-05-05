from pathlib import Path
import shutil


def get_scan_directory():
    """Ask the user which directory to scan."""
    user_input = input("Directory to scan (press Enter for current directory): ").strip()

    if user_input == "":
        scan_dir = Path.cwd()
    else:
        scan_dir = Path(user_input).expanduser()

    scan_dir = scan_dir.resolve()

    if not scan_dir.exists():
        print(f"Error: directory does not exist: {scan_dir}")
        return None

    if not scan_dir.is_dir():
        print(f"Error: path is not a directory: {scan_dir}")
        return None

    return scan_dir


def get_target_directory():
    """Ask the user for the target folder."""
    default_target = Path.home() / "newfolderforpdfs"
    user_input = input(f"Target folder (press Enter for {default_target}): ").strip()

    if user_input == "":
        target_dir = default_target
    else:
        target_dir = Path(user_input).expanduser()

    return target_dir.resolve()


def find_pdfs(scan_dir):
    """Recursively find PDF files, case-insensitive."""
    pdf_files = []

    try:
        for path in scan_dir.rglob("*"):
            if path.is_file() and path.suffix.lower() == ".pdf":
                pdf_files.append(path.resolve())
    except PermissionError as error:
        print(f"Permission error while scanning: {error}")
    except OSError as error:
        print(f"OS error while scanning: {error}")

    return pdf_files


def get_unique_destination(target_dir, filename):
    """
    Return a destination path that does not overwrite an existing file.

    Example:
    file.pdf -> file_1.pdf -> file_2.pdf
    """
    destination = target_dir / filename

    if not destination.exists():
        return destination

    original = Path(filename)
    stem = original.stem
    suffix = original.suffix
    counter = 1

    while True:
        new_name = f"{stem}_{counter}{suffix}"
        destination = target_dir / new_name

        if not destination.exists():
            return destination

        counter += 1


def copy_pdf(file_path, target_dir):
    """Copy a PDF file to the target directory."""
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        destination = get_unique_destination(target_dir, file_path.name)
        shutil.copy2(file_path, destination)
        print(f"Copied to: {destination}")
        return True
    except Exception as error:
        print(f"Error copying {file_path}: {error}")
        return False


def move_pdf(file_path, target_dir):
    """Move a PDF file to the target directory."""
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        destination = get_unique_destination(target_dir, file_path.name)
        shutil.move(str(file_path), str(destination))
        print(f"Moved to: {destination}")
        return True
    except Exception as error:
        print(f"Error moving {file_path}: {error}")
        return False


def delete_pdf(file_path):
    """Delete a PDF file after confirmation."""
    confirmation = input("Type YES to confirm delete: ").strip()

    if confirmation != "YES":
        print("Delete cancelled.")
        return "skipped"

    try:
        file_path.unlink()
        print(f"Deleted: {file_path}")
        return "deleted"
    except Exception as error:
        print(f"Error deleting {file_path}: {error}")
        return "error"


def process_files(files, target_dir):
    """Ask the user what to do with each PDF file."""
    summary = {
        "copied": 0,
        "moved": 0,
        "deleted": 0,
        "skipped": 0,
        "errors": 0,
    }

    for index, file_path in enumerate(files, start=1):
        print()
        print(f"[{index}/{len(files)}] {file_path}")
        print("[c] copy  [m] move  [d] delete  [s] skip  [q] quit")

        choice = input("Choose action: ").strip().lower()

        if choice == "c":
            if copy_pdf(file_path, target_dir):
                summary["copied"] += 1
            else:
                summary["errors"] += 1

        elif choice == "m":
            if move_pdf(file_path, target_dir):
                summary["moved"] += 1
            else:
                summary["errors"] += 1

        elif choice == "d":
            result = delete_pdf(file_path)

            if result == "deleted":
                summary["deleted"] += 1
            elif result == "skipped":
                summary["skipped"] += 1
            else:
                summary["errors"] += 1

        elif choice == "s":
            print("Skipped.")
            summary["skipped"] += 1

        elif choice == "q":
            print("Stopped by user.")
            break

        else:
            print("Invalid choice. File skipped.")
            summary["skipped"] += 1

    return summary


def main():
    """Main program entry point."""
    print("pdf-sweeper")
    print("Find PDF files and choose whether to copy, move, delete, or skip them.")
    print()

    scan_dir = get_scan_directory()

    if scan_dir is None:
        return

    print(f"Scanning: {scan_dir}")
    files = find_pdfs(scan_dir)

    if not files:
        print("No PDF files found.")
        return

    print()
    print("Found PDF files:")

    for index, file_path in enumerate(files, start=1):
        print(f"{index}. {file_path}")

    print()
    target_dir = get_target_directory()

    print()
    print(f"Target folder: {target_dir}")

    summary = process_files(files, target_dir)

    print()
    print("Summary")
    print("-------")
    print(f"Copied:  {summary['copied']}")
    print(f"Moved:   {summary['moved']}")
    print(f"Deleted: {summary['deleted']}")
    print(f"Skipped: {summary['skipped']}")
    print(f"Errors:  {summary['errors']}")


if __name__ == "__main__":
    main()
