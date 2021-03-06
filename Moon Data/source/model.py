import torch
import torch.nn as nn
import torch.nn.functional as F

## TODO: Complete this classifier
class SimpleNet(nn.Module):
    
    ## TODO: Define the init function
    def __init__(self, input_dim, hidden_dim, output_dim):
        '''Defines layers of a neural network.
           :param input_dim: Number of input features
           :param hidden_dim: Size of hidden layer(s)
           :param output_dim: Number of outputs
         '''
        super(SimpleNet, self).__init__()
        
        # define all layers, here
        # fully connected layers
        self.fc_in = nn.Linear(input_dim, hidden_dim)
        self.fc_hidden = nn.Linear(hidden_dim, hidden_dim)
        self.fc_out = nn.Linear(hidden_dim, output_dim)
        # dropout layer
        self.drop = nn.Dropout(0.5)
        # Sigmoid layer for classification
        self.sig = nn.Sigmoid()
    
    ## TODO: Define the feedforward behavior of the network
    def forward(self, x):
        '''Feedforward behavior of the net.
           :param x: A batch of input features
           :return: A single, sigmoid activated value
         '''
        # your code, here
        # 10 hidden layers with a dropout layer between each
        x = F.relu(self.fc_in(x))
        x = self.drop(x)
        for i in range(9):
            x = F.relu(self.fc_hidden(x))
            x = self.drop(x)
        # last hidden layer with sigmoid activation for output
        x = self.fc_out(x)
        x = self.sig(x)
        
        return x