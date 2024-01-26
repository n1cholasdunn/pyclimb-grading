from enum import Enum
from pydantic import BaseModel


class GradeLevels(str, Enum):
    UNKNOWN = 'unknown'
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    EXPERT = 'expert'


class Distribution(BaseModel):
    UNKNOWN: float
    BEGINNER: float
    INTERMEDIATE: float
    ADVANCED: float
    EXPERT: float


def score_to_level(score: float, distribution: Distribution) -> GradeLevels:
    sorted_levels = sorted(GradeLevels, key=lambda level: getattr(
        distribution, level.value), reverse=True)
    for level in sorted_levels:
        if getattr(distribution, level.value) <= score:
            return level
    return GradeLevels.UNKNOWN


def route_score_to_level(score: float) -> GradeLevels:
    distribution = Distribution(
        UNKNOWN=-1,
        BEGINNER=0,
        INTERMEDIATE=54,
        ADVANCED=67.5,
        EXPERT=82.5
    )
    return score_to_level(score, distribution)


def boulder_score_to_level(score: float) -> GradeLevels:
    distribution = Distribution(
        UNKNOWN=-1,
        BEGINNER=0,
        INTERMEDIATE=50,
        ADVANCED=60,
        EXPERT=72
    )
    return score_to_level(score, distribution)
