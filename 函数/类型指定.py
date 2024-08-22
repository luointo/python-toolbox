# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
对函数的参数和返回值进行指定类型和检查

python一直以来都不是开发大工程的主流语言，不管是前端还是后端，主要的原因其实就是以下几点：

python是解释性语言，运行效率比java等语言慢；
python是动态语言，在后期维护的成本非常高，很重要的一点就是没有进行类型检查，当然还包括新建变量不需要声明以及指定类型等等。
但是，在python3.5之后，就新增了对函数参数和返回值的类型指定和检查，以及在新建变量时也可以指定类型

"""

from typing import List, Dict, Tuple, Sequence, TypeVar, Union, NamedTuple


# 基本类型指定
def f(a: int, b: str) -> str:
    print(a, b)
    return "res"


res = f(1, "a")
print(res)

# 更为复杂的指定
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


new_vector = scale(2.0, [1.0, -4.2, 5.4])

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...


def broadcast_message(
        message: str,
        servers: Sequence[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:
    ...


"""
这里需要注意，元组这个类型是比较特殊的，因为它是不可变的。所以，当我们指定Tuple[str, str]时，就只能传入长度为2，并且元组中的所有元素都是str类型
"""

# 泛型指定
T = TypeVar('T')  # 声明类型变量, 可以是任何东西


def first(l: Sequence[T]) -> T:  # Generic function
    return l[0]


A = TypeVar('A', str, bytes)  # Must be str or bytes
B = Union[str, None]  # Must be str or None


# 创建变量时的类型指定
class Employee(NamedTuple):
    name: str
    id: int = 3


employee = Employee('Guido')
assert employee.id == 3
