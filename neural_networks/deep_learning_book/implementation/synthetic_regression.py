from torch import randn, matmul, reshape
from module import DataModule


class SyntheticRegressionData(DataModule):

    def __init__(self, w, b, noise=0.01, num_train=1000,
                 num_val=1000, batch_size=32):
        super().__init__()
        self.save_hyperparameters()
        n = num_train + num_val
        self.X = randn(n, len(w))
        noise = randn(n, 1) * noise
        self.y = matmul(self.X, reshape(w, (-1, 1))) + b + noise

    def get_dataloader(self, train):
        i = slice(0, self.num_train) if train else slice(self.num_train, None)
        return self.get_tensorloader((self.X, self.y), train, i)
