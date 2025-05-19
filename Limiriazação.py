from PIL import Image

# Abrir imagem colorida
img = Image.open('imagem_cinza_mediaSimples.png').convert('RGB')
pixels = list(img.getdata())

# Aplicar a fórmula para cada pixel

# Limiriazação
grayscale_pixels = [
    int( 0 if (r + g + b) < 150 else 255)
    for (r, g, b) in pixels
]

# Criar nova imagem em escala de cinza
img_gray = Image.new('L', img.size)
img_gray.putdata(grayscale_pixels)
img_gray.save('imagem_limiriazacao.png')
