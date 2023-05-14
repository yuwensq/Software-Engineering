import unittest
import max_product_sub_array as mpsa
from unittest.mock import patch


class TestMPSA(unittest.TestCase):
    """
    单元测试类
    """

    def test_common_case(self):
        # 测试数组长度为1
        self.assertEqual(mpsa.unit_test([2])[0], 2)
        self.assertEqual(mpsa.unit_test([-2])[0], -2)
        # 测试全为正整数
        self.assertEqual(mpsa.unit_test([2, 3, 4])[0], 24)
        # 测试全为负整数
        self.assertEqual(mpsa.unit_test([-2, -3, -4])[0], 12)
        # 测试正整数负整数混合
        self.assertEqual(mpsa.unit_test([2, 3, -2, 4])[0], 6)
        # 测试浮点数
        self.assertEqual(mpsa.unit_test([2.0, 3.0, -2.0, 4.0])[0], 6)
        # 测试浮点数整数混合
        self.assertEqual(mpsa.unit_test([2.0, 3.0, -2, 4])[0], 6)

    @patch('builtins.input')
    def test_read_from_stdin(self, mock_input):
        mock_input.return_value = '[2]'
        self.assertEqual(mpsa.unit_test()[0], 2)
        mock_input.return_value = '[-2]'
        self.assertEqual(mpsa.unit_test()[0], -2)
        mock_input.return_value = '[2, 3, 4]'
        self.assertEqual(mpsa.unit_test()[0], 24)
        mock_input.return_value = '[-2, -3, -4]'
        self.assertEqual(mpsa.unit_test()[0], 12)
        mock_input.return_value = '[2, 3, -2, 4]'
        self.assertEqual(mpsa.unit_test()[0], 6)
        mock_input.return_value = '[2.0, 3.0, -2.0, 4.0]'
        self.assertEqual(mpsa.unit_test()[0], 6)
        mock_input.return_value = '[2.0, 3.0, -2, 4]'
        self.assertEqual(mpsa.unit_test()[0], 6)

    def test_read_from_file(self):
        # 和test_read_from_stdin一样
        self.assertEqual(mpsa.unit_test("test_cases/case1.txt")[0], 2)
        self.assertEqual(mpsa.unit_test("test_cases/case2.txt")[0], -2)
        self.assertEqual(mpsa.unit_test("test_cases/case3.txt")[0], 24)
        self.assertEqual(mpsa.unit_test("test_cases/case4.txt")[0], 12)
        self.assertEqual(mpsa.unit_test("test_cases/case5.txt")[0], 6)
        self.assertEqual(mpsa.unit_test("test_cases/case6.txt")[0], 6)
        self.assertEqual(mpsa.unit_test("test_cases/case7.txt")[0], 6)

    @patch('builtins.input')
    def test_error(self, mock_input):
        # 输入数组为空
        self.assertEqual(mpsa.unit_test([]), None)
        # 输入不是列表
        self.assertEqual(mpsa.unit_test((1, 2, 3)), None)
        # 输入格式错误
        mock_input.return_value = "[1, 2, 3"
        self.assertEqual(mpsa.unit_test(), None)
        self.assertEqual(mpsa.unit_test("test_cases/error_case.txt"), None)
        # 数组元素不是int/float
        self.assertEqual(mpsa.unit_test(['a', "b", (1, 2)]), None)
        self.assertEqual(mpsa.unit_test(['a', "b", 'c']), None)
        # 数组维度大于一
        self.assertEqual(mpsa.unit_test([[1, 2, 3], [4, 5, 6]]), None)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [TestMPSA("test_common_case"), TestMPSA("test_read_from_stdin"),
             TestMPSA("test_read_from_file"), TestMPSA("test_error")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
