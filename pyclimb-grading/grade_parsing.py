from typing import Union, List, Optional
from pydantic import BaseModel
from enum import Enum
from .grade_scale import GradeScales, GradeScale


def get_scale(grade_scale_type: GradeScales) -> Optional[GradeScale]:
    scale = scales.get(grade_scale_type)
    if scale is None:
        print(f"Scale: {grade_scale_type} isn't supported")
    return scale
