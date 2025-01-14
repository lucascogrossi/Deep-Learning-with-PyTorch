import torch

print(f"PyTorch version: {torch.__version__}")

x = torch.tensor([1, 2, 3, 4, 5])
print(f"Tensor: {x}")

y = x + 1
print(f"Tensor + 1: {y}")

print(f"Tensor device: {x.device}") 
print(f"Tensor dtype: {x.dtype}")