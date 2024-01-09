import torch
input = torch.randn(2,2)
print(input.size())
per=input.permute(1,0)
print(per)
per=input.permute(0,1)
print(per)