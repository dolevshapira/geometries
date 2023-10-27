from typing import OrderedDict
from unittest import TextTestRunner, TestCase, TestSuite
from data_types.geometry.point import Point
from data_types.geometry.rectangle import Rectangle


class RectanglePropertiesTestCase(TestCase):
    def setUp(self) -> None:
        self.top_left = Point(1, 2)
        self.bottom_right = Point(3, 4)
        self.rect = Rectangle(top_left=self.top_left, bottom_right=self.bottom_right)

    def test_top(self):
        self.assertEqual(self.top_left.y, self.rect.top)

    def test_bottom(self):
        self.assertEqual(self.bottom_right.y, self.rect.bottom)

    def test_left(self):
        self.assertEqual(self.top_left.x, self.rect.left)

    def test_right(self):
        self.assertEqual(self.bottom_right.x, self.rect.right)

    def test_width(self):
        self.assertEqual(self.bottom_right.x - self.top_left.x, self.rect.width)

    def test_width(self):
        self.assertEqual(self.bottom_right.y - self.top_left.y, self.rect.height)

    def runTest(self):
        self.test_left()
        self.test_right()
        self.test_top()
        self.test_bottom()


class RectangleInitializationTestCase(TestCase):
    def test_int_initialization(self):
        top_left = Point(1, 2)
        bottom_right = Point(3, 4)
        rect = Rectangle(top_left, bottom_right)
        self.assertEqual(top_left.x, rect.top_left.x)
        self.assertEqual(top_left.y, rect.top_left.y)
        self.assertEqual(bottom_right.x, rect.bottom_right.x)
        self.assertEqual(bottom_right.y, rect.bottom_right.y)
        self.assertIsInstance(rect.bottom_right.x, int)
        self.assertIsInstance(rect.bottom_right.x, int)
        self.assertIsInstance(rect.top_left.x, int)
        self.assertIsInstance(rect.top_left.x, int)

    def test_float_initialization(self):
        top_left = Point(1.0, 2.0)
        bottom_right = Point(3.0, 4.0)
        rect = Rectangle(top_left, bottom_right)
        self.assertEqual(top_left, rect.top_left)
        self.assertEqual(bottom_right, rect.bottom_right)
        self.assertIsInstance(rect.bottom_right.x, float)
        self.assertIsInstance(rect.bottom_right.x, float)
        self.assertIsInstance(rect.top_left.x, float)
        self.assertIsInstance(rect.top_left.x, float)

    def test_from_corners(self):
        top_left = Point(1, 2)
        bottom_right = Point(3, 4)
        rect = Rectangle(top_left, bottom_right)
        self.assertEqual(top_left, rect.top_left)
        self.assertEqual(bottom_right, rect.bottom_right)

    def test_from_xywh(self):
        x = 1
        y = 2
        w = 3
        h = 4
        rect = Rectangle.from_xywh(x, y, w, h)
        self.assertEqual(rect.top_left.x, x)
        self.assertEqual(rect.top_left.y, y)
        self.assertEqual(rect.bottom_right.y, y + h)
        self.assertEqual(rect.bottom_right.x, x + w)

    def test_from_xyxy(self):
        x1 = 1
        y1 = 2
        x2 = 3
        y2 = 4
        rect = Rectangle.from_xyxy(x1, y1, x2, y2)
        self.assertEqual(rect.top_left.x, x1)
        self.assertEqual(rect.top_left.y, y1)
        self.assertEqual(rect.bottom_right.x, x2)
        self.assertEqual(rect.bottom_right.y, y2)

    def runTest(self):
        self.test_int_initialization()
        self.test_float_initialization()
        self.test_from_corners()
        self.test_from_xywh()
        self.test_from_xyxy()


class RectangleExportingTestCase(TestCase):
    def setUp(self) -> None:
        self.top_left = Point(1.0, 2.0)
        self.bottom_right = Point(3, 4)
        self.rect = Rectangle.from_corners(
            top_left_corner=self.top_left, bottom_right_corner=self.bottom_right
        )

    def test_to_xyxy(self):
        xyxy = self.rect.to_xyxy()
        self.assertIsInstance(xyxy, OrderedDict)
        xyxy_keys = list(xyxy.keys())
        self.assertEqual(xyxy_keys, ["x1", "y1", "x2", "y2"])
        self.assertEqual(self.rect.top_left.x, xyxy["x1"])
        self.assertEqual(self.rect.top_left.y, xyxy["y1"])
        self.assertEqual(self.rect.bottom_right.x, xyxy["x2"])
        self.assertEqual(self.rect.bottom_right.y, xyxy["y2"])

    def test_to_xywh(self):
        xywh = self.rect.to_xywh()
        self.assertIsInstance(xywh, OrderedDict)
        xywh_keys = list(xywh.keys())
        self.assertEqual(xywh_keys, ["x", "y", "w", "h"])
        self.assertEqual(self.rect.top_left.x, xywh["x"])
        self.assertEqual(self.rect.top_left.y, xywh["y"])
        self.assertEqual(self.rect.bottom_right.x - self.rect.top_left.x, xywh["w"])
        self.assertEqual(self.rect.bottom_right.y - self.rect.top_left.y, xywh["h"])

    def test_as_float(self):
        x1 = self.rect.top_left.x
        y1 = self.rect.top_left.y
        x2 = self.rect.bottom_right.x
        y2 = self.rect.bottom_right.y

        float_rect = self.rect.as_float()
        x1_float = float_rect.top_left.x
        y1_float = float_rect.top_left.y
        x2_float = float_rect.bottom_right.x
        y2_float = float_rect.bottom_right.y

        self.assertIsInstance(x1_float, float)
        self.assertIsInstance(y1_float, float)
        self.assertIsInstance(x2_float, float)
        self.assertIsInstance(y2_float, float)

        self.assertEqual(x1, x1_float)
        self.assertEqual(y1, y1_float)
        self.assertEqual(x2, x2_float)
        self.assertEqual(y2, y2_float)

    def test_as_int(self):
        x1 = self.rect.top_left.x
        y1 = self.rect.top_left.y
        x2 = self.rect.bottom_right.x
        y2 = self.rect.bottom_right.y

        float_rect = self.rect.as_int()
        x1_int = float_rect.top_left.x
        y1_int = float_rect.top_left.y
        x2_int = float_rect.bottom_right.x
        y2_int = float_rect.bottom_right.y

        self.assertIsInstance(x1_int, int)
        self.assertIsInstance(y1_int, int)
        self.assertIsInstance(x2_int, int)
        self.assertIsInstance(y2_int, int)

        self.assertEqual(x1, x1_int)
        self.assertEqual(y1, y1_int)
        self.assertEqual(x2, x2_int)
        self.assertEqual(y2, y2_int)

    def runTest(self):
        self.test_to_xyxy()
        self.test_to_xywh()
        self.test_as_float()
        self.test_as_int()


class RectangleOpsTestCase(TestCase):
    def setUp(self) -> None:
        self.x1 = 1
        self.y1 = 2
        self.x2 = 3
        self.y2 = 4
        self.x3 = 5
        self.y3 = 6
        self.x4 = 7
        self.y4 = 8
        self.point1 = Point.from_xy(self.x1, self.y1)
        self.point2 = Point.from_xy(self.x2, self.y2)
        self.point3 = Point.from_xy(self.x3, self.y3)
        self.point4 = Point.from_xy(self.x4, self.y4)
        self.rect1 = Rectangle.from_corners(self.point1, self.point3)
        self.rect2 = Rectangle.from_corners(self.point2, self.point4)

    def test_mul_point(self):
        mul_rect = self.rect1 * self.point4
        self.assertEqual(mul_rect.top_left.x, self.point1.x * self.point4.x)
        self.assertEqual(mul_rect.bottom_right.x, self.point3.x * self.point4.x)
        self.assertEqual(mul_rect.top_left.y, self.point1.y * self.point4.y)
        self.assertEqual(mul_rect.bottom_right.y, self.point3.y * self.point4.y)

    def test_mul_scalar(self):
        mul_rect = self.rect1 * 4
        self.assertEqual(mul_rect.top_left.x, self.point1.x * 4)
        self.assertEqual(mul_rect.bottom_right.x, self.point3.x * 4)
        self.assertEqual(mul_rect.top_left.y, self.point1.y * 4)
        self.assertEqual(mul_rect.bottom_right.y, self.point3.y * 4)

    def test_div_point(self):
        div_rect = self.rect1 / self.point4
        self.assertEqual(div_rect.top_left.x, self.point1.x / self.point4.x)
        self.assertEqual(div_rect.bottom_right.x, self.point3.x / self.point4.x)
        self.assertEqual(div_rect.top_left.y, self.point1.y / self.point4.y)
        self.assertEqual(div_rect.bottom_right.y, self.point3.y / self.point4.y)

    def test_div_scalar(self):
        div_rect = self.rect1 / 4
        self.assertEqual(div_rect.top_left.x, self.point1.x / 4)
        self.assertEqual(div_rect.bottom_right.x, self.point3.x / 4)
        self.assertEqual(div_rect.top_left.y, self.point1.y / 4)
        self.assertEqual(div_rect.bottom_right.y, self.point3.y / 4)

    def test_add_point(self):
        add_rect = self.rect1 + self.point4
        self.assertEqual(add_rect.top_left.x, self.point1.x + self.point4.x)
        self.assertEqual(add_rect.bottom_right.x, self.point3.x + self.point4.x)
        self.assertEqual(add_rect.top_left.y, self.point1.y + self.point4.y)
        self.assertEqual(add_rect.bottom_right.y, self.point3.y + self.point4.y)

    def test_add_scalar(self):
        add_rect = self.rect1 + 4
        self.assertEqual(add_rect.top_left.x, self.point1.x + 4)
        self.assertEqual(add_rect.bottom_right.x, self.point3.x + 4)
        self.assertEqual(add_rect.top_left.y, self.point1.y + 4)
        self.assertEqual(add_rect.bottom_right.y, self.point3.y + 4)

    def test_sub_point(self):
        sub_rect = self.rect1 - self.point4
        self.assertEqual(sub_rect.top_left.x, self.point1.x - self.point4.x)
        self.assertEqual(sub_rect.bottom_right.x, self.point3.x - self.point4.x)
        self.assertEqual(sub_rect.top_left.y, self.point1.y - self.point4.y)
        self.assertEqual(sub_rect.bottom_right.y, self.point3.y - self.point4.y)

    def test_sub_scalar(self):
        sub_rect = self.rect1 - 4
        self.assertEqual(sub_rect.top_left.x, self.point1.x - 4)
        self.assertEqual(sub_rect.bottom_right.x, self.point3.x - 4)
        self.assertEqual(sub_rect.top_left.y, self.point1.y - 4)
        self.assertEqual(sub_rect.bottom_right.y, self.point3.y - 4)

    def test_eq(self):
        self.assertTrue(self.rect1.as_int() == self.rect1.as_float())
        self.assertTrue(self.rect1.as_int() == self.rect1.as_float())
        self.assertFalse(self.rect1 == self.rect2)

    def runTest(self):
        self.test_add_scalar()
        self.test_add_point()
        self.test_sub_scalar()
        self.test_sub_point()
        self.test_mul_scalar()
        self.test_mul_point()
        self.test_div_scalar()
        self.test_div_point()
        self.test_eq()


def suite():
    suite = TestSuite()
    suite.addTest(RectangleInitializationTestCase())
    suite.addTest(RectanglePropertiesTestCase())
    suite.addTest(RectangleExportingTestCase())
    suite.addTest(RectangleOpsTestCase())
    return suite


if __name__ == "__main__":
    runner = TextTestRunner()
    runner.run(suite())
