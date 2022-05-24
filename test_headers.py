import requests
class Test2Cookies:
    def test_headers(self):
        response1 = requests.post("https://playground.learnqa.ru/api/homework_header")
        print(response1.headers)
        print(response1.status_code)
        a =response1.headers
        b = response1.status_code
        assert b == 200 and a == response1.headers





1