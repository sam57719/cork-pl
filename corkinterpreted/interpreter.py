from decorators import skip_if_error
from values import *


class Interpreter:
    def __init__(self):
        self.error = None

    @skip_if_error
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.__not_implemented)
        return method(node)

    def __not_implemented(self, node):
        raise NotImplementedError(f'{node.__class__.__name__} not implemented properly')

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        result, self.error = self.visit(node.node_a) + self.visit(node.node_b)
        return result

    def visit_SubtractNode(self, node):
        result, self.error = self.visit(node.node_a) - self.visit(node.node_b)
        return result

    def visit_MultiplyNode(self, node):
        result, self.error = self.visit(node.node_a) * self.visit(node.node_b)
        return result

    def visit_DivideNode(self, node):
        result, self.error = self.visit(node.node_a) / self.visit(node.node_b)
        return result

    def visit_PlusNode(self, node):
        result, self.error = +self.visit(node.node)
        return result

    def visit_MinusNode(self, node):
        result, self.error = -self.visit(node.node)
        return result

    def visit_FloorNode(self, node):
        result, self.error = self.visit(node.node_a) // self.visit(node.node_b)
        return result

    def visit_ModNode(self, node):
        result, self.error = self.visit(node.node_a) % self.visit(node.node_b)
        return result

    def visit_PowerNode(self, node):
        result, self.error = self.visit(node.node_a) ** self.visit(node.node_b)
        return result
