import fastberry as fb
import strawberry
from enum import Enum

# Type(s) Tools
from .. import types


@strawberry.enum
class IceCreamFlavour(Enum):
    VANILLA = "vanilla"
    STRAWBERRY = "strawberry"
    CHOCOLATE = "chocolate"


@fb.gql
class Demo:
    """Demo Api"""

    class Meta:
        """GQL-Class Metadata"""

        app = False
        model = "Demo"

    class Query:
        """Query"""

        async def ice_cream(info) -> IceCreamFlavour:
            """Read the Docs"""
            print(info)
            return "Detail"

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
