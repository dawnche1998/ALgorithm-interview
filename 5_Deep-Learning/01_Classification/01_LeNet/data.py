import torchvision
import torch
import torchvision.transforms as transforms
import matplotlib.pyplot as plt


class FashionMNIST:
    def __init__(self):
        self.mnist_train = torchvision.datasets.FashionMNIST(root='../Datasets', train=True, download=True,
                                                             transform=transforms.ToTensor())
        self.mnist_test = torchvision.datasets.FashionMNIST(root='../Datasets', train=False, download=True,
                                                            transform=transforms.ToTensor())

    # def get_fashion_mnist_labels(self, labels):
    #     text_labels = self.mnist_train.classes
    #     return [text_labels[int(i)] for i in labels]
    # 显示图例
    def show_fashion_mnist(images, labels):
        _, figs = plt.subplots(1, len(images), figsize=(12, 12))
        for f, img, lbl in zip(figs, images, labels):
            f.imshow(img.view((28, 28)).numpy())
            f.set_title(lbl)
            f.axes.get_xaxis().set_visible(False)
            f.axes.get_yaxis().set_visible(False)
        plt.show()

    def load_data_fashion_mnist(self, batch_size=256):
        train_iter = torch.utils.data.DataLoader(self.mnist_train, batch_size=batch_size, shuffle=False)
        test_iter = torch.utils.data.DataLoader(self.mnist_test, batch_size=batch_size, shuffle=False)
        return train_iter, test_iter



