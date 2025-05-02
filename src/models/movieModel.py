from typing import TypedDict

class MovieModel(TypedDict):
    id: int
    title: str
    cast: list[str]
