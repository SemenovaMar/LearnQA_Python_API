import requests
class Test2Cookies:
    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.text)
        print(response.status_code)
        print(dict(response.cookies))
        code = response.status_code
        assert code == 200