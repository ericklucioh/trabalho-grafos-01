from dataclasses import dataclass

@dataclass
class MovieModel:
    id: int
    title: str
    cast: list[str]
