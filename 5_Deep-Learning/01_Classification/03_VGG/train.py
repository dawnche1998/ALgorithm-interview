import torch
from torch import nn
from model import vgg
from torchvision import transforms


def main():
    # basic
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"using {device} device.")
    # net
    net = vgg(model_name='vgg16')

    # data
    data_transform = {
        "train": transforms.Compose([transforms.RandomResizedCrop(224),
                                     transforms.RandomHorizontalFlip(),
                                     transforms.ToTensor(),
                                     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]),
        "val": transforms.Compose([transforms.Resize((224, 224)),
                                   transforms.ToTensor(),
                                   transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])}


    # train
    batch_size, lr, num_epochs = 256, 0.001, 5
    optimizer = torch.optim.Adam(net.parameters(), lr)
    loss_function = nn.CrossEntropyLoss()
    best_acc = 0.0
    for epoch in range(num_epochs):
        print("training on")
        net.train()
        running_loss = 0.0


if __name__ == '__main__':
    main()
