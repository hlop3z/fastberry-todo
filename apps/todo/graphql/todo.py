# -*- coding: utf-8 -*-
"""
    API - GraphQL
"""

# Fastberry
import fastberry as fb

# Type(s) Tools
from .. import forms, manager, types

# Create your API (GraphQL) here.
@fb.gql
class Todo:
    """Todo Api"""

    class Meta:
        """Meta-Data"""

        app = False
        model = None

    class Query:
        """Query"""

        async def search(status: str | None = None) -> fb.edges(types.Task):
            """(Search-Task) Read the Docs"""
            return await manager.Task.search(status)

        async def detail(item: fb.ID) -> fb.query(types.Task):
            """(Detail-Task) Read the Docs"""
            return await manager.Task.detail(item)

    class Mutation:
        """Mutation"""

        async def create(form: forms.Task) -> fb.mutation(types.Task):
            """(Create-Task) Read the Docs"""
            return await manager.Task.create(form.input)

        async def update(item: fb.ID, status: str) -> fb.mutation(types.Task):
            """(Update-Task) Read the Docs"""
            return await manager.Task.update(item, status)

        async def delete(item: fb.ID) -> bool:
            """(Delete-Task) Read the Docs"""
            return await manager.Task.delete(item)
