FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-devel
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install albumentations==0.4.3 opencv-python pudb==2019.2 imageio==2.9.0 imageio-ffmpeg==0.4.2 pytorch-lightning==1.4.2 omegaconf==2.1.1 test-tube>=0.7.5 streamlit>=0.73.1 einops==0.3.0 torch-fidelity==0.3.0 git+https://github.com/openai/CLIP.git protobuf~=3.20.1 torchmetrics==0.6.0 transformers==4.19.2 kornia==0.5.8 && pip uninstall -y torchtext