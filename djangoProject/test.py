import requests
from django.test import TestCase

from djangoProject.processors.api_processor import ApiProcessor, POSTS_URL

ACTUAL_LONGEST_COMMENT = "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"

class ApiTestCase(TestCase):
    def setUp(self):
        pass

    def test_longest_comment_format(self):
        dict = {
            'postId': None,
            'id': None,
            'name': None,
            'email': None,
            'body': None
        }

        longest_comment = ApiProcessor.longest_comment()
        self.assertEqual(longest_comment.keys(), dict.keys(), "Attributes do not match.")


    def test_longest_comment(self):
        potentially_longest_comment = ApiProcessor.longest_comment()['body']
        self.assertEqual(ACTUAL_LONGEST_COMMENT, potentially_longest_comment, "This is not the longest comment.")


    def test_post_with_longest_title_format(self):
        dict = {
            'userId': None,
            'id': None,
            'title': None,
            'body': None
        }

        post = ApiProcessor.post_with_longest_title()
        self.assertEqual(post.keys(), dict.keys(), "Attributes do not match.")

    def test_post_with_longest_title(self):
        #Not sure how good it is to have an API call in a Unit test, but put it anyways.
        data = requests.get(POSTS_URL).json()
        longest = {
            "size": len(data[0]["title"]),
            "value": data[0]["title"]


        }

        for post in data:
            if len(post["title"]) > longest["size"]:
                longest["size"] = len(post["title"])
                longest["value"] = post["title"]

        potentionally_longest_title = ApiProcessor.post_with_longest_title()["title"]

        self.assertEqual(potentionally_longest_title, longest["value"], "Wrong output.")
