from model import LeNet
import torch
from PIL import Image
import torchvision.transforms as transforms


def main():
    transform = transforms.Compose(
        [transforms.Resize((28, 28)),
         transforms.ToTensor(),
         transforms.Normalize((0.5), (0.5))])
    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
    net = LeNet()
    net.load_state_dict(torch.load('LeNet.pth'))

    im = Image.open('1.jpg')
    im = transform(im)  # [C, H, W]
    im = torch.unsqueeze(im, dim=0)  # [N, C, H, W]

    with torch.no_grad():
        output = net(im)
        predict = torch.max(output, dim=1)[1]
    print(classes[int(predict)])


if __name__ == '__main__':
    main()
