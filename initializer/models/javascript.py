from .base import BaseModel
from common.framework_enums import JSFrameworkEnums
from config.console import Console
from constants.help_text import FRAMEWORK_NOT_SUPPORTED
from config.filesystem import FileSystem
import subprocess


class JavaScriptFramework(BaseModel):

    EXPRESS_DEFAULT_CONTENT = r"""const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})"""

    def __init__(self, framework: int, project_root_dir: str, ts: bool = False) -> None:
        super().__init__(framework, project_root_dir)
        self.ts = ts
        self.dependencies = ["node", "npm", "npx"]
        self.framework_dev_dependencies = ["nodemon", "dotenv"]

    def setup_project(self) -> None:
        try:
            FileSystem.change_directory(self.project_root_dir)
            subprocess.call(["npm", "init", "-y"])
            if self.framework == JSFrameworkEnums.EXPRESS:
                self.setup_express()
            else:
                Console.info(FRAMEWORK_NOT_SUPPORTED)
        except Exception as e:
            Console.error(e)

    def setup_express(self) -> None:
        try:
            self.framework_dependencies = [
                "express", "express-async-handler", "http-errors",
                "cors", "cookie-parser", "bcryptjs",
                "joi", "jsonwebtoken", "moment",
                "mongoose", "redis"
            ]
            self.root_folders = [
                "common", "config", "controllers", "helpers", "middleware", "models", "routes"]
            Console.info(
                'Installing dependencies and dev dependencies for Express app.')
            subprocess.call(
                f"npm i {' '.join(self.framework_dependencies)}", shell=True)
            subprocess.call(
                f"npm i -D {' '.join(self.framework_dev_dependencies)}", shell=True)
            Console.info('Dependencies successfully installed.')
            FileSystem.create_file(
                "app.js", project_dir_path=self.project_root_dir, content=self.EXPRESS_DEFAULT_CONTENT)
            FileSystem.create_folders_in_root(
                self.root_folders, self.project_root_dir)
            Console.success("Project successfully intialized!!!.")
        except Exception as e:
            Console.error(e)
