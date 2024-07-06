

class Book:
    def __init__(self, title, page_count):
        self.title = title  
        self.page_count = page_count  
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            raise ValueError("Title must be a string")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        elif value <= 0:
            raise ValueError("Page count must be a positive integer")
        else:
            self._page_count = value
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        