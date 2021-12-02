import os
import json
import torch
import torch.nn as nn
from model import AlexNet
import torch.optim as optim


def main():
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f"using {device} device.")
    net = AlexNet()
    batch_size, lr, num_epochs = 256, 0.001, 10
    loss_function = nn.CrossEntropyLoss()
    optimizer = optim.Adam(net.parameters(), lr=lr)


    # data


    # train
    for epoch in range(num_epochs):
        pass

    # save
    save_path = './AlexNet.pth'
    torch.save(net.state_dict(), save_path)
    print('finished training')


if __name__ == '__main__':
    main()
