import torch
import numpy
a = numpy.array([1, 2, 3])
t = torch.from_numpy(a)
print(t)
t[0] = -1
array=t.cpu().numpy()
print(array)
