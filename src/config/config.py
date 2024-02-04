from typing import TypedDict, Literal, List


class config_type(TypedDict):
    command_type: Literal["voice"] | Literal["gesture"]
    command: str | None
    exec: str | None


config: List[config_type] = [
    {
        "command_type": "gesture",
        "command": "open web browser",
        "exec": "echo hello world"
    }
]
