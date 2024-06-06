from api_requests.simple_books_api import submit_order, get_order


class TestGetSingleOrder:
    def test_get_single_order_with_valid_order_id(self):
        #prima oara plasam o comanda ca sa luam id-ul comenzii
        order_response = submit_order(1, 'Test_user')
        order_id = order_response.json()['orderId']

        #luam detalii despre comanda,cu id-ul de mai sus sa vad daca gaseste comanda
        get_order_response = get_order(order_id)

        #verific daca id-urile coincid si ca s-a plasat bine comanda
        assert order_id == get_order_response.json()['id'], 'Unexpected error'

        assert get_order_response.status_code == 200, 'Unexpected code error'

        print(get_order_response.json())
    #Tema: def test_get_single_order_with_invalid_id(self):