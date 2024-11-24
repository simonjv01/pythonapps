import os
import shutil


def organize_folder(folder):
    file_types = {
        "Images": [
            ".jpeg",
            ".jpg",
            ".tiff",
            ".gif",
            ".bmp",
            ".png",
            ".bpg",
            ".svg",
            ".heif",
            ".psd",
        ],
        "Videos": [
            ".avi",
            ".flv",
            ".wmv",
            ".mov",
            ".mp4",
            ".webm",
            ".vob",
            ".mng",
            ".qt",
            ".mpg",
            ".mpeg",
            ".3gp",
        ],
        "Documents": [
            ".oxps",
            ".epub",
            ".pages",
            ".docx",
            ".doc",
            ".fdf",
            ".ods",
            ".odt",
            ".pwi",
            ".xsn",
            ".xps",
            ".dotx",
            ".docm",
            ".dox",
            ".rvg",
            ".rtf",
            ".rtfd",
            ".wpd",
            ".xls",
            ".xlsx",
            ".ppt",
            ".pptx",
            ".pdf",
        ],
        "Archives": [
            ".a",
            ".ar",
            ".cpio",
            ".iso",
            ".tar",
            ".gz",
            ".rz",
            ".7z",
            ".dmg",
            ".rar",
            ".xar",
            ".zip",
        ],
        "Applications": [".exe", ".bat", ".bin", ".msi", ".apk", ".app", ".ipa"],
    }

    with os.scandir(folder) as entries:
        for entry in entries:
            if entry.is_file():
                ext = os.path.splitext(entry.name)[1].lower()
                for folder_name, extensions in file_types.items():
                    if ext in extensions:
                        target_folder = os.path.join(folder, folder_name)
                        os.makedirs(target_folder, exist_ok=True)
                        shutil.move(entry.path, os.path.join(target_folder, entry.name))
                        print(f"Moved {entry.name} to {folder_name}")


organize_folder("/Users/sjvar/Downloads")
