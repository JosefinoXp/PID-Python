from PIL import Image

# Abrir imagem colorida
img = Image.open('gato.png').convert('RGB')
pixels = list(img.getdata())

# Aplicar a fórmula para cada pixel

# Media Ponderada
grayscale_pixels = [
    int(0.299 * r + 0.587 * g + 0.114 * b)
    for (r, g, b) in pixels
]

# Media simples

# grayscale_pixels = [
#     int( (r + g + b) / 3)
#     for (r, g, b) in pixels
# ]

# Criar nova imagem em escala de cinza
img_gray = Image.new('L', img.size)
img_gray.putdata(grayscale_pixels)
img_gray.save('imagem_cinza.png')
