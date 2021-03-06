# from https://github.com/jayleicn/TVQA/blob/master/model/mlp.py
import torch
import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, in_dim, out_dim, hsz, n_layers):
        super(MLP, self).__init__()

        layers = []
        prev_dim = in_dim
        for i in range(n_layers):
            if i == n_layers - 1:
                layers.append(nn.Linear(prev_dim, out_dim))
            else:
                layers.extend([
                    nn.Linear(prev_dim, hsz[i]),
                    nn.ReLU(True),
                    nn.Dropout(0.0)
                ])
                prev_dim = hsz[i]

        self.main = nn.Sequential(*layers)

    def forward(self, x):
        return self.main(x)


if __name__ == '__main__':
    test_in = torch.randn(10, 300)

    mlp1 = MLP(300, 1, 100, 1)
    print("="*20)
    print(mlp1)
    print(mlp1(test_in).size())

    mlp2 = MLP(300, 10, 100, 2)
    print("="*20)
    print(mlp2)
    print(mlp2(test_in).size())

    mlp3 = MLP(300, 5, 100, 4)
    print("=" * 20)
    print(mlp3)
    print(mlp3(test_in).size())