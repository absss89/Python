class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"제목: {self.title}, 저자: {self.author}, 가격: {self.price}원")

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.price == other.price
        return False
