import torch

from torch.autograd import Variable

from group_norm import GroupNormMoving, GroupNorm

if __name__ == "__main__":
    m = GroupNormMoving(64)
    input = Variable(torch.randn(3, 64, 32, 32))

    output = m(input)
    print(output.size())
