import os
import qrcode
import qrcode.image.svg

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
        
        
        img_png = qr.make_image(fill_color="black", back_color="white")
        png_filename = f"{folder_name}.png"
        img_png.save(os.path.join(base_dir, DIRECTORY, png_filename))
        
        
        
        factory = qrcode.image.svg.SvgPathImage
        img_svg = qr.make_image(image_factory=factory)
        
        svg_filename = f"{folder_name}.svg"
        svg_filepath = os.path.join(base_dir, DIRECTORY, svg_filename)
        img_svg.save(svg_filepath)
        
        
        with open(svg_filepath, "r", encoding="utf-8") as file:
            svg_content = file.read()
        
        
        svg_content = svg_content.replace(
            "<svg ", 
            '<svg style="background-color: white;" shape-rendering="crispEdges" ', 
            1
        )
        
        with open(svg_filepath, "w", encoding="utf-8") as file:
            file.write(svg_content)
        
        
        print(f"✅ QR codes générés pour '{folder_name}' -> {png_filename} & {svg_filename}")

print("Opération terminée !")