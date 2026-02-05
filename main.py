import os
import shutil

def organize_files_by_extension(folder_path):
    # Verifica se a pasta existe
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não existe.")
        return

    # Itera sobre os arquivos na pasta
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Ignora subpastas e processa apenas arquivos
        if os.path.isfile(file_path):
            # Obtém a extensão do arquivo
            file_extension = os.path.splitext(file_name)[1].lower()

            # Cria uma subpasta para a extensão, se necessário
            if file_extension:
                extension_folder = os.path.join(folder_path, file_extension[1:])
                os.makedirs(extension_folder, exist_ok=True)

                # Gera um novo nome se o arquivo já existir na subpasta
                new_file_path = os.path.join(extension_folder, file_name)
                counter = 1
                while os.path.exists(new_file_path):
                    base_name, ext = os.path.splitext(file_name)
                    new_file_name = f"{base_name}_{counter}{ext}"
                    new_file_path = os.path.join(extension_folder, new_file_name)
                    counter += 1

                # Move o arquivo para a subpasta correspondente
                shutil.move(file_path, new_file_path)

    print("Arquivos organizados e renomeados com sucesso!")

if __name__ == "__main__":
    # Caminho da pasta a ser organizada
    folder_to_organize = input("Digite o caminho da pasta que deseja organizar: ")
    organize_files_by_extension(folder_to_organize)