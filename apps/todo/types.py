# -*- coding: utf-8 -*-
"""
    { Types } for GraphQL
"""

from typing import Optional
import fastberry as fb

# Create your <types> here.
@fb.sql.model
class Task:
    """Task's Database Table"""

    title: str
    description: str
    status: str


import datetime

# DateTime Functions
class Date:
    datetime = lambda: datetime.datetime.now()
    date = lambda: datetime.date.today()
    time = lambda: datetime.datetime.now().time()


@fb.type
class Product:
    # Other { Type | Model }
    category: Optional["Category"] = None

    # Core { Python }
    name: str | None = None
    aliases: list[str] | None = None
    stock: int | None = None
    is_available: bool | None = None

    # Custom Scalars { GraphQL }
    created_on: fb.datetime = fb.field(Date.datetime)
    available_from: fb.date = fb.field(Date.date)
    same_day_shipping_before: fb.time = fb.field(Date.time)
    price: fb.decimal | None = None
    notes: list[fb.text] = fb.field(list)
    is_object: fb.json = fb.field(dict)

    # Other { Type | Model }
    async def group(self) -> Optional["Group"]:
        """Group Type"""
        return Group(name="awesome")


@fb.type
class Category:
    """(Type) Read The Docs"""

    name: str


@fb.type
class Group:
    """(Type) Read The Docs"""

    name: str
