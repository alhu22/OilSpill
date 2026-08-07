import random
import os
import time
from pathlib import Path

from ultralytics import YOLO


random.seed(time.time_ns())

# --- Config ---
TEST_IMAGES_DIR = Path("LADOS-2-yolo/images/test")
MODEL_PATH = "runs/detect/train/weights/best.pt"  # path to your trained weights
OUTPUT_DIR = Path("predictions")
CONF_THRESHOLD = 0.25
NUM_IMAGES = 3  # how many random images to run per script call

# --- Pick random images ---
image_files = list(TEST_IMAGES_DIR.glob("*.jpg")) + list(TEST_IMAGES_DIR.glob("*.png"))
if not image_files:
    raise FileNotFoundError(f"No images found in {TEST_IMAGES_DIR}")

num_to_pick = min(NUM_IMAGES, len(image_files))
random_images = random.sample(image_files, num_to_pick)
print(f"Selected {num_to_pick} image(s): {[img.name for img in random_images]}")

# --- Load model ---
model = YOLO(MODEL_PATH)
OUTPUT_DIR.mkdir(exist_ok=True)

# --- Run inference on each selected image ---
for img_path in random_images:
    results = model.predict(
        source=str(img_path),
        conf=CONF_THRESHOLD,
        device=0,  # set to "cpu" if you don't want to use the GPU
    )

    result = results[0]
    save_path = OUTPUT_DIR / f"annotated_{img_path.name}"
    result.save(filename=str(save_path))

    print(f"\n{img_path.name} -> {save_path}")
    if len(result.boxes) == 0:
        print("  No objects detected above the confidence threshold.")
    else:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            conf = float(box.conf[0])
            print(f"  {cls_name}: {conf:.2f}")