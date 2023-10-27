from typing import Union, Dict
from collections import OrderedDict
from utils.dict_utils import add_suffix_to_dict_keys
from data_types.point import Point


class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        self.top_left = top_left
        self.bottom_right = bottom_right

    @staticmethod
    def from_corners(top_left_corner: Point, bottom_right_corner: Point) -> "Rectangle":
        return Rectangle(top_left=top_left_corner, bottom_right=bottom_right_corner)

    @staticmethod
    def from_xywh(
        x: Union[int, float],
        y: Union[int, float],
        w: Union[int, float],
        h: Union[int, float],
    ) -> "Rectangle":
        top_left = Point.from_xy(x=x, y=y)
        bottom_right = Point.from_xy(x=x + w, y=y + h)
        return Rectangle.from_corners(
            top_left_corner=top_left, bottom_right_corner=bottom_right
        )

    @staticmethod
    def from_xyxy(
        x1: Union[int, float],
        y1: Union[int, float],
        x2: Union[int, float],
        y2: Union[int, float],
    ) -> "Rectangle":
        top_left = Point.from_xy(x=x1, y=y1)
        bottom_right = Point.from_xy(x=x2, y=y2)
        return Rectangle.from_corners(
            top_left_corner=top_left, bottom_right_corner=bottom_right
        )

    @property
    def width(self) -> Union[int, float]:
        return self.right - self.left

    @property
    def height(self) -> Union[int, float]:
        return self.bottom - self.top

    @property
    def area(self) -> Union[int, float]:
        return self.height * self.width

    @property
    def top(self) -> Union[int, float]:
        return self.top_left.y

    @property
    def bottom(self) -> Union[int, float]:
        return self.bottom_right.y

    @property
    def left(self) -> Union[int, float]:
        return self.top_left.x

    @property
    def right(self) -> Union[int, float]:
        return self.bottom_right.x

    def as_float(self) -> "Rectangle":
        return Rectangle.from_corners(
            top_left_corner=self.top_left.as_float(),
            bottom_right_corner=self.bottom_right.as_float(),
        )

    def as_int(self) -> "Rectangle":
        return Rectangle.from_corners(
            top_left_corner=self.top_left.as_int(),
            bottom_right_corner=self.bottom_right.as_int(),
        )

    def to_xyxy(self) -> OrderedDict[str, Union[int, float]]:
        point1_kwargs = add_suffix_to_dict_keys(self.top_left.to_xy(), "1")
        point2_kwargs = add_suffix_to_dict_keys(self.bottom_right.to_xy(), "2")
        return OrderedDict(**point1_kwargs, **point2_kwargs)

    def to_xywh(self) -> OrderedDict[str, Union[int, float]]:
        point_kwargs = self.top_left.to_xy()
        wh_kwargs = OrderedDict(w=self.bottom - self.top, h=self.right - self.left)
        return OrderedDict(**point_kwargs, **wh_kwargs)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return (self.top_left == other.top_left) and (
                self.bottom_right == other.bottom_right
            )
        else:
            return False

    def __sub__(self, other: object) -> "Rectangle":
        if isinstance(other, Union[int, float, Point]):
            return Rectangle.from_corners(
                top_left_corner=self.top_left - other,
                bottom_right_corner=self.bottom_right - other,
            )
        else:
            raise ValueError(
                f"Trying to subtract from Rectangle {str(self)} with non Point object {str(other)}"
            )

    def __add__(self, other: object) -> "Rectangle":
        if isinstance(other, Union[int, float, Point]):
            return Rectangle.from_corners(
                top_left_corner=self.top_left + other,
                bottom_right_corner=self.bottom_right + other,
            )
        else:
            raise ValueError(
                f"Trying to add to Rectangle {str(self)} with non Point object {str(other)}"
            )

    def __mul__(self, other: object):
        if isinstance(other, Union[int, float, Point]):
            return Rectangle.from_corners(
                top_left_corner=self.top_left * other,
                bottom_right_corner=self.bottom_right * other,
            )
        else:
            raise ValueError(
                f"Trying to multiply Rectangle {str(self)} with non Point object {str(other)}"
            )

    def __truediv__(self, other: object):
        if isinstance(other, Union[int, float, Point]):
            return Rectangle.from_corners(
                top_left_corner=self.top_left / other,
                bottom_right_corner=self.bottom_right / other,
            )
        else:
            raise ValueError(
                f"Trying to multiply Rectangle {str(self)} with non Point object {str(other)}"
            )

    def __str__(self) -> str:
        return f"Rectangle({str(self.top_left)},{str(self.bottom_right)})"
