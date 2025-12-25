print("Python 101/ Medium Ex.1" )

def three_Sum(num):
    num.sort()
    print(num)
    
    for i in range(len(num)-2):
        left= i + 1
        right = len(num) - 1
        print(left,right)



num =  [-1,0,1,2,-1,-4]
three_Sum(num)
input("Press Enter to exit...") 