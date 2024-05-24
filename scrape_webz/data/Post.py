class Post:
    """class which holds a post, to format easilly to json"""

    def __init__(self, title: str, content: str, author: str, date: str):
        self.title = title
        self.text = content
        self.author = author
        self.published = date  # the date should be in the right format // h:m
