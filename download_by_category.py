import sys
import os
import urllib.request
from datasets import datasets  # 👈 Import from external file

def download_files(category):
    if category not in datasets:
        print(f"❌ Category '{category}' not found. Available: {', '.join(datasets.keys())}")
        return

    # Create directory
    save_path = os.path.join("temp", "Datasets", category)
    os.makedirs(save_path, exist_ok=True)
    print(f"📁 Files will be saved to: {save_path}")

    for url in datasets[category]:
        filename = os.path.basename(url)
        destination = os.path.join(save_path, filename)
        print(f"⬇️ Downloading {filename} ...")
        urllib.request.urlretrieve(url, destination)
        print(f"✅ Saved: {destination}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_by_category.py <tissue name>")
    else:
        download_files(sys.argv[1].lower())
