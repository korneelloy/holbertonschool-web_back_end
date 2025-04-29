#!/usr/bin/env python3
"""list all elements of a mongodb database"""

from typing import List, Collection


def list_all(mongo_collection: Collection) -> List:
    """returning list based upon db collection"""
    list = []
    list = mongo_collection.find()
    return list
