import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "")
        self.assertNotEqual(hello.hello(), "Bye, world!")

    def test_add(self):
        self.assertEqual(hello.add(4, 5), 9)
        self.assertEqual(hello.add(3, 19), 22)
        self.assertNotEqual(hello.add(0, 0), 1)

    def test_sub(self):
        self.assertEqual(hello.sub(19, 1), 18)
        self.assertEqual(hello.sub(5, 9), -4)
        self.assertNotEqual(hello.sub(0, 0), 1)

    def test_mul(self):
        self.assertEqual(hello.mul(5, 5), 25)
        self.assertNotEqual(hello.mul(0, 5), 1)
        self.assertEqual(hello.mul(1, 9), 9)

    def test_div(self):
        self.assertEqual(hello.div(5, 5), 1)
        self.assertEqual(hello.div(15, 1), 15)
        self.assertNotEqual(
            hello.div(3, 10), 0.33333333333333333333333333333333333333333
        )

    def test_sprt(self):
        self.assertEqual(hello.sqrt(25), 5)
        self.assertNotEqual(hello.sqrt(4), 3)
        self.assertNotEqual(hello.sqrt(81), 10)

    def test_power(self):
        self.assertEqual(hello.power(5, 3), 125)
        self.assertEqual(hello.power(2, 8), 256)
        self.assertEqual(hello.power(1, 1), 1)

    def test_log(self):
        self.assertEqual(hello.log(2.718281828459045), 1)
        self.assertEqual(hello.log(2.718281828459045**5), 5)

    

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
