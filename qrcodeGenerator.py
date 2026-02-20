import os
import qrcode
from PIL import Image

DIRECTORY = "qrcode"

EXCEPT_DIRECOTIES = ["qrcode", "venv", "__pycache__", "nomCanyon", "assets"]

if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)

base_dir = os.path.dirname(os.path.abspath(__file__))

for item in os.listdir(base_dir):
    item_path = os.path.join(base_dir, item)
    
    if os.path.isdir(item_path):
        folder_name = item
        
        if folder_name.startswith('.') or folder_name in EXCEPT_DIRECOTIES:
            continue
            
        url = f"https://40ansefc.github.io/traceGPX/{folder_name}"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        img_pil = img.get_image()
        
        img_pil = img_pil.convert("RGB")
        
        img_resized = img_pil.resize((1500, 1500), Image.Resampling.NEAREST)
        
        jpg_filename = f"{folder_name}.jpg"
        jpg_filepath = os.path.join(base_dir, DIRECTORY, jpg_filename)
        img_resized.save(jpg_filepath, format="JPEG", quality=100)
        
        print(f"✅ QR code généré pour '{folder_name}' -> {jpg_filename} (1500x1500px)")

url = f"https://40ansefc.github.io/traceGPX"
        
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img_pil = img.get_image()

img_pil = img_pil.convert("RGB")

img_resized = img_pil.resize((1500, 1500), Image.Resampling.NEAREST)

jpg_filename = f"general.jpg"
jpg_filepath = os.path.join(base_dir, DIRECTORY, jpg_filename)
img_resized.save(jpg_filepath, format="JPEG", quality=100)

print(f"✅ QR code généré pour 'general' -> {jpg_filename} (1500x1500px)")

print("Opération terminée !")