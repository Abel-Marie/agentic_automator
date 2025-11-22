import logging
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class Logger:
    def info(self, message: str):
        print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} {message}")

    def warning(self, message: str):
        print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {message}")

    def error(self, message: str):
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")

    def tool_output(self, tool_name: str, output: str):
        print(f"{Fore.CYAN}[TOOL: {tool_name}]{Style.RESET_ALL} {output}")

logger = Logger()
