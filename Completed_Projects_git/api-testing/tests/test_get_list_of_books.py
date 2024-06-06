from api_requests.simple_books_api import get_list_of_books


class TestGetListOfBooks:

    def test_get_list_of_books_without_filter(self):
        response = get_list_of_books()
        assert response.status_code == 200, 'Unexpected status code'

        body = response.json() #in variabila asta am toate rezultatele de books

        assert len(body) == 6, "Unexpected number of books returned"


    def test_get_list_of_books_filter_by_type(self):
        response = get_list_of_books(book_type='fiction')
        body = response.json()
        assert len(body) == 4, "Unexpected number of books returned"

        #verific ca toate cele 4 carti au ca tipe fiction conform filtrului adaugat in test
        for book in body:
            assert book['type'] == 'fiction'

    def test_get_list_of_books_filter_by_limit(self):
        response = get_list_of_books(limit_size=2)
        body = response.json()

        assert response.status_code == 200, 'Unexpected status code'
        assert len(body) == 2, "Limit is not in range"


    #Negative limit error
    def test_get_list_of_books_filter_by_invalid_limit_less_than_0(self):
        response = get_list_of_books(limit_size=-5)


        assert response.status_code == 400, 'Unexpected status code'

        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 0."
        actual_error_message = response.json()['error']
        assert expected_error_message == actual_error_message, 'Unexpected error message'


    def test_get_list_of_books_filter_by_invalid_limit_greater_than_20(self):
        response = get_list_of_books(limit_size=22)

        assert response.status_code == 400, 'Unexpected status code'

        expected_error_message = "Invalid value for query parameter 'limit'. Cannot be greater than 20."
        actual_error_message = response.json()['error']
        assert expected_error_message == actual_error_message, 'Unexpected error message'
