
#--------------------------------------------install the data--------------------------------------------------
# from roboflow import Roboflow
# rf = Roboflow(api_key="B8LlIjRf2K80cYYwVhaB")
# project = rf.workspace("konstantinos-gkountakos").project("lados")
# version = project.version(2)
# dataset = version.download("coco-segmentation")


#--------------------------------COCO to YOLO------------------------------------------------------------------

# from ultralytics.data.converter import convert_coco

# convert_coco(
#     labels_dir="LADOS-2",   # folder containing train/, valid/, test/
#     save_dir="LADOS-2-yolo",
#     use_segments=False,   # True if your annotations are polygons and you want seg masks
#     use_keypoints=False,
# )

#----------------------------------------------move the images------------------------------------------------
# import json
# import shutil
# from pathlib import Path

# SOURCE = Path("LADOS-2")       # contains train/, valid/, test/
# DEST = Path("LADOS-2-yolo")
# SPLITS = ["train", "valid", "test"]

# # Build class list/mapping from train.json (assumes same categories across splits)
# with open(SOURCE / "train" / "_annotations.coco.json") as f:
#     train_data = json.load(f)

# categories = sorted(train_data["categories"], key=lambda c: c["id"])
# cat_id_to_idx = {c["id"]: i for i, c in enumerate(categories)}
# names = [c["name"] for c in categories]
# print("Classes:", names)

# for split in SPLITS:
#     json_path = SOURCE / split / "_annotations.coco.json"
#     if not json_path.exists():
#         print(f"Skipping {split}: no json found")
#         continue

#     with open(json_path) as f:
#         data = json.load(f)

#     images = {img["id"]: img for img in data["images"]}
#     (DEST / "images" / split).mkdir(parents=True, exist_ok=True)
#     (DEST / "labels" / split).mkdir(parents=True, exist_ok=True)

#     anns_by_image = {}
#     for ann in data["annotations"]:
#         anns_by_image.setdefault(ann["image_id"], []).append(ann)

#     for img_id, img in images.items():
#         w, h = img["width"], img["height"]
#         filename = img["file_name"]
#         src_img = SOURCE / split / filename
#         dst_img = DEST / "images" / split / filename

#         if not src_img.exists():
#             print(f"WARNING: missing image {src_img}")
#             continue
#         shutil.copy(src_img, dst_img)

#         lines = []
#         for ann in anns_by_image.get(img_id, []):
#             x, y, bw, bh = ann["bbox"]  # COCO: x_min, y_min, width, height
#             xc = (x + bw / 2) / w
#             yc = (y + bh / 2) / h
#             nw = bw / w
#             nh = bh / h
#             cls_idx = cat_id_to_idx[ann["category_id"]]
#             lines.append(f"{cls_idx} {xc:.6f} {yc:.6f} {nw:.6f} {nh:.6f}")

#         label_path = DEST / "labels" / split / (Path(filename).stem + ".txt")
#         with open(label_path, "w") as lf:
#             lf.write("\n".join(lines))


