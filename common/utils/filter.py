from common.objects.filter import TFilter

import cv2 as cv
import numpy as np


def apply_filter(path: str, filter: TFilter) -> None:
    image = cv.imread(filename=path)

    if filter == TFilter.BILATERAL:
        image = cv.bilateralFilter(
            src=image,
            d=25,
            sigmaColor=50,
            sigmaSpace=50,
        )

    elif filter == TFilter.EMBOSS:
        kernel = np.array(
            [
                [-2, -1, 0],
                [-1, 1, 1],
                [0, 1, 2],
            ]
        )

        image = cv.filter2D(
            src=image,
            kernel=kernel,
            ddepth=-1,
        )

    elif filter == TFilter.GAUSSIAN_BLUR:
        image = cv.GaussianBlur(
            src=image,
            ksize=(5, 5),
            sigmaX=15,
            sigmaY=15,
        )

    elif filter == TFilter.GRAYSCALE:
        image = cv.cvtColor(
            src=image,
            code=cv.COLOR_BGR2GRAY,
        )

    elif filter == TFilter.INVERT:
        image = cv.bitwise_not(src=image)

    elif filter == TFilter.RETRO:
        image = cv.cvtColor(
            src=image,
            code=cv.COLOR_RGB2XYZ,
        )

    cv.imwrite(img=image, filename=path)
