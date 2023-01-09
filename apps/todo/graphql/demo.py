import fastberry as fb

# Type(s) Tools
from .. import types


@fb.gql
class Demo:
    """Demo Api"""

    class Meta:
        """GQL-Class Metadata"""

        app = False
        model = "Demo"

    class Query:
        """Query"""

        async def list(info) -> list[types.Product]:
            """Read the Docs"""
            print(info)
            return "Detail"

        async def detail(info) -> types.Product:
            """Read the Docs"""
            print(info)
            return "Detail"

    class Mutation:
        """Mutation"""

        async def create(info) -> str:
            """Read the Docs"""
            print(info)
            return "Create"
