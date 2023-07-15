from typing import Union
from pathlib import Path
import os


class FileSystem:

    @staticmethod
    def init_project_dir(project_root_dir: str) -> bool:
        try:
            Path(project_root_dir).mkdir()
            return True
        except FileNotFoundError:
            return False
        except OSError:
            return False

    @staticmethod
    def create_folders_in_root(folder_list: list[str], project_root_dir: str) -> bool:
        try:
            for folder in folder_list:
                folder_path = Path(project_root_dir).joinpath(folder)
                Path(folder_path).mkdir()
            return True
        except FileNotFoundError:
            return False
        except OSError:
            return False

    @staticmethod
    def create_nested_folders(nested_folder_list: list[str], project_dir_path: str) -> bool:
        try:
            base_path = Path(project_dir_path)
            new_path = base_path.joinpath(*nested_folder_list)
            new_path.mkdir(parents=True, exist_ok=True)
            return True
        except FileNotFoundError:
            return False
        except OSError:
            return False

    @staticmethod
    def create_file(file_name: str, project_dir_path: str, content: Union[str, None] = None) -> bool:
        try:
            base_path = Path(project_dir_path).joinpath(file_name)
            with open(base_path, "w") as f:
                if content is not None:
                    f.writelines(content)
        except Exception as e:
            return False

    @staticmethod
    def change_directory(dir_path: str) -> None:
        try:
            os.chdir(Path(dir_path))
        except OSError:
            return False
