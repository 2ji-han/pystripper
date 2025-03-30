import ast


class CodeTransformer(ast.NodeTransformer):
    def visit_arg(self, node: ast.arg) -> ast.AST:
        node = ast.arg(
            arg=node.arg,
            annotation=None,
            lineno=node.lineno,
            col_offset=node.col_offset,
        )
        return self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        node = ast.FunctionDef(
            name=node.name,
            args=node.args,
            body=node.body,
            decorator_list=node.decorator_list,
            returns=None,
            type_comment=None,
            type_params=[],
            lineno=node.lineno,
            col_offset=node.col_offset,
        )
        return self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
        node = ast.AsyncFunctionDef(
            name=node.name,
            args=node.args,
            body=node.body,
            decorator_list=node.decorator_list,
            returns=None,
            type_comment=None,
            type_params=[],
            lineno=node.lineno,
            col_offset=node.col_offset,
        )
        return self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
        node = ast.ClassDef(
            name=node.name,
            bases=node.bases,
            keywords=node.keywords,
            body=node.body,
            decorator_list=node.decorator_list,
            type_params=[],
            lineno=node.lineno,
            col_offset=node.col_offset,
        )
        return self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> ast.AST:
        assign = ast.Assign(
            targets=[node.target],
            value=node.value or ast.Constant(...),
            lineno=node.lineno,
            col_offset=node.col_offset,
        )
        return assign

    def visit_TypeAlias(self, node: ast.TypeAlias) -> ast.AST:
        return ast.Assign(
            targets=[node.name],
            value=ast.Constant(...),
            lineno=node.lineno,
            col_offset=node.col_offset,
        )


class TypeTransformer(ast.NodeTransformer):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        node.body = [ast.Expr(ast.Constant(...))]
        return self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
        node.body = [ast.Expr(ast.Constant(...))]
        return self.generic_visit(node)
