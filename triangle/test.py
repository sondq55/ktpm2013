from triangle import *
from decimal import *
import math
import unittest


class TesArithmetic(unittest.TestCase):
    def testKiemtra(self):
        self.assertEqual(True,kiemtra(2.0,4.0,5.0))

    def testint(self):
        self.assertEqual(False,kiemtra(1,4,5))
        
    def testFalse(self):
        self.assertEqual(False,kiemtra(0,4.0,5.0))

    def testSoam(self):
        self.assertEqual(False,kiemtra(-1,-4,-5))
    
    def testKitu(self):
        self.assertEqual(False,kiemtra('hello',4.0,5.0))
        
    def testTamgiacthuong(self):
        self.assertEqual('Tam giac thuong', detect_triangle(2.0,3.0,4.0))
        
    def testTamgiacvuongtaiC(self):
        result = detect_triangle(3,4,5)
        self.assertEquals(result,'Tam giac vuong tai C')

    def testTamgiacvuongtaiB(self):
        result = detect_triangle(3,5,4)
        self.assertEquals(result,'Tam giac vuong tai B')

    def testTamgiacvuongtaiA(self):
        result = detect_triangle(5,4,3)
        self.assertEquals(result,'Tam giac vuong tai A')
        
    def testCantaiC(self):
        result = detect_triangle(2,2,3)
        self.assertEquals(result,'can tai C')
    def testCantaiB(self):
        result = detect_triangle(8,4,8)
        self.assertEquals(result,'can tai B')
    def testCantaiA(self):  
        result = detect_triangle(6,9,9)
        self.assertEquals(result,'can tai A')

    def testTamgiacbisuybien(self):
        self.assertEqual('Tam giac bi suy bien', detect_triangle(6,24,30))
      
    def testKhongphailatamgiac(self):
        self.assertEqual('Khong phai la tam giac', detect_triangle(-1,2,3))
        
    def testTamgiacdeu(self):
        self.assertEqual('Tam giac deu', detect_triangle(8,8,8))

    def testTamgiacvuongcantaiA(self):
        result = detect_triangle(4,math.sqrt(8),math.sqrt(8))
        self.assertEquals(result,'Tam giac vuong can tai A')
        
    def testTamgiacvuongcantaiB(self):
        result = detect_triangle(math.sqrt(5),math.sqrt(10),math.sqrt(5))
        self.assertEquals(result,'Tam giac vuong can tai B')

    def testTamgiacvuongcantaiC(self):
        result = detect_triangle(math.sqrt(4),math.sqrt(4),math.sqrt(8))
        self.assertEquals(result,'Tam giac vuong can tai C')
        
unittest.main()
