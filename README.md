# MNIST Digit Classification using PyTorch

A simple and beginner-friendly Deep Learning project built with PyTorch to classify handwritten digits (0-9) using the classic MNIST dataset and an Artificial Neural Network (ANN).

## 🚀 Features
- Loads and preprocesses the MNIST dataset using PyTorch `DataLoader`.
- Implements a fully connected Feedforward Neural Network (ANN) using `nn.Sequential`.
- Trains the model using the Cross-Entropy Loss and Adam Optimizer.
- Evaluates model performance and computes test accuracy.
- Saves the trained model weights (`minst_model.pth`) and tests predictions on single images using Matplotlib.

## 🛠️ Tech Stack
- **Python**
- **PyTorch**
- **Torchvision**
- **Matplotlib**

## 📂 Project Structure
```text
├── mnist_project.ipynb   # Main Jupyter Notebook with code
├── minst_model.pth       # Saved model weights
├── requirements.txt      # Required Python libraries
└── README.md             # Project documentation
