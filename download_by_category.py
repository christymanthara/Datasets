import sys
import os
import urllib.request
from Datasets.datasets import datasets  # Importing the dataset dictionary

def download_files(category):
    if category not in datasets:
        print(f"❌ Category '{category}' not found. Available: {', '.join(datasets.keys())}")
        return

    # Create directory for downloads
    save_path = os.path.join("temp", "Datasets", category)
    os.makedirs(save_path, exist_ok=True)
    print(f"📁 Files will be saved to: {save_path}\n")

    for url in datasets[category]:
        filename = os.path.basename(url)
        destination = os.path.join(save_path, filename)

        if os.path.exists(destination):
            print(f"✅ File already exists: {destination}")
        else:
            print(f"⬇️ Downloading {filename} ...")
            try:
                urllib.request.urlretrieve(url, destination)
                print(f"✅ Downloaded and saved: {destination}")
            except Exception as e:
                print(f"❌ Failed to download {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_by_category.py <category>")
    else:
        download_files(sys.argv[1].lower())
