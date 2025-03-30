from .transformer import CodeTransformer, TypeTransformer
import ast
import copy
from pathlib import Path


def transform_to_types(ast: ast.AST) -> ast.AST:
    transformer = TypeTransformer()
    type_ast = transformer.visit(ast)
    return type_ast


def transform_to_code(ast: ast.AST) -> ast.AST:
    transformer = CodeTransformer()
    code_ast = transformer.visit(ast)
    return code_ast


def strip(path: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    module = ast.parse(path.read_text(encoding="utf-8"))
    type_ast = transform_to_types(copy.deepcopy(module))
    code_ast = transform_to_code(copy.deepcopy(module))
    dest.with_suffix(".py").write_text(ast.unparse(code_ast), encoding="utf-8")
    dest.with_suffix(".pyi").write_text(ast.unparse(type_ast), encoding="utf-8")


def strip_dir(path: Path, dest: Path):
    for child in path.glob("**/*"):
        if child.is_dir():
            continue
        relative = child.relative_to(path)
        dest_child = dest / relative
        dest_child.parent.mkdir(parents=True, exist_ok=True)
        if child.suffix == ".pyi":
            dest_child.write_bytes(child.read_bytes())
        elif child.suffix == ".py":
            strip(child, dest_child)
        else:
            dest_child.write_bytes(child.read_bytes())


__all__ = [
    "strip",
    "strip_dir",
    "CodeTransformer",
    "TypeTransformer",
]
__version__ = "0.1.0"
