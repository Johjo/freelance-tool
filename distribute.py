import dataclasses
from typing import List


@dataclasses.dataclass
class Worker:
    name: str
    effort: int
    coefficient: float


def distribute(budget, *peoples: List[Worker]):
    tj = sum([people.coefficient * people.effort for people in peoples])
    return {people.name: (budget / tj * (people.coefficient * people.effort)) for people in peoples}