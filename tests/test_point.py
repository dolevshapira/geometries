from unittest import TextTestRunner, TestCase, TestSuite
from data_types.point import Point


class PointInitializationTestCase(TestCase):
    def test_int_initialization(self):
        x = 1
        y = 2
        point = Point(x=x, y=y)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        self.assertIsInstance(point.x, int)
        self.assertIsInstance(point.y, int)

    def test_float_initialization(self):
        x = 1.0
        y = 2.0
        point = Point(x=x, y=y)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        self.assertIsInstance(point.x, float)
        self.assertIsInstance(point.y, float)

    def test_from_xy(self):
        x = 1
        y = 2
        point = Point.from_xy(x, y)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)

    def test_from_yx(self):
        x = 1
        y = 2
        point = Point.from_yx(y, x)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)

    def runTest(self):
        self.test_int_initialization()
        self.test_float_initialization()
        self.test_from_xy()
        self.test_from_yx()


class PointExportingTestCase(TestCase):
    def setUp(self) -> None:
        self.point = Point(x=1, y=2)

    def test_to_xy(self):
        xy = self.point.to_xy()
        self.assertEqual(xy["x"], self.point.x)
        self.assertEqual(xy["y"], self.point.y)
        self.assertEqual([key for key in xy], ["x", "y"])

    def test_to_yx(self):
        yx = self.point.to_yx()
        self.assertEqual(yx["x"], self.point.x)
        self.assertEqual(yx["y"], self.point.y)
        self.assertEqual([key for key in yx], ["y", "x"])

    def test_as_float(self):
        float_point = Point(1, 2).as_float()
        self.assertIsInstance(float_point.x, float)
        self.assertIsInstance(float_point.y, float)

    def test_as_int(self):
        int_point = Point(1.0, 2.0).as_int()
        self.assertIsInstance(int_point.x, int)
        self.assertIsInstance(int_point.y, int)

    def runTest(self):
        self.test_to_xy()
        self.test_to_yx()
        self.test_as_float()
        self.test_as_int()


class PointOpsTestCase(TestCase):
    def setUp(self) -> None:
        self.x1 = 1
        self.y1 = 2
        self.x2 = 3
        self.y2 = 4
        self.point1 = Point.from_xy(self.x1, self.y1)
        self.point2 = Point.from_xy(self.x2, self.y2)

    def test_mul(self):
        mul_point = self.point1 * self.point2
        self.assertEqual(mul_point.x, self.point1.x * self.point2.x)
        self.assertEqual(mul_point.y, self.point1.y * self.point2.y)
        mul_point_num = self.point1 * self.y2
        self.assertEqual(mul_point_num.x, self.point1.x * self.y2)
        self.assertEqual(mul_point_num.y, self.point1.y * self.y2)

    def test_div(self):
        mul_point = self.point1 / self.point2
        self.assertEqual(mul_point.x, self.point1.x / self.point2.x)
        self.assertEqual(mul_point.y, self.point1.y / self.point2.y)
        mul_point_num = self.point1 / self.y2
        self.assertEqual(mul_point_num.x, self.point1.x / self.y2)
        self.assertEqual(mul_point_num.y, self.point1.y / self.y2)

    def test_add(self):
        add_point = self.point1 + self.point2
        self.assertEqual(add_point.x, self.point1.x + self.point2.x)
        self.assertEqual(add_point.y, self.point1.y + self.point2.y)
        add_point_num = self.point1 + self.y2
        self.assertEqual(add_point_num.x, self.point1.x + self.y2)
        self.assertEqual(add_point_num.y, self.point1.y + self.y2)

    def test_sub(self):
        sub_point = self.point1 - self.point2
        self.assertEqual(sub_point.x, self.point1.x - self.point2.x)
        self.assertEqual(sub_point.y, self.point1.y - self.point2.y)
        sub_point_num = self.point1 - self.y2
        self.assertEqual(sub_point_num.x, self.point1.x - self.y2)
        self.assertEqual(sub_point_num.y, self.point1.y - self.y2)

    def test_eq(self):
        self.assertTrue(self.point1.as_int() == self.point1.as_float())
        self.assertFalse(self.point1 == self.point2)

    def runTest(self):
        self.test_add()
        self.test_sub()
        self.test_mul()
        self.test_div()
        self.test_eq()


def suite():
    suite = TestSuite()
    suite.addTest(PointInitializationTestCase())
    suite.addTest(PointExportingTestCase())
    suite.addTest(PointOpsTestCase())
    return suite


if __name__ == "__main__":
    runner = TextTestRunner()
    runner.run(suite())
