from api_requests.simple_books_api import submit_order, delete_order, get_order


class TestDeleteOrder:
    def test_delete_user(self):
        submit_order_response = submit_order(1, 'TestUser1')

        # scoatem id-ul comenzii, comanda plasat init are id-ul de mai jos
        order_id = submit_order_response.json()['orderId']

        delete_response = delete_order(order_id)
        assert delete_response.status_code == 204, 'Unexpected error message'

        get_order_reponse = get_order(order_id)
        expected_error_text = f"No order with id {order_id}."
        actual_error_text = get_order_reponse.json()['error']

        assert expected_error_text == actual_error_text , 'Unexpected error text'


