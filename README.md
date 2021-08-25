# YoloV5_for_CPU

YoLo v5: CPUセットアップ

## Requirements

OS: Ubuntu 20.04 LTS
CPU: Ryzen 3700X
(GPU): RTX 3080
Python: 3.8 or higher

⚠ GPU搭載のPCで実行する場合は、torch, torchvisionのバージョンをCPUに設定しておかないと、
GPUを使おうとするので [PyTorch-START LOCALLY](https://pytorch.org/get-started/locally/)を参考にインストールされたい。

## Setup Virtualenv 

上記環境の場合。GPU versionはCudaの設定からまた別ドキュメントで作成予定。

### 1. Create virtualenv
`python3 -m venv venv`
### 2. Activate venv
`source venv/bin/activate`
### 3. Install python library
`pip install torch==1.9.0+cpu torchvision==0.10.0+cpu torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html`  
`pip install -r requrements.txt`

### 4. Check run detect.py

`python detect.py`






