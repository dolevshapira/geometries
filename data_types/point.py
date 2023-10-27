from typing import Tuple, List, Union
from collections import OrderedDict


class Point:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = x
        self.y = y

    @staticmethod
    def from_xy(x: Union[int, float], y: Union[int, float]) -> "Point":
        return Point(x=x, y=y)

    @staticmethod
    def from_yx(y: Union[int, float], x: Union[int, float]) -> "Point":
        return Point(x=x, y=y)

    def as_int(self) -> "Point":
        return Point.from_xy(x=int(self.x), y=int(self.y))

    def as_float(self) -> "Point":
        return Point.from_xy(x=float(self.x), y=float(self.y))

    def to_xy(self) -> OrderedDict[str, Union[int, float]]:
        return OrderedDict(x=self.x, y=self.y)

    def to_yx(self) -> OrderedDict[str, Union[int, float]]:
        return OrderedDict(y=self.y, x=self.x)

    def relative_to(self, other: "Point") -> "Point":
        return self - other

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Point):
            this_point = self.as_float()
            other_point = __value.as_float()
            return this_point.x == other_point.x and this_point.y == other_point.y
        else:
            return False

    def __sub__(self, other: object) -> "Point":
        if isinstance(other, Point):
            return Point.from_xy(x=self.x - other.x, y=self.y - other.y)
        elif isinstance(other, Union[int, float]):
            return Point.from_xy(x=self.x - other, y=self.y - other)
        else:
            raise ValueError(
                f"Trying to subtruct from Point {str(self)} with non Point object {str(other)}"
            )

    def __add__(self, other: object) -> "Point":
        if isinstance(other, Point):
            return Point.from_xy(x=self.x + other.x, y=self.y + other.y)
        elif isinstance(other, Union[int, float]):
            return Point.from_xy(x=self.x + other, y=self.y + other)
        else:
            raise ValueError(
                f"Trying to add to Point {str(self)} with non Point object {str(other)}"
            )

    def __mul__(self, other: object) -> "Point":
        if isinstance(other, Point):
            return Point.from_xy(x=self.x * other.x, y=self.y * other.y)
        elif isinstance(other, Union[int, float]):
            return Point.from_xy(x=self.x * other, y=self.y * other)
        else:
            raise ValueError(
                f"Trying to multiply Point {str(self)} with non Point object {str(other)}"
            )

    def __truediv__(self, other: object) -> "Point":
        if isinstance(other, Point):
            return Point.from_xy(x=self.x / other.x, y=self.y / other.y)
        elif isinstance(other, Union[int, float]):
            return Point.from_xy(x=self.x / other, y=self.y / other)
        else:
            raise ValueError(
                f"Trying to multiply Point {str(self)} with non Point object {str(other)}"
            )

    def __str__(self) -> str:
        return f"Point({str(self.x)},{str(self.y)})"
