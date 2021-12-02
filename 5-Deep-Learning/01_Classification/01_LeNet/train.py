import torch
import torchvision
import torch.nn as nn
from model import LeNet
import torch.optim as optim
import torchvision.transforms as transforms
from data import FashionMNIST
import time


def main():

    def evaluate_accuracy(data_iter, net, device=None):
        if device is None and isinstance(net, torch.nn.Module):
            device = list(net.parameters())[0].device
        acc_sum, n = 0.0, 0
        with torch.no_grad():
            for X, y in data_iter:
                if isinstance(net, torch.nn.Module):
                    net.eval()  # 评估模式下, 关闭dropout, 使用eval()模式
                    acc_sum += (net(X.to(device)).argmax(dim=1) == y.to(device)).float().sum().cpu().item()
                    net.train()  # 改回训练模式
                else:  # 自定义的模型, 3.13节之后不会用到, 不考虑GPU
                    if ('is_training' in net.__code__.co_varnames):  # 如果有is_training这个参数
                        # 将is_training设置成False
                        acc_sum += (net(X, is_training=False).argmax(dim=1) == y).float().sum().item()
                    else:
                        acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
                n += y.shape[0]
        return acc_sum / n

    fashionMNIST = FashionMNIST()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = LeNet()
    net = net.to(device)
    loss_function = nn.CrossEntropyLoss()
    num_epochs, lr, batch_size = 20, 0.001, 256
    optimizer = optim.Adam(net.parameters(), lr)

    # data
    train_iter, test_iter = fashionMNIST.load_data_fashion_mnist(batch_size)

    # train
    print('training on', device)
    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n, batch_count, start = 0.0, 0.0, 0, 0, time.time()
        for X, y in train_iter:
            X = X.to(device)
            y = y.to(device)
            y_pred = net(X)
            loss = loss_function(y_pred, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            train_l_sum += loss.cpu().item()
            train_acc_sum += (y_pred.argmax(dim=1) == y).sum().cpu().item()
            n += y.shape[0]
            batch_count += 1
        test_acc = evaluate_accuracy(test_iter, net)
        print(f'epoch {epoch + 1}, loss {train_l_sum / batch_count}, train acc {train_acc_sum / n}, test acc {test_acc}, time {time.time() - start} sec')

    save_path = './LeNet.pth'
    torch.save(net.state_dict(), save_path)


if __name__ == '__main__':
    main()

