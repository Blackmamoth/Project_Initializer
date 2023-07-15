'''Project Initializer module for boiler plate code generation'''
from argparse import ArgumentParser
import sys
from common.framework_enums import JSFrameworkEnums
from constants.help_text import (UTILITY_DESCRIPTION, LANGUAGE_HELP_TEXT,
                                 FRAMEWORK_HELP_TEXT, FRAMEWORK_ROOT_HELP_TEXT, REQUIRED_ARGS)
from constants.list_constants import SUPPORTTED_LANGUAGES, SUPPORTTED_FRAMEWORKS
from models.javascript import JavaScriptFramework
from config.console import Console

parser = ArgumentParser(description=UTILITY_DESCRIPTION,
                        add_help=True)

parser.add_argument("--language", help=LANGUAGE_HELP_TEXT,
                    choices=SUPPORTTED_LANGUAGES, required=True)

parser.add_argument("--framework", help=FRAMEWORK_HELP_TEXT,
                    choices=SUPPORTTED_FRAMEWORKS)

parser.add_argument("--path", help=FRAMEWORK_ROOT_HELP_TEXT)

if len(sys.argv) <= 1:
    parser.print_help(sys.stderr)
    parser.exit()

if __name__ == "__main__":
    args = parser.parse_args()
    if (args.language == 'js' and args.framework == 'express'):
        if not args.path in (None, ''):
            app = JavaScriptFramework(JSFrameworkEnums.EXPRESS, args.path)
            app.intialize_project()
        else:
            Console.warning(REQUIRED_ARGS, emoji=True)
    else:
        Console.warning(REQUIRED_ARGS, emoji=True)
