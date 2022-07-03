
class Post():

    def __init__(self, _id, _author, _text):
        self._id = None
        self._set_id(_id)
        
        self._date = None
        self._set_date()
        
        self._author = None
        self._set_author(_author)
        
        self._text = None
        self._set_text(_text)


    def __del__(self):
        print("deleted")


    def _set_id(self, _id):
        self._id =_id


    def _set_date(self):
        import datetime
        self._date = datetime.datetime.now().strftime("%d.%m.%Y %H:%m:%S")


    def _set_author(self, _author):
        self._author = _author


    def _set_text(self, _text):
        self._text = _text


    @property
    def get_id(self):
        return self._id


    @property
    def get_date(self):
        return self._date


    @property
    def get_author(self):
        return self._author


    @property
    def get_text(self):
        return self._text


    @property
    def get_data(self):
        return {"id":self.get_id, "date": self.get_date, "author": self.get_author, "text": self.get_text}


    @property
    def get_data_str(self):
        return f'{self.get_id}. {self.get_date} {self.get_author} posted: "{self.get_text}"'


class Comment(Post):

    def __init__(self, _id, _author, _text, _post_id):
        Post.__init__(self, _id, _author, _text)
        
        self._post_id = None
        self._set_post_id(_post_id)


    def _set_post_id(self, _post_id):
        self._post_id = _post_id

    @property
    def get_post_id(self):
        return self._post_id


    @property
    def get_data(self):
        return {"id":self.get_id, "post_id": self.get_post_id, "date": self.get_date, "author": self.get_author, "text": self.get_text}


    @property
    def get_data_str(self):
        return f'{self.get_id}. {self.get_date} {self.get_author} commented: "{self.get_text} on post with id of {self.get_post_id}"'


if __name__ == "__main__":
    import time

    kenobi_post = Post(1, "Obi-Wan Kenobi", "Hello there!")
    time.sleep(5)

    grievous_comment1 = Comment(1, "General Grievous", "General Kenobi!", kenobi_post.get_id)
    time.sleep(3)

    grievous_comment2 = Comment(2, "General Grievous", "You are a bold one.", kenobi_post.get_id)
    time.sleep(3)

    grievous_comment3 = Comment(3, "General Grievous", "Kill him!", kenobi_post.get_id)

    print(kenobi_post.get_data)
    print(grievous_comment1.get_data)
    print(grievous_comment2.get_data)
    print(grievous_comment3.get_data)