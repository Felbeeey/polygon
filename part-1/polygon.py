#!/usr/bin/env python3
import sys
import numpy as np
from typing import Any, Union, NoReturn
from os import EX_DATAERR


def _read(q: Any, s: Any) -> str:
    return input(f'{q}{s}')


def _check_input(input_value: Union[int, float, str]) -> Union[int, float]:
    if input_value is None:
        return 0

    if isinstance(input_value, str):
        if input_value.lower() in ('', 'null', 'zero', 'empty'):
            return 0

        try:
            input_value = int(input_value)
        except (AssertionError, ValueError):
            print(f'{input_value} is invalid !')
            sys.exit(EX_DATAERR)
        return input_value


def calc_area(x: list, y: list) -> Union[int, float]:
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def calc_side_length(x: list, y: list) -> Union[int, float]:
    res: Union[int, float] = 0
    lx: int = len(x)
    if lx == len(y):
        for i in range(lx):
            xa = x[i]
            ya = y[i]
            if i < (lx - 1):
                xb = x[i + 1]
                yb = y[i + 1]
            else:
                xb = x[0]
                yb = y[0]

            res += np.abs(np.linalg.norm(np.array((xa, ya)) - np.array((xb, yb))))
    return res


def main() -> NoReturn:
    value: str = _read('Polygon with how much corners ?\n', '>> ')
    corners: int = _check_input(value)

    if corners <= 2:
        flag: str = 's'
        if corners in (1, -1):
            flag: str = ''
        print(f'Polygon with {corners} corner{flag} ??')
        sys.exit(EX_DATAERR)

    x_coordinates: list = []
    y_coordinates: list = []
    for i in range(corners):
        # guard statement for x value
        x_value: Union[int, float, str] = _read(f'x[{i}] ', '>>')
        x_coord: float = _check_input(x_value)

        # guard statement for y value
        y_value: Union[int, float, str] = _read(f'y[{i}] ', '>>')
        y_coord: float = _check_input(y_value)

        x_coordinates.append(x_coord)
        y_coordinates.append(y_coord)

    print(f'Your polygon has an area of: {calc_area(x_coordinates, y_coordinates)}')
    print(f'Your polygon has an border length of: { calc_side_length(x_coordinates, y_coordinates)}')


if __name__ == '__main__':
    main()
