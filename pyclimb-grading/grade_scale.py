from enum import Enum
from typing import Union, List, Tuple, Callable, Optional
from pydantic import BaseModel
from abc import ABC, abstractmethod
import math
from .grade_level import GradeLevels


class GradeScales(Enum):
    AI = 'ai'
    AID = 'aid'
    WI = 'wi'
    VSCALE = 'vscale'
    YDS = 'yds'
    FONT = 'font'
    FRENCH = 'french'
    UIAA = 'uiaa'
    EWBANK = 'ewbank'
    SAXON = 'saxon'
    NORWEGIAN = 'norwegian'
    BRAZILLIAN_CRUX = 'brazilian_crux'


ScoreTuple = Tuple[float, float]


class GradeScale(ABC):
    display_name: str
    name: GradeScales
    offset: float
    allowable_conversion_type: List[GradeScales]
    grades: Optional[List[str]] = None

    @abstractmethod
    def is_type(self, grade: str) -> bool:
        pass

    @abstractmethod
    def get_score(self, grade: str) -> Union[float, ScoreTuple]:
        pass

    @abstractmethod
    def get_grade(self, score: Union[float, ScoreTuple]) -> str:
        pass

    @abstractmethod
    def get_grade_level(self, grade: str) -> GradeLevels:
        pass


def find_score_range(compare_fn: Callable, lst: List[BaseModel]) -> Union[float, ScoreTuple]:
    scores = sorted([lev.score for lev in lst if compare_fn(lev)])
    low = scores[0] if scores else 0
    high = scores[-1] if scores else low
    return (low, high) if high != low else low


def get_average_score(score: Union[float, ScoreTuple]) -> float:
    return score if isinstance(score, float) else (score[1] + score[0]) / 2


def get_rounded_score_tuple(grade_avg: float, next_grade_avg: float) -> ScoreTuple:
    low = math.ceil(min(grade_avg, next_grade_avg))
    high = math.floor(max(grade_avg, next_grade_avg))
    return (low, high)
