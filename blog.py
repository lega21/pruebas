class Blog:
    def __init__(self, title, author, posts):
        self.title = title
        self.author = author
        self.posts = posts

    def __repr__(self): 
        posts_string = 'post' if len(self.posts) == 1 else 'posts'

        return '{} by {} ({} {})'.format(self.title, self.author, len(self.posts), posts_string)