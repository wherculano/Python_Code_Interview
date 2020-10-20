"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
For example:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Source: https://www.programcreek.com/2012/12/leetcode-evaluate-reverse-polish-notation/
"""
import operator
from typing import List


class InvalidExpression(Exception):
    pass


def reverse_polish_notation(expression: List[str]) -> int:
    """
    >>> reverse_polish_notation(["2", "1", "+", "3", "*"])
    9
    >>> reverse_polish_notation(["4", "13", "5", "/", "+"])
    6

    """
    stack = []
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.floordiv
                 }
    for operator_operand in expression:
        try:
            num = int(operator_operand)
            stack.append(num)
        except ValueError:
            op = operator_operand
            try:
                operand_2 = stack.pop()
            except IndexError:
                raise InvalidExpression(f'Missing some operands: {expression}')
            try:
                operand_1 = stack.pop()
            except IndexError:
                raise InvalidExpression(f'Missing some operands: {expression}')

            func = operators[op]
            result = func(operand_1, operand_2)
            stack.append(result)

    if len(stack) > 1:
        raise InvalidExpression(
            f'There are to much (or missing) some operands/operators in the expression: {expression}')
    return stack.pop()
