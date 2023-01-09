conda env create -f /workspaces/torch-nilm/torch-nilm.yml
conda activate torch-nilm
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 -f https://download.pytorch.org/whl/torch_stable.html