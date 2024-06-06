from api_requests.simple_books_api import get_api_status


class TestApiStatus:

    def test_api_status_code_and_body(self):
        #am apelat functia si returneaza response in response
        response = get_api_status()

        #assert pe status code
        assert response.status_code == 200, 'Unexpected status code'
        #assert pe body
        assert response.json()['status'] == 'OK', 'Unexpected body'



