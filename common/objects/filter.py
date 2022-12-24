from enum import Enum
from enum import auto


class TFilter(Enum):
    BILATERAL = auto()
    EMBOSS = auto()
    GAUSSIAN_BLUR = auto()
    GRAYSCALE = auto()
    INVERT = auto()
    RETRO = auto()
