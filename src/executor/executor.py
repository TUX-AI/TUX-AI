import os
from config import config


def exec(command: str):
    for c in config:
        try:
            if command == c["command"]:
                os.system(command)
        except KeyError:
            return
    print(f"{command=}")
