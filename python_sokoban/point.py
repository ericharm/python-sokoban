from __future__ import annotations

from dataclasses import dataclass


class PointIter:
    def __init__(self, point: Point):
        self.point = point
        self.i = 0

    def __iter__(self) -> PointIter:
        return self

    def __next__(self) -> int:
        if self.i == 0:
            self.i += 1
            return self.point.x
        elif self.i == 1:
            self.i += 1
            return self.point.y
        else:
            raise StopIteration


@dataclass
class Point:
    """
    A point is a location in a 2D space.
    """

    x: int
    y: int

    def __iter__(self) -> PointIter:
        return PointIter(self)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)
