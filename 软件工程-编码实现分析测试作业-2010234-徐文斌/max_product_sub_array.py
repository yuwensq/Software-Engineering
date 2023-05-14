# -*- coding: UTF-8 -*-
"""
@Project: 最大乘积子数组
@File: max_product_sub_array.py
@Author: 徐文斌2010234
"""
from ast import literal_eval
import numpy as np


class MaxProductSubArray:
    """
    用于计算数组中最大乘积子数组
    """
    def __init__(self):
        """
        初始化函数
        array为数组，legal表示数组是否合法
        """
        self.array = []
        self.legal = True

    def __on_solve(self, nums):
        """
        计算一维数组最大乘积子数组O(N)算法
        :param nums: 待处理的一维数组
        :return: 最大乘积以及对应的子数组内容
        """
        if not self.legal:
            return None
        res_val = min(nums)
        nums_len = len(nums)
        f_max = [0] * nums_len
        f_min = [0] * nums_len
        f_max[0] = nums[0]
        f_min[0] = nums[0]
        res_list = []
        for i in range(1, nums_len):
            f_max[i] = max(f_max[i - 1] * nums[i], f_min[i - 1] * nums[i], nums[i])
            f_min[i] = min(f_max[i - 1] * nums[i], f_min[i - 1] * nums[i], nums[i])
            if f_max[i] > res_val:
                res_val = f_max[i]
        for i in range(nums_len):
            if f_max[i] == res_val:
                tmp_val = nums[i]
                res_list.append(nums[i])
                for j in range(i - 1, -1, -1):
                    if tmp_val == res_val and nums[j] != 1:
                        break
                    tmp_val = tmp_val * nums[j]
                    res_list.append(nums[j])
                break
        res_list.reverse()
        return res_val, res_list

    def __read_array_from_stdin(self):
        """
        从标准输入中读取数组
        :return: 读取到的数组
        """
        res_list = self.array
        try:
            res_list = literal_eval(input("请输入数组，输入格式参照[1, 2, 3, 4]: "))
        except (SyntaxError, ValueError):
            print("输入格式不合法")
            res_list = None
        return res_list

    def __read_array_from_file(self, file_path):
        """
        从文件中读取数组
        :param file_path: 文件路径
        :return: 返回读取到的数组
        """
        res_list = self.array
        with open(file=file_path, mode='r', encoding='UTF-8') as file:
            try:
                res_list = literal_eval(file.read())
            except(SyntaxError, ValueError):
                print("文件读取失败!")
                res_list = None
        return res_list

    def __solve(self):
        """
        根据数组的维度来进行对应的计算
        :return: 最大乘积以及对应的子数组
        """
        res = None
        tmp = np.array(self.array)
        if len(tmp.shape) == 1:
            res = self.__on_solve(self.array)
        else:
            print("多维数组暂未支持")
        return res

    def array_is_legal(self):
        """
        检查self.array是否合法，不为空，且元素是int/float
        :return: True表示合法，False表示不合法
        """
        res = True
        if isinstance(self.array, list):
            if not self.array:
                res = False
                print("输入数组为空")
            else:
                try:
                    tmp = np.array(self.array)
                except ValueError:
                    res = False
                    print("数组格式错误")
                    return res
                if len(tmp.shape) == 1:
                    for ele in self.array:
                        try:
                            assert isinstance(ele, (int, float))
                        except AssertionError:
                            res = False
                            print("数组元素类型非法!")
                            return res
                else:
                    res = False
                    print("暂不支持多维数组")
        else:
            res = False
            print("输入数组不是以列表形式")
        return res

    def set_array(self, source=None):
        """
        根据参数初始化self.array数组
        :param source: 可以传入一个列表或字符串或为空，如果传入字符串，会从对应的文件中读取数组；
        如果为空，则从标准输入读取
        :return: None
        """
        input_array = source
        # 在从文件读取的时候不对数组进行类型检查
        if source is None:
            input_array = self.__read_array_from_stdin()
        elif isinstance(source, str):
            input_array = self.__read_array_from_file(source)
        self.array = input_array
        # 最终调用array_is_legal统一进行数组检查
        self.legal = self.array_is_legal()

    def solve(self):
        """
        计算数组最大乘积子数组，用户接口
        :return: 最大乘积以及对应的子数组内容
        """
        if not self.legal:
            print("错误，无法计算")
            return None
        res = self.__solve()
        return res


def profile_test(scale):
    """
    性能测试函数
    :param scale: 测试数组规模
    :return: None
    """
    test_array = [np.random.randint(-10, 10) for i in range(scale)]
    mpsa = MaxProductSubArray()
    mpsa.set_array(test_array)
    mpsa.solve()


def unit_test(source=None):
    """
    单元测试代码
    :param source: 输入数组
    :return: 最大乘积子数组结果
    """
    mpsa = MaxProductSubArray()
    mpsa.set_array(source)
    return mpsa.solve()


if __name__ == '__main__':
    MPSA = MaxProductSubArray()
    MPSA.set_array()
    print(MPSA.solve())
