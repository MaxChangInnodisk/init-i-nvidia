from re import TEMPLATE


TEMPLATE = {
    "tag": "cls",
    "tensorrt": {
        "model_path": "./task/classification_sample/resnet50.engine",
        "label_path": "./task/classification_sample/imagenet.txt",
        "device": "NVIDIA GeForce GTX 1050 Ti",
        "input_size": "3,224,224",
        "preprocess": "torch",
        "thres": 0.9
    }
}