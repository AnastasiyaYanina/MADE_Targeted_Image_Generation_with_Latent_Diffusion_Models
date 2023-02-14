import torch
from PIL import Image

from lavis.models import load_model_and_preprocess

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#откуда брать изображение
from google.colab import drive 
drive.mount('/content/gdrive')

#куда сохранить описание изображения
file_save = open('/content/gdrive/MyDrive/Project/images/descriptions_1.txt','w')
file_save.write('Descriptions' +'\n')

model, vis_processors, _ = load_model_and_preprocess(
    name="blip_caption", model_type="large_coco", is_eval=True, device=device
)

init_image = Image.open('/content/gdrive/MyDrive/Project/images/1.jpg').convert("RGB")
init_image = init_image.resize((512, 512))

image = vis_processors["eval"](init_image).unsqueeze(0).to(device)
des = model.generate({"image": image}, use_nucleus_sampling=True, num_captions=1)
#сохраниение описания изображения
#example des[0] = an orange squirrel in leaves with a nut
file_save.write(des[0] +'\n')