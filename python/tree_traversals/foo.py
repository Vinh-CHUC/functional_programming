from enum import Enum
from dataclasses import dataclass
import functools
import tempfile
from typing import Generic, Iterable, TypeVar, Optional

import graphviz
import numpy as np

T = TypeVar('T')


@dataclass(frozen=True)
class Tree(Generic[T]):
    val: T
    left: Optional["Tree[T]"]
    right: Optional["Tree[T]"]

    @classmethod
    def BST_from_sequence(cls, seq: Optional[Iterable[int]]) -> Optional["Tree[int]"]:
        if not seq:
            seq = np.random.randint(0, 50, 20)

        return functools.reduce(
            lambda tree, val: insert(tree, val),
            seq,
            Tree(np.random.randint(0, 50, 1)[0], None, None)
        )

    def inorder(self, root: Optional["Tree[T]"] = None) -> Iterable[T]:
        if not root:
            root = self

        return [
            *(self.inorder(root.left) if root.left else []),
            root.val,
            *(self.inorder(root.right) if root.right else [])
        ]

    def _generate_graphviz_dot(self):
        def _helper(tree: "Tree[T]", dot):
            if tree.left:
                dot.edge(str(tree.val), str(tree.left.val))
                _helper(tree.left, dot)
            else:
                none_node_name = str(tree.val) + 'LEFT'
                dot.node(none_node_name, '', color='grey')
                dot.edge(str(tree.val), none_node_name, color='grey')

            if tree.right:
                dot.edge(str(tree.val), str(tree.right.val))
                _helper(tree.right, dot)
            else:
                none_node_name = str(tree.val) + 'RIGHT'
                dot.node(none_node_name, '', color='grey')
                dot.edge(str(tree.val), none_node_name, color='grey')

        dot = graphviz.Digraph()
        _helper(self, dot)
        return dot

    def to_graphviz(self):
        dot = self._generate_graphviz_dot()
        return dot.render(tempfile.NamedTemporaryFile(delete=False, prefix="graphviz").name)


def insert(tree: Tree[int], val: int) -> Tree[int]:
    diff = val - tree.val
    match diff:
        case _ if diff > 0:
            match tree.right:
                case None:
                    return Tree(tree.val, tree.left, Tree(val, None, None))
                case _:
                    return Tree(tree.val, tree.left, insert(tree.right, val))
        case _ if diff < 0:
            match tree.left:
                case None:
                    return Tree(tree.val, Tree(val, None, None), tree.right)
                case _:
                    return Tree(tree.val, insert(tree.left, val), tree.right)
        case _:
            return Tree(val, tree.left, tree.right)
