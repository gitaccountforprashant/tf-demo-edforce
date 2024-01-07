import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_add_numbers(self):
        response = self.app.get("/users/octocat/")
        print(type(response.json))
        l1 = []
        for i in response.json:
            l1.append((i["html_url"].split("/")[-1], i))
        l1.sort()
        l2 = []
        for i, j in l1:
            l2.append(j)
        print(l2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(l2), 8)  # octocat user have total 8 gists
        self.assertEqual(
            l2,
            [
                {
                    "html_url": "https://gist.github.com/octocat/0831f3fbd83ac4d46451",
                    "url": "https://api.github.com/gists/0831f3fbd83ac4d46451",
                },
                {
                    "html_url": "https://gist.github.com/octocat/1162032",
                    "url": "https://api.github.com/gists/1162032",
                },
                {
                    "html_url": "https://gist.github.com/octocat/1169852",
                    "url": "https://api.github.com/gists/1169852",
                },
                {
                    "html_url": "https://gist.github.com/octocat/1169854",
                    "url": "https://api.github.com/gists/1169854",
                },
                {
                    "html_url": "https://gist.github.com/octocat/1305321",
                    "url": "https://api.github.com/gists/1305321",
                },
                {
                    "html_url": "https://gist.github.com/octocat/2a6851cde24cdaf4b85b",
                    "url": "https://api.github.com/gists/2a6851cde24cdaf4b85b",
                },
                {
                    "html_url": "https://gist.github.com/octocat/6cad326836d38bd3a7ae",
                    "url": "https://api.github.com/gists/6cad326836d38bd3a7ae",
                },
                {
                    "html_url": "https://gist.github.com/octocat/9257657",
                    "url": "https://api.github.com/gists/9257657",
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()

# l = [
#     {
#         "html_url": "https://gist.github.com/octocat/6cad326836d38bd3a7ae",
#         "url": "https://api.github.com/gists/6cad326836d38bd3a7ae",
#     },
#     {
#         "html_url": "https://gist.github.com/octocat/0831f3fbd83ac4d46451",
#         "url": "https://api.github.com/gists/0831f3fbd83ac4d46451",
#     },
#     {
#         "html_url": "https://gist.github.com/octocat/2a6851cde24cdaf4b85b",
#         "url": "https://api.github.com/gists/2a6851cde24cdaf4b85b",
#     },
#     {
#         "html_url": "https://gist.github.com/octocat/9257657",
#         "url": "https://api.github.com/gists/9257657",
#     },
#     {
#         "html_url": "https://gist.github.com/octocat/1305321",
#         "url": "https://api.github.com/gists/1305321",
#     },
#     {
#         "html_url": "https://gist.github.com/octocat/1169854",
#         "url": "https://api.github.com/gists/1169854",
#     },
#     {
#         "html_url": "https://gist.github.com/octocat/1169852",
#         "url": "https://api.github.com/gists/1169852",
#     },
#     {
#         "html_url": "https://gist.github.com/octocat/1162032",
#         "url": "https://api.github.com/gists/1162032",
#     },
# ]
l1 = []

for i in l:
    l1.append((i["html_url"].split("/")[-1], i))
