import requests
class Test2Cookies:
    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.text)
        print(dict(response.cookies))
        name = response.text
        assert name == response.text

