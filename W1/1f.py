import torch
input=torch.rand(7,7)
r=torch.rand(1,7)
r=r.permute(1,0)
ans=torch.matmul(input,r)
print(ans.size())