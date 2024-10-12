import torch
import torch.utils
import torch.utils.data
from utils import nn_Module
from hyperparameters import HyperParameters
from progressboard import ProgressBoard


class Module(nn_Module, HyperParameters):
    def __init__(self, plot_train_per_epoch=2, plot_valid_per_epoch=1):
        super().__init__()
        self.save_hyperparameters()
        self.board = ProgressBoard()

    def loss(self, y_hat, y):
        raise NotImplementedError

    def foward(self, X):
        assert hasattr(self, 'net'), 'Neural Network is not initialized'
        return self.net(X)

    def plot(self, key, value, train):
        assert hasattr(self, 'trainer'), 'Trainer is not initialized'
        self.board.xlabel = 'epoch'
        x, n = 0, 0
        if train:
            x = self.trainer.train_batch_idx / self.trainer.num_train_batches
            n = self.trainer.num_train_batches / self.plot_train_per_epoch
        else:
            x = self.trainer.epoch + 1
            n = self.trainer.num_val_batches / self.plot_valid_per_epoch
        print(f'{'train_' if train else 'val_' + key}: ', end='')
        print(f'X: {x}\n N: {n}')
        print()

    def training_step(self, batch):
        loss = self.loss(self(*batch[:-1]), batch[-1])
        self.plot('loss', loss, train=False)
        return loss

    def validation_step(self, batch):
        loss = self.loss(self(*batch[:-1]), batch[-1])
        self.plot('loss', loss, train=False)

    def configure_optimizers(self):
        return torch.optim.SGD(self.parameters(), lr=self.lr)

    def apply_init(self, inputs, init=None):
        self.foward(*inputs)
        if init is not None:
            self.net.apply(init)


class DataModule(HyperParameters):

    def __init__(self, root='../data', num_workers=4):
        self.num_workers = num_workers
        self.save_hyperparameters()

    def get_dataloader(self, train):
        raise NotImplementedError

    def train_dataloader(self):
        return self.get_dataloader(train=True)

    def val_dataloader(self):
        return self.get_dataloader(train=False)

    def get_tensorloader(self, tensors, train, indices=slice(0, None)):
        tensors = tuple(a[indices] for a in tensors)
        dataset = torch.utils.data.TensorDataset(*tensors)
        return torch.utils.data.DataLoader(dataset, self.batch_size,
                                           shuffle=train,
                                           num_workers=self.num_workers)
