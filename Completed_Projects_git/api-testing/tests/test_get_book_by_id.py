from api_requests.simple_books_api import get_book_by_id


class TestGetBookById():
    def test_get_book_by_valid_id(self):
        response = get_book_by_id(book_id=5)

        assert response.status_code == 200, 'Unexpected error'
        assert  response.json()['id'] == 5



#Tema def_get_book_by_invalid_id(self)