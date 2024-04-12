import os
import json
import requests
from tqdm import tqdm
from colorama import Fore, Style

def download_media_from_json(json_data):
    # Download media files
    for data_set in json_data:
        for key, value in data_set.items():
            image_url = value.get("Image")
            video_url = value.get("Video")

            # Download image
            image_filename = os.path.join("media", key + ".png")
            download_file(image_url, image_filename, key + ".png")

            # Download video
            video_filename = os.path.join("media", key + ".mp4")
            download_file(video_url, video_filename, key + ".mp4")

def fetch_data_from_json(json_data):
    try:
        fetched_data = ""
        for data_set in json_data:
            fetched_data += "-----------\n"
            for key, value in data_set.items():
                fetched_data += f"{key}:\n"
                fetched_data += f"Image: {value.get('Image')}\n"
                fetched_data += f"Video: {value.get('Video')}\n"
            fetched_data += "\n"  # Add space between sets of data
        return fetched_data
    except Exception as e:
        return f"An error occurred: {e}"

def save_text_to_file(text, filename):
    with open(filename, "w") as file:
        file.write(text)

def download_file(url, filename, file_display_name):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    with open(filename, 'wb') as f, tqdm(
            desc=file_display_name,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
    ) as progress_bar:
        for data in response.iter_content(block_size):
            f.write(data)
            progress_bar.update(len(data))

if __name__ == "__main__":
    # Logo
   logo = """
 
 ▄▄▄██▀▀▀  ██████  ▒█████   ███▄    █  ██▓     ▒█████   ▄▄▄      ▓█████▄ ▓█████  ██▀███  
   ▒██   ▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
   ░██   ░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒███   ▓██ ░▄█ ▒
▓██▄██▓    ▒   ██▒▒██   ██░▓██▒  ▐▌██▒▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
 ▓███▒   ▒██████▒▒░ ████▓▒░▒██░   ▓██░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░▒████▒░██▓ ▒██▒
 ▒▓▒▒░   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░   ░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
 ░ ░ ░   ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░   ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░    ░     ░░   ░ 
 ░   ░         ░      ░ ░           ░     ░  ░    ░ ░        ░  ░   ░       ░  ░   ░     
                                                                  ░                                                                                 
                           
                         """ + "\033[1;31mMade By TG: @ANONYMOUS_AMIT\033[0m" + """                                   
"""

    # Print logo
    print(Fore.GREEN + logo)

    # Options
    print(Fore.BLUE + "[1] Download Media from Json file")
    print(Fore.YELLOW + "[2] Fetch Data from Json")

    choice = input(Style.RESET_ALL + "Enter your choice: ")

    if choice == "1":
        print(Fore.CYAN + "[1] Input file path")
        print(Fore.MAGENTA + "[2] Send Json content here")
        fetch_choice = input(Style.RESET_ALL + "Choose how to provide JSON data: ")

        if fetch_choice == "1":
            file_path = input("Enter the path of the JSON file: ")
            with open(file_path, "r") as file:
                json_data = json.load(file)
            download_media_from_json(json_data)
        elif fetch_choice == "2":
            print("Paste your JSON content below (press Ctrl+D when finished):")
            json_content = ""
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                json_content += line + "\n"
            try:
                json_data = json.loads(json_content)
                download_media_from_json([json_data])
            except json.JSONDecodeError as e:
                print(f"Invalid JSON content: {e}")
        else:
            print("Invalid choice.")

    elif choice == "2":
        print(Fore.CYAN + "[1] Input file path")
        print(Fore.MAGENTA + "[2] Send Json content here")
        fetch_choice = input(Style.RESET_ALL + "Choose how to provide JSON data: ")

        if fetch_choice == "1":
            file_path = input("Enter the path of the JSON file: ")
            with open(file_path, "r") as file:
                json_data = json.load(file)
            fetched_data = fetch_data_from_json(json_data)
            print(fetched_data)
            save_text_to_file(fetched_data, "fetched_data.txt")
            print("Fetched data saved to fetched_data.txt")
        elif fetch_choice == "2":
            print("Paste your JSON content below (press Ctrl+D when finished):")
            json_content = ""
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                json_content += line + "\n"
            try:
                json_data = json.loads(json_content)
                fetched_data = fetch_data_from_json([json_data])
                print(fetched_data)
                save_text_to_file(fetched_data, "fetched_data.txt")
                print("Fetched data saved to fetched_data.txt")
            except json.JSONDecodeError as e:
                print(f"Invalid JSON content: {e}")
        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")
#4 Implemented saving fetched data to a text file.
# Added options for providing JSON content directly in the terminal.
# Added space between each set of data in fetched_data and printed fetched_data.
