#!/usr/bin/env python3
from typing import Collection, List
"""
function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection: Collection, topic: str) -> List[str]:
    """
    function that returns the list of school having a specific topic
    argv:
        mongo_collection
        topic: string
    Returns: a list
    """
    return (mongo_collection.find({'topics': topic}))
