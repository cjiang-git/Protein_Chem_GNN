#!/bin/bash
conda create -n cs224w python=3.10
conda activate cs224w
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia
pip install numpy pandas scikit-learn matplotlib networkx biopython