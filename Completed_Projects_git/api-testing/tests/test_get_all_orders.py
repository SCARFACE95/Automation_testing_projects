from api_requests.simple_books_api import submit_order, get_all_orders


class TestGetAllOrders:

    def test_get_all_orders(self):
        book_id = 1
        customer_name = 'Py ta 14'
        submit_order_response = submit_order(book_id, customer_name)

        #dictionar
        submit_order_body = submit_order_response.json()
        submit_order_id = submit_order_body['orderId']

        get_orders_response = get_all_orders()

        # lista
        get_orders_body = get_orders_response.json()

        #fiind o lista de dictionare, se apeleaza ind 0 din lista si keya id din dictionar
        get_orders_id = get_orders_body[0]['id']


        #se va returna o lista cu toate comenzile facute, fiind o singura comanda returneaza 1
        assert len(get_orders_response.json()) == 1, 'Unexpected len error'

        #status code
        assert get_orders_response.status_code == 200, 'Unexpected error code'


        #verific primu element din lista cu order id din comanda
        assert submit_order_id == get_orders_id, 'Unexpected command error'



