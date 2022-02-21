from decorators import check_for_instance_error
from values import *


# noinspection PyArgumentList
class Interpreter:
    def __init__(self):
        self.error = None

    @check_for_instance_error(method_has_return=True, check_before=False)
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.__not_implemented)
        return method(node)

    def __not_implemented(self, node):
        raise NotImplementedError(f'{node.__class__.__name__} not implemented properly')

    # noinspection PyMethodMayBeStatic
    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        result, self.error = self.visit(node.node_a) + self.visit(node.node_b)
        return Number(result)

    def visit_SubtractNode(self, node):
        result, self.error = self.visit(node.node_a) - self.visit(node.node_b)
        return Number(result)

    def visit_MultiplyNode(self, node):
        result, self.error = self.visit(node.node_a) * self.visit(node.node_b)
        return Number(result)

    def visit_DivideNode(self, node):
        result, self.error = self.visit(node.node_a) / self.visit(node.node_b)
        return Number(result)

    def visit_PlusNode(self, node):
        result, self.error = +self.visit(node.node)
        return Number(result)

    def visit_MinusNode(self, node):
        result, self.error = -self.visit(node.node)
        return Number(result)

    def visit_FloorNode(self, node):
        result, self.error = self.visit(node.node_a) // self.visit(node.node_b)
        return Number(result)

    def visit_ModNode(self, node):
        result, self.error = self.visit(node.node_a) % self.visit(node.node_b)
        return Number(result)

    def visit_PowerNode(self, node):
        result, self.error = self.visit(node.node_a) ** self.visit(node.node_b)
        return Number(result)
