a, b=int(input()), int(input())
a, b=a*b, 2*(a+b)
print("Area"*(a>b)+"Peri"*(b>a)+"Eq"*(b==a),a+(b>a)*(b-a),sep='\n')