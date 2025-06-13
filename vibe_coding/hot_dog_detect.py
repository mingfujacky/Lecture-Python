from pathlib import Path
from PIL import Image
import torch
from torchvision import models, transforms
import urllib.request

# Set environment
image_dir = Path.cwd() / 'restricted' / 'assets' / 'hot_dogs'

# Download ImageNet class labels if not present
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
labels_path = "imagenet_classes.txt"
if not Path(labels_path).exists():
    urllib.request.urlretrieve(LABELS_URL, labels_path)
with open(labels_path, "r") as f:
    labels = [line.strip() for line in f.readlines()]

# Load pre-trained model and set to eval mode
model = models.mobilenet_v2(weights='IMAGENET1K_V1')
model.eval()

# Preprocessing pipeline
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def hot_dog_likelihood(img_path):
    """Return the likelihood (probability) that the image is a hot dog."""
    img = Image.open(img_path).convert('RGB')
    x = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        preds = model(x)
        probs = preds.softmax(1)[0]
        top5 = probs.topk(5)
        for idx, prob in zip(top5.indices, top5.values):
            label = labels[idx]
            if 'hotdog' in label.lower() or 'hot dog' in label.lower():
                return float(prob)
    return 0.0

def classify_image(img_path):
    """Return the top-1 label and its probability for the image."""
    img = Image.open(img_path).convert('RGB')
    x = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        preds = model(x)
        probs = preds.softmax(1)[0]
        top1_prob, top1_idx = torch.max(probs, 0)
        label = labels[top1_idx]
        return label, float(top1_prob)
    
def classify_hot_dog():
    # Scan directory for images in alphabetical order and show likelihood
    for img_file in sorted(image_dir.glob('*')):
        if img_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            likelihood = hot_dog_likelihood(img_file)
            print(f"{img_file.name}: Hot dog likelihood = {likelihood:.4f}")

def classify_all_images():
    """Classify all images in the directory and print top-1 label and probability."""
    for img_file in sorted(image_dir.glob('*')):
        if img_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            label, prob = classify_image(img_file)
            print(f"{img_file.name}: {label} (probability: {prob:.4f})")

if __name__ == "__main__":
    classify_hot_dog()
    print("-" * 40)
    classify_all_images()