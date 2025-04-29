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
    list_schools = []
    schools = mongo_collection.find()
    for school in schools:
        if 'topics' in school and school['topics'] is not None:
            for t in school['topics']:
                if t == topic:
                    list_schools.append(school)
    return list_schools
