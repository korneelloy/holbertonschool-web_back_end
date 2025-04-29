#!/usr/bin/env python3
"""update mongo collection"""
from typing import Collection, List


def update_topics(mongo_collection: Collection, name: str, topics: List[str]):
    """
    update mongo collection
    argv :  mongo_collection: collection
    name: string
    topics: list of strings
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
