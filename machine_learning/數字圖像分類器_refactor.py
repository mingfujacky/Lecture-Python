import math
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    ConfusionMatrixDisplay,
)

def load_data(test_size=0.25, random_state=0):
    """Load digits dataset and split into train/test with stratification."""
    digits = load_digits()
    X, y = digits.data, digits.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state
    )
    return digits, X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """Train and return a Gaussian Naive Bayes model. 高斯簡單(單純)貝氏分類器"""
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    return gnb

def evaluate_and_plot_confusion_matrix(model, X_test, y_test):
    """Print metrics and plot confusion matrix."""
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}\n")
    print("Classification report:")
    print(classification_report(y_test, y_pred, digits=4))

    disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    disp.ax_.set_title("Confusion Matrix (Test Set)")
    plt.tight_layout()
    #plt.show()

def show_sample_images_with_predictions(digits, model, n=20):
    """Show n sample images with model predictions."""
    # 使用整個資料集的 image 與對應預測
    images = digits.images
    y_hat_all = model.predict(digits.data)

    n = min(n, len(images))
    cols = 5
    rows = math.ceil(n / cols)
    plt.figure(figsize=(cols * 2.2, rows * 2.2))
    for idx in range(n):
        plt.subplot(rows, cols, idx + 1)
        plt.axis("off")
        plt.imshow(images[idx], cmap="gray", interpolation="nearest")
        plt.title(f"Pred: {y_hat_all[idx]}")
    #plt.show()

def main():
    digits, X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    evaluate_and_plot_confusion_matrix(model, X_test, y_test)
    show_sample_images_with_predictions(digits, model, n=10)
    plt.show()

if __name__ == "__main__":
    main()