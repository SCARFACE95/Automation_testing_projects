from api_requests.simple_books_api import submit_order


class TestSubmitOrder:

    def test_submit_valid_order(self):
        book_id = 1
        customer_name = 'Py ta 14'

        response = submit_order(book_id,customer_name)

        assert response.status_code == 201, 'Unexpected status code'

        #verificam daca s-a creat comanda
        assert response.json()['created'], 'Unexpected error, order was not submitted'