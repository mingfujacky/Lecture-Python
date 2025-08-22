from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

digits = load_digits()
X = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)               # predictions on unseen data
print(confusion_matrix(y_test, y_pred))

image_and_predictions = list(zip(digits.images, gnb.predict(X)))
for index, (image, prediction) in enumerate(image_and_predictions[:20]):
    plt.subplot(5, 5, index + 1)
    plt.axis('off')
    # plt.gray()
#     plt.imshow(image, interpolation='nearest', cmap='gray')
    plt.imshow(image, cmap='gray') 

    plt.title(f'Prediction: {prediction}')
plt.tight_layout(pad=2.0, w_pad=1.0, h_pad=1.0)
plt.show()    