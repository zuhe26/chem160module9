A=2
print(A)
B=A
print(B)
A=5
print(B)
print("========")
A= [2,14,7]
print(A)
B=A
print(B)
A[0]=5
print(B)
print("=======")
import copy
A=[2,14,7]
print(A)
B=copy.copy(A)
print(B)
A[0]=5
print(B)