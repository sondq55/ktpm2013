import input
import unittest
import itertools

ar = []
arr =[]
string = input.main.__doc__
i = 0
j = -1
k = 0
while(i<len(string)):
    tmp = ''
    if(string[i]=='['):
        k = i+1
        while(string[k]!=';'):
            tmp += string[k]
            k+=1
        a = int(tmp)
        tmp = ''
        k+=1
        while(string[k]!=']'):
            tmp += string[k]
            k+=1
        b = int(tmp)
        arr[j].append(a)
        arr[j].append(b)
        ar[j].append((a+b)/2)
        tmp = ''
            
    if((i+1)<len(string) and string[i+1]==':'):
        j+=1
        ar.append([])
        arr.append([])
        
    i+=1
print "\n",arr

for i in range (0, len(arr) ):
        for j in range(0, len(arr[i])-2,2):
            if (arr[i][j+2]-arr[i][j+1])*(arr[i][j+3]-arr[i][j]) < 0:
                raise Exception("Dau vao sai")
            if len(arr[i]) > 4 and ( arr[i][4]-arr[i][1])*(arr[i][5]-arr[i][0]) < 0 :
                raise Exception("Dau vao sai")
                      
print ar

class output(unittest.TestCase):
    pass

def test_generator(*args):
    def Test(self):
        return self.assertEqual("Test",input.main(*args),1)
    #return Test
if __name__ == '__main__':
    for e in itertools.product(*ar):
        print e
        test_name = 'test_%s' + str(e)
        test = test_generator(*e)
        setattr(output, test_name, test)
    unittest.main()
