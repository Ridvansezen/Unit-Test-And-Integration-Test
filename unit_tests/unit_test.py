import unittest

# Örnek bir fonksiyon
def toplama(a, b):
    return a + b

# Testler için bir test sınıfı
class TestToplama(unittest.TestCase):
    
    def test_toplama(self):

        a = 2  
        b = 3  
        beklenen_sonuc = 5  

        sonuc = toplama(a, b)
        self.assertEqual(sonuc, beklenen_sonuc, "Toplama işlemi hatalı")


def cikarma(a,b):
    return a - b

class TestCikarma(unittest.TestCase):

    def test_cikarma(self):

        a = 5
        b = 4

        sonuc = cikarma(a, b)
        self.assertEqual(sonuc, 1, "Çıkarma işlemi hatalı")


def carpma(a,b):
    return a * b

class TestCarpma(unittest.TestCase):

    def test_carpma(self):

        a = 8
        b = 6

        sonuc = carpma(a, b)
        self.assertEqual(sonuc, 48, "Çarpma işlemi hatalı")


def bolme(a,b):
    return a / b

class TestBolme(unittest.TestCase):

    def test_bolme(self):

        a = 9
        b = 3

        sonuc = bolme(a, b)
        self.assertEqual(sonuc, 3, "Bölme işlemi hatalı")

if __name__ == "__main__":
    unittest.main()
