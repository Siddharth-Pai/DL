import torch
# print(torch.cuda.is_available())
input=torch.tensor([[2,3],[4,5]])
print(input)
ele=input[0][1] #print 1st element from the 0th list
print(ele)

