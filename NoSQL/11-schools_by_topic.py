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
        if 'topics' in school and topic in school['topics']:
            list_schools.append(school)
    return list_schools
