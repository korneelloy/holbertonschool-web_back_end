#!/usr/bin/env python3
"""insert elements of a mongodb database"""

from typing import Dict, Collection


def insert_school(mongo_collection: Collection,
                  **kwargs: Dict[str, str]) -> int:
    """insert element in db collection"""

    result = mongo_collection.insert_one({
        'name': kwargs['name'],
        'address': kwargs['address']
    })

    return (result.inserted_id)
