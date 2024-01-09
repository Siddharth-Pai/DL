print("hello worlddddddd")
import torch
# import pandas as pd
# import matplotlib
#
# scalar= torch.tensor(7)
# print(scalar)
#
# vec= torch.tensor([7,7])
# print(vec)
#
# mat= torch.tensor([[7,8],[6,5]])
# print(mat)
#
tensor= torch.tensor([[[7,8,9],[6,5,4],[12,11,19]]])
print(tensor)

print(tensor.ndim)
# print(tensor.size)
print(torch.cuda.is_available())
print("done")