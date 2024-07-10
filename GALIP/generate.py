import torch
import os
from PIL import Image
import clip
import os.path as osp
import os, sys
import torchvision.utils as vutils
import time
sys.path.insert(0, './code')

from lib.utils import load_model_weights,mkdir_p
from models.GALIP import NetG, CLIP_TXT_ENCODER
start_time = time.time()
device = 'cuda' # 'cpu' # 'cuda:0'
CLIP_text = "ViT-B/32"
clip_model, preprocess = clip.load("ViT-B/32", device=device)
clip_model = clip_model.eval()

text_encoder = CLIP_TXT_ENCODER(clip_model).to(device)
netG = NetG(64, 100, 512, 256, 3, False, clip_model).to(device)
path = 'code/saved_models/pretrained/pre_coco.pth'
checkpoint = torch.load(path, map_location=torch.device('cuda'))
netG = load_model_weights(netG, checkpoint['model']['netG'], multi_gpus=False)

batch_size = 1
noise = torch.randn((batch_size, 100)).to(device)

captions = [sys.argv[1]]
print(captions)
mkdir_p('./samplesoriginal')

# generate from text
with torch.no_grad():
    for i in range(len(captions)):
        caption = captions[i]
        tokenized_text = clip.tokenize([caption]).to(device)
        sent_emb, word_emb = text_encoder(tokenized_text)
        sent_emb = sent_emb.repeat(batch_size,1)
        fake_imgs = netG(noise,sent_emb,eval=True).float()
        name = f'{captions[i].replace(" ", "-")}'
        vutils.save_image(fake_imgs.data, './samplesoriginal/%s.png'%(name), nrow=8, value_range=(-1, 1), normalize=True)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")