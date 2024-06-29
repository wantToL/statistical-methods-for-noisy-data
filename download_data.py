import os
import requests

def download_file(url, dest_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f'Download completed: {dest_path}')

# URL des fichiers de données
urls = [
    ('https://example.com/path/to/x_test_c7ETL4q.csv', 'data/x_test_c7ETL4q.csv'),
    ('https://example.com/path/to/x_train_Lafd4AH.csv', 'data/x_train_Lafd4AH.csv')
]

# Créer le répertoire data s'il n'existe pas
os.makedirs('data et benchmark', exist_ok=True)

# Télécharger chaque fichier
for url, dest_path in urls:
    download_file(url, dest_path)
