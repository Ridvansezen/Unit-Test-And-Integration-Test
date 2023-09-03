import requests
import unittest

class IntegrationTest(unittest.TestCase):

    def test_api_integration(self):
        # API'ye GET isteği gönderip yanıtı kontrol edelim
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

        # Yanıtın durumu 200 (Başarılı) olmalı
        self.assertEqual(response.status_code, 200)

        # JSON yanıtını alalım
        data = response.json()

        # JSON yanıtının belirli bir anahtarını kontrol edelim
        self.assertEqual(data['userId'], 1)

if __name__ == '__main__':
    unittest.main()
