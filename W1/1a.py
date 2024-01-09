import torch
import pandas as pd

a = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8])
print(a.reshape([4,2]))

print(a.view(4, 2))
print(a.view(2,4))

# creating tensors
x = torch.tensor([1., 3., 6., 10.])
y = torch.tensor([2., 7., 9., 13.])

# join above tensor using "torch.stack()"
print("join tensors:")
t = torch.stack((x, y))
print(t)

input = torch.randn(3,1,2,1,4)
print(input.size())
output = torch.squeeze(input)
print(output.size())

unsqueez=torch.unsqueeze(output, dim=2)
print(unsqueez.size())
