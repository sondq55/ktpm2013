#kiem tra(a,b,c) co phai la 3 canh cua tam giac khong
#import math
def kiemtra(a,b,c):
    if type(a)== float and type(b) == float and type(c) == float:
        if 0<a<((2**32)-1) and 0<b<((2**32)-1) and 0<c<((2**32)-1):
            return True
    return False
def detect_triangle(a,b,c):
    if (True) and (a+b)>=c and (a+c)>=b and (b+c)>=a and (a>0) and (b>0) and (c>0):#Kiem tra day co phai la ba canh cua tam giac
        if(a==b) and (b==c):#Tam giac deu
            return 'Tam giac deu'
        elif(((round((a*b),1)+round((b*b),1)==round((c*c),1))and(a==b))):#Tam giac vuong can
            return 'Tam giac vuong can tai C'
        elif(((round((a*c),1)+round((c*c),1)==round((b*b),1))and (a==c))):
            return 'Tam giac vuong can tai B'
        elif(((round((c*b),1)+round((b*b),1)==round((a*a),1))and(c==b))):
            return 'Tam giac vuong can tai A'
        #Tam giac can
        elif(a==b):
            return 'can tai C'
        elif(b==c):
            return 'can tai A'
        elif(c==a):
            return 'can tai B'
        elif(a*a==b*b+c*c):#Tam giac vuong
            return 'Tam giac vuong tai A'
        elif(b*b==a*a+c*c):
            return 'Tam giac vuong tai B'
        elif(c*c==a*a+b*b):
            return 'Tam giac vuong tai C'
        elif((a+b==c)or(c+b==a)or(c+a==b)):
            return 'Tam giac bi suy bien'
        else:			#Tam giac thuong
            return 'Tam giac thuong'
    else:				#Khong phai la 3 canh cua tam giac
            return 'Khong phai la tam giac'

