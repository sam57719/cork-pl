from nodes import *
from values import *


class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.__not_implemented)
        return method(node)

    def __not_implemented(self, node):
        raise NotImplementedError(f'{node.__class__.__name__} not implemented properly')

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a) + self.visit(node.node_b))

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a) - self.visit(node.node_b))

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a) * self.visit(node.node_b))

    def visit_DivideNode(self, node):
        return Number(self.visit(node.node_a) / self.visit(node.node_b))

    def visit_PlusNode(self, node):
        return Number(+self.visit(node.node))

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node))

    def visit_FloorNode(self, node):
        return Number(self.visit(node.node_a) // self.visit(node.node_b))

    def visit_ModNode(self, node):
        return Number(self.visit(node.node_a) % self.visit(node.node_b))

    def visit_PowerNode(self, node):
        return Number(self.visit(node.node_a) ** self.visit(node.node_b))
