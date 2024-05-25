import os
from PIL import Image
import numpy as np

def normalize_image(image_path):
    # Carregar a imagem
    image = Image.open(image_path).convert('RGB')
    
    # Converter a imagem para um array numpy
    image_array = np.array(image).astype(np.float32)
    
    # Normalizar os valores dos pixels para a faixa [0, 1]
    normalized_array = image_array / 255.0
    
    return normalized_array

def normalize_images_in_folder(input_folder, output_folder):
    # Criar a pasta de saída se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterar sobre todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        # Construir o caminho completo para o arquivo
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Verificar se é um arquivo de imagem
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Normalizar a imagem
            normalized_array = normalize_image(input_path)
            
            # Converter o array normalizado de volta para a faixa [0, 255] e uint8 para salvar
            normalized_image = (normalized_array * 255).astype(np.uint8)
            normalized_pil_image = Image.fromarray(normalized_image)
            
            # Salvar a imagem normalizada na pasta de saída
            normalized_pil_image.save(output_path)
            print(f'Imagem {filename} normalizada e salva em {output_path}')

# Exemplo de uso
input_folder = 'C:/Users/jorge/OneDrive/Documentos/GitHub/Pesquisa-ufpi/Imagens_marcar'
output_folder = 'C:/Users/jorge/OneDrive/Documentos/GitHub/Pesquisa-ufpi/normalizadas'
normalize_images_in_folder(input_folder, output_folder)

print("Todas as imagens foram normalizadas com sucesso!")
