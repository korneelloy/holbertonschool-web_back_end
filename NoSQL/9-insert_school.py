#!/usr/bin/env python3
"""insert elements of a mongodb database"""

from typing import Dict, Collection


def insert_school(mongo_collection: Collection,
                  **kwargs: Dict[str, str]) -> int:
    """insert element in db collection"""
    new_dict = {}

    for key, value in kwargs.items():
        new_dict[key] = value

    result = mongo_collection.insert_one(new_dict)

    return (result.inserted_id)
