from dataclasses import dataclass
from typing import List

"""
for example:
"thread_url": "https://reddit.com/r/BeAmazed/comments/166kz5m/this_took_my_brain_longer_than_it_should_have/",
    "thread_title": "This Took my brain longer than it should have.. 😂",
    "thread_id": "166kz5m",
    "is_nsfw": False,
    "comments": [
        {
            "comment_body": "Mirror",
            "comment_url": "/r/BeAmazed/comments/166kz5m/this_took_my_brain_longer_than_it_should_have/jykfj60/",
            "comment_id": "jykfj60",
        }]
"""


@dataclass
class Comment:
    comment_body: str
    comment_url: str
    comment_id: str


@dataclass
class Content:
    thread_url: str
    thread_title: str
    thread_id: str
    is_nsfw: bool
    comments: List[Comment]
