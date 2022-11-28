# -*- coding: utf-8 -*-
"""
    { Types } for GraphQL
"""

from typing import Optional
import fastberry as fb

# Create your <types> here.
@fb.sql.model
class Task:
    """(Type) Read The Docs"""

    title: str
    description: str
    status: str