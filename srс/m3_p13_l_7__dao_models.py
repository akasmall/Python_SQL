from dataclasses import dataclass
from typing import Optional


@dataclass
class Course:
    name: str
    description: str
    id: Optional[int] = None


@dataclass
class Lesson:
    name: str
    text: str
    course_id: int
    id: Optional[int] = None
