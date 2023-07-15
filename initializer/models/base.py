'''Base model for framework setup and initialization'''
import subprocess
from abc import ABC, abstractmethod
from config.console import Console
from config.filesystem import FileSystem


class BaseModel(ABC):
    '''BaseModel class will be used as a parent class for language
    and framework dependency and setup handling'''

    def __init__(self, framework: int, project_root_dir: str) -> None:
        self.framework = framework
        self.project_root_dir = project_root_dir
        self.dependencies: list[str] = []
        self.framework_dependencies: list[str] = []
        self.root_folders: list[str] = []

    def check_dependencies(self) -> False:
        '''Check for CLI dependencies required by system to install necessary packages'''
        try:
            for dependency in self.dependencies:
                subprocess.check_output([dependency, "--version"])
            return True
        except subprocess.CalledProcessError:
            return False

    @abstractmethod
    def setup_project(self):
        '''Override in child class and define the logic for project setup'''
        raise NotImplementedError(
            "Method 'setup_project' must be implemented.")

    def intialize_project(self) -> None:
        '''Check dependencies and initializer project'''
        try:
            if not self.check_dependencies():
                Console.error(
                    f"""Please make sure the following dependencies
                    are installed on your system: {', '.join(self.dependencies)}.""")
            else:
                FileSystem.init_project_dir(
                    project_root_dir=self.project_root_dir)
                self.setup_project()
        except OSError:
            Console.error(
                'Something went wrong while initializing your project.')
