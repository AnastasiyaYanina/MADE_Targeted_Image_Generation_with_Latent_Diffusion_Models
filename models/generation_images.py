import torch
from GPUtil import showUtilization as gpu_usage
from numba import cuda
from huggingface_hub import login
from huggingface_hub import snapshot_download
import torch
import os
from torch import autocast
from diffusers import DPMSolverMultistepScheduler, StableDiffusionImg2ImgPipeline

from contextlib import nullcontext
#import requests
from PIL import Image
#from io import BytesIO
from torch import autocast


#куда сохранять изображение
from google.colab import drive 
drive.mount('/content/gdrive')

# setup device to use
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

Huggingface_Token = ""
login(token = Huggingface_Token )

ADD_LINK = "stabilityai/stable-diffusion-2-1-base"
WHERE_SAVE_SD_MODEL = os.getcwd()
snapshot_download(repo_id=ADD_LINK, cache_dir = os.getcwd())
#путь к моделе
MODEL_NAME = "/content/models--stabilityai--stable-diffusion-2-1-base/snapshots/ae20c88a98ede80edcd1945220235e01292b098e"

scheduler_name="DPMSolverMultistepScheduler"
if scheduler_name == "DPMSolverMultistepScheduler":
    scheduler = DPMSolverMultistepScheduler.from_pretrained(MODEL_NAME, subfolder="scheduler")
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        MODEL_NAME,
        scheduler=scheduler,
        safety_checker=None,
        torch_dtype=torch.float16,
         feature_extractor=None,#раньше работало без него
        revision="fp16",
    ).to("cuda")


#описание изображения из LAVIS
des = 'painting in the style of Banksy on the wall photo a very cute furry teddy bear with a blue nose'
negative_prompt = "" 
num_samples = 1 
guidance_scale =  9
num_inference_steps = 100 # num_inference_steps - (num_inference_steps - num_inference_steps*strength)
strength = 0.7

#путь к изображению
init_image = Image.open('/content/gdrive/MyDrive/Project/images/1.jpg').convert("RGB")
init_image = init_image.resize((512, 512))

#Banksy
prompt = 'painting in the style of Banksy ' + des
with autocast("cuda"), torch.inference_mode():
        images = pipe(
            prompt=prompt, 
            image=init_image, 
            strength=strength,
            negative_prompt=negative_prompt,
            num_images_per_prompt=num_samples,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            generator=None,
        ).images
for img in images:
  #путь куда сохранять изображение
  #img.save('/content/gdrive/MyDrive/Project/sad/1.jpg')
  display(img)


#Robert Delaunay
prompt = 'painting in the style of Robert Delaunay ' + des
with autocast("cuda"), torch.inference_mode():
        images = pipe(
            prompt=prompt, 
            image=init_image, 
            strength=strength,
            negative_prompt=negative_prompt,
            num_images_per_prompt=num_samples,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            generator=None,
        ).images
for img in images:
  #путь куда сохранять изображение
  #img.save('/content/gdrive/MyDrive/Project/sad/1.jpg')
  display(img)


#Vincent Van Gogh
prompt = 'painting in the style of Vincent Van Gogh ' + des
with autocast("cuda"), torch.inference_mode():
        images = pipe(
            prompt=prompt, 
            image=init_image, 
            strength=strength,
            negative_prompt=negative_prompt,
            num_images_per_prompt=num_samples,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            generator=None,
        ).images
for img in images:
  #путь куда сохранять изображение
  #img.save('/content/gdrive/MyDrive/Project/sad/1.jpg')
  display(img)


#Malevich
prompt = 'painting in the style of Malevich ' + des
with autocast("cuda"), torch.inference_mode():
        images = pipe(
            prompt=prompt, 
            image=init_image, 
            strength=strength,
            negative_prompt=negative_prompt,
            num_images_per_prompt=num_samples,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            generator=None,
        ).images
for img in images:
  #путь куда сохранять изображение
  #img.save('/content/gdrive/MyDrive/Project/sad/1.jpg')
  display(img)