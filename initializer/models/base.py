import subprocess
from config.console import Console
from config.filesystem import FileSystem
from abc import ABC, abstractmethod


class BaseModel(ABC):

    def __init__(self, framework: int, project_root_dir: str) -> None:
        self.framework = framework
        self.project_root_dir = project_root_dir
        self.dependencies: list[str] = []
        self.framework_dependencies: list[str] = []
        self.root_folders: list[str] = []

    def check_dependencies(self) -> False:
        try:
            for dependency in self.dependencies:
                subprocess.check_output([dependency, "--version"])
            return True
        except subprocess.CalledProcessError:
            return False

    @abstractmethod
    def setup_project(self):
        raise NotImplementedError(
            "Method 'setup_project' must be implemented.")

    def intialize_project(self) -> bool:
        try:
            if not self.check_dependencies():
                Console.error(
                    f"Please make sure the following dependencies are installed on your system: {', '.join(self.dependencies)}.")
            else:
                FileSystem.init_project_dir(
                    project_root_dir=self.project_root_dir)
                self.setup_project()
        except Exception as e:
            return False
