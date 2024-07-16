import requests
from termcolor import colored
import json
import os

ascii_art = """
⠐⡠⠀⢄⠠⠀⡄⠠⢀⠄⠠⡀⠄⢠⠀⠄⡠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⢠⠀⠄⡠⠀⢄⠠⠀⡄⠠⢀⠄⠠⡀⠄⢠⠀⠄⠂
⠂⠄⡁⠂⠄⠡⢀⠁⠂⠌⡐⠠⠈⠄⡈⠐⠠⠁⠌⠠⠁⢌⣠⣁⣌⣤⣡⣌⣤⣥⣬⣤⣥⣬⣤⣥⣬⣄⣡⣌⣤⣁⣌⡠⠉⡐⠠⢈⠐⠠⢁⠂⠄⠡⢀⠁⠂⠌⡐⠠⠈⠄⡈⠄⡁
⡁⠂⠄⠡⢈⠐⠠⢈⠐⠄⠠⠁⠌⡐⠠⢁⣂⣥⠾⠒⠛⡉⠡⠀⠄⡀⠄⡀⠠⢀⠠⠀⠄⠠⠀⠄⡀⠠⢀⠠⠀⠄⡈⢉⠛⠒⠶⣤⣈⠐⠠⠈⠄⡁⠂⠌⡐⠠⢀⠡⢈⠐⡀⠂⠄
⠄⠡⢈⠐⠠⢈⠐⠠⠈⠄⠡⠘⠠⠐⣠⠞⡁⠠⠐⡈⠐⠠⠁⠌⡐⢀⠂⠄⡁⠂⠄⠡⠈⠄⡁⠂⠄⡁⠂⠄⡁⢂⠐⠄⣈⠐⠠⠀⠌⠳⣆⢁⠂⠄⡁⠂⠄⡁⢂⠐⡀⠂⠄⡁⠂
⠌⡐⠠⢈⠐⠠⠈⠄⠡⠈⢄⠁⢂⢱⠇⡐⠠⢁⠂⠄⡁⢂⠁⢂⠐⠠⢈⠐⠠⠁⠌⠠⢁⠂⠄⡁⠂⠄⡁⢂⠐⠠⢈⠐⠠⢈⠡⠈⠄⠡⠸⡆⡈⠐⠠⢁⠂⡐⢀⠂⠄⡁⠂⠄⡁
⠂⠄⡁⠂⠌⠠⠁⠌⠠⢁⠂⠌⡀⡟⠠⢀⠡⠀⠌⣐⣀⣂⡌⡠⢈⠐⠠⠈⠄⠡⢈⠐⠠⢈⠐⠠⢁⠂⡐⠠⢈⡐⣠⣈⣐⣀⠂⠡⠈⠄⡁⢿⠀⡁⠂⠄⢂⠐⠠⢈⠐⠠⢁⠂⠄
⡁⠂⠄⠡⠈⠄⠡⢈⠐⠠⠌⡐⢠⡇⢁⠂⢤⡷⣿⣭⣿⣿⣿⣿⣿⣶⢥⣌⠠⢁⠂⠌⡐⠠⢈⠐⡀⣢⡴⣷⣿⣿⣿⣿⣿⣭⣿⢦⡅⢂⠐⢸⠂⠄⠡⠈⠄⣈⠐⠠⢈⠐⠠⠈⠄
⠄⠡⠈⠄⠡⢈⠐⠠⢈⠐⠄⡐⢠⡇⠠⢨⣯⠿⠋⢉⠉⡉⠙⠻⠿⣿⣿⣿⣭⠂⠌⡐⠠⢁⠂⡐⣭⣷⣿⣿⠿⠟⠋⢉⠉⡉⠙⠿⣽⡆⢈⢸⡃⠌⠠⢁⠂⠄⡈⢐⠠⠈⠄⡁⠂
⠌⠠⠁⠌⡐⠠⢈⠐⠠⢈⠐⠠⢸⠇⡀⡏⠁⠄⡈⠄⠂⠄⡁⢂⠐⡈⠙⠻⠟⠃⡐⠠⢁⠂⡐⠈⠿⠟⠋⡁⠐⠠⢁⠂⡐⠠⢁⠂⠌⢹⠀⢸⡇⠠⢁⠂⠌⡐⢀⠂⠄⡁⠂⠄⡁
⠌⠠⢁⠂⠄⡁⠂⠌⡐⠠⢈⠐⣸⡁⢣⠁⠌⡐⠠⢈⣰⣤⣴⣤⣦⣄⡁⠂⠌⠠⢹⡆⢀⢢⡟⠀⢂⠐⢠⣠⣥⣦⣤⣦⣀⠁⠂⠌⡐⠈⣜⠠⡇⠂⠄⡈⠐⡀⠂⠌⡐⠠⢁⠂⠄
⠌⡐⠠⢈⠐⠠⢁⠂⠄⡁⢂⠐⣾⠀⡘⣧⡂⠠⣱⡟⣫⣭⣶⣾⣯⣽⣛⢷⡌⠐⣀⡇⠂⢼⡀⠌⢠⡾⢟⣯⣽⣶⣾⣭⣝⣻⣦⠂⢠⣽⠁⠄⣿⢀⠂⠌⡐⠠⢁⠂⠄⡁⠂⠌⡀
⠂⠄⡁⠂⠌⡐⠠⢈⠐⡀⠂⢄⡏⡐⢀⣬⣷⣿⣿⣜⣛⠿⠿⠿⠿⣛⣻⡼⠋⠠⢸⡇⢈⢸⡇⠠⠙⣷⣟⣻⠿⠿⠿⢿⣛⣣⣿⣿⣾⣅⡀⢂⢹⡠⢈⠐⠠⢁⠂⠌⡐⠠⢁⠂⠄
⡁⠂⠄⡁⠂⠄⡁⠂⠄⠡⢈⠸⣇⣰⣿⠞⠉⡀⠄⡉⠛⠛⠛⠛⠛⢋⠡⢀⠁⢂⢸⡇⠠⢸⡇⠠⢁⠠⢈⠙⠛⠛⠛⠛⠛⠉⡀⠄⡉⠺⣽⣆⣼⡃⠠⢈⠐⠠⢈⠐⠠⢁⠂⠌⡀
⠄⡁⠂⠄⡁⠂⠄⠡⢈⠡⢀⠸⣿⠴⠁⡀⢂⠐⠠⠄⠡⠈⠄⠡⠈⠄⠂⠄⡈⠄⣾⠁⡐⠈⣷⠐⡀⠂⠤⠈⠄⠡⠈⠄⡁⢂⠐⢠⠀⠡⠈⠧⣿⠆⢁⠂⠌⡐⠠⢈⠐⠠⢈⠐⡀
⠂⠄⡁⠂⠄⠡⢈⠐⡀⠆⠠⢘⣿⡆⡐⡀⠂⠌⡐⠈⠄⠡⠈⠄⠡⢈⣰⠀⡐⢸⡏⠐⠠⢁⢹⡇⠠⢁⣂⠡⠈⠄⡁⢂⠐⠠⠈⠄⡈⠄⢡⢸⣿⠂⠄⡈⠐⠠⢁⠂⠌⡐⢀⠂⠄
⡁⠂⠄⠡⢈⠐⡀⢂⠐⡈⠐⡀⢿⢷⡹⣦⣁⠂⠄⠡⠈⠄⢡⣨⣴⣾⡇⠐⠠⢸⠂⡁⠂⠄⣈⡇⠐⠠⢹⣷⣮⣔⠀⠂⠌⠠⢁⠂⣐⣼⢏⡾⡿⢀⠂⠄⡑⢀⠂⠌⡐⢀⠂⠌⡀
⠄⠡⢈⠐⡀⢂⠐⡀⠂⠌⡐⢀⠺⡏⣧⣨⣿⡷⣾⣤⣷⠾⠛⠋⡁⠘⢧⣈⣴⣬⣣⠠⢁⠂⡜⣥⣼⣀⡼⠃⡈⠙⠻⠷⣾⣴⣶⢾⣿⣅⣼⢱⡇⠠⢈⠐⡀⠂⠌⡐⢀⠂⠌⡐⠀
⠌⡐⢀⠂⡐⢀⠂⠄⡁⠂⠔⠠⠈⣧⠘⣧⣻⣷⡜⣿⣿⣧⡠⠁⠄⡁⠂⠌⣹⣿⣿⣿⣿⣿⣿⣿⣏⠁⠄⠂⠄⡁⢂⣼⣿⣿⢣⣾⡿⣼⠃⣼⠀⡁⢂⠐⠠⢁⠂⡐⠠⢈⠐⠠⠁
⢂⠐⡀⢂⠐⠠⢈⠐⠠⠁⠌⠠⢁⢹⡄⠘⣧⣳⡿⣌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡿⣡⢿⢟⡼⠁⢤⡏⠐⡀⠂⠌⡐⢀⠂⠄⡁⠂⠌⠠⠁
⢂⠐⡀⠂⠌⡐⠠⠈⠄⠡⢈⡐⠠⢈⣧⠐⠈⢷⡻⣝⢦⣙⠛⠛⠛⠛⠛⠛⠛⠿⠿⣤⢥⡬⠽⠟⠛⠛⠛⠛⠛⠛⠛⢋⡴⣫⢟⡾⠁⠌⣸⠁⠂⠄⡁⢂⠐⠠⢈⠐⠠⠁⠌⠠⠁
⢂⠐⠠⢁⠂⠄⠡⠈⠄⡁⠂⠄⡁⢂⠸⣆⠁⢂⠻⣝⢦⡙⠲⣬⣀⠡⠈⠄⡁⠂⠄⠠⢀⠀⠂⠌⠠⠁⠌⢠⣁⣬⠞⢋⡴⣫⠟⠀⠌⣰⠋⠄⡁⢂⠐⠠⢈⠐⠠⠈⠄⠡⠈⠄⡁
⠂⠌⡐⠠⠈⠄⠡⢈⠐⠠⢁⠂⠰⢀⠂⠙⣎⡠⢀⠛⣮⢳⡄⠠⢉⠙⠛⠛⠓⢻⣶⣷⣶⣾⣾⡞⠛⠛⠛⠋⢉⠀⣐⠞⣵⠋⠠⢁⣼⠋⢀⠂⡐⠠⢈⠐⠠⠈⠄⠡⠈⠄⡁⠂⠄
⡁⠂⠄⠡⠈⠄⡁⠂⠌⡐⠠⢈⠐⠠⢈⠐⡈⠳⣄⠂⡈⢷⡙⢦⠀⠌⠠⢁⠂⠄⣿⣿⣿⣿⣿⠀⡐⠠⠁⠌⡀⡲⢋⡾⠁⠠⣡⠞⢁⠀⢂⠐⠠⢁⠂⠌⠠⠁⠌⠠⢁⠂⠄⡁⠂
⠄⠡⠈⠄⡁⠂⠄⡁⠂⠄⡁⠂⠌⡐⠀⠆⠠⢁⠘⠷⣄⠀⠻⣦⠋⠠⢁⠂⠌⡐⣿⣿⣿⣿⣿⠃⠠⠁⠌⡐⠘⣵⠋⠄⣈⡶⠉⡐⠠⠈⠄⣈⠐⠠⠈⠄⠡⠈⠄⡁⠂⠌⡐⠠⠁
⠌⠠⢁⠂⠄⡁⠂⠄⡁⠂⠄⡁⠂⠄⠡⢈⠐⠄⠂⠄⡉⠷⣄⡈⢷⡅⠂⠌⡐⢀⢹⣿⣿⣿⡏⠠⠁⠌⡐⢠⡟⢁⣰⠞⢉⠀⡐⠠⠁⠌⡐⠠⠈⠄⠡⠈⠄⡁⠂⠄⡁⠂⠄⡁⠂
⠌⡐⠠⢈⠐⠠⢁⠂⠄⡁⠂⠄⠡⢈⠐⠠⠈⠄⡑⠠⠐⠠⢈⠻⢤⡙⢧⡐⢀⠂⠄⣿⣿⣿⠀⢂⠁⢂⡴⢋⡴⠞⠁⡐⢀⠂⠄⠡⢈⠐⠠⠁⠌⠠⠁⠌⡐⠠⢁⠂⠄⡁⠂⠄⡁
⠂⠄⡁⠂⠌⡐⠠⢈⠐⠠⠁⠌⡐⠠⠈⠄⡁⠂⠄⠡⢈⠐⡠⠐⠠⠙⠲⢽⡦⢬⣀⢿⣿⡿⣀⡦⢼⡯⠖⠋⡀⢂⠡⠐⠠⠈⠄⡁⠂⠌⠠⠁⠌⠠⢁⠂⠄⡁⠂⠌⡐⠠⢁⠂⠄
⡁⠂⠄⡁⠂⠄⡁⠂⠌⠠⢁⠂⠄⠡⢈⠐⠠⠁⠌⡐⢀⠂⠄⡁⢂⠡⠈⠄⡉⢉⠩⢉⠛⡉⠉⠍⡉⠠⢀⠡⠐⡀⢂⠁⢂⠁⠂⠄⠡⠈⠄⠡⢈⠐⠠⢈⠐⠠⢁⠂⠄⡁⠂⠌⡀
⢄⡁⠂⠄⡁⠂⠄⠡⢈⠐⠠⠈⠄⡁⠂⠌⠠⢁⠂⡐⠠⢈⠐⡀⠂⠄⡁⢂⠰⢀⠂⠄⠂⠄⡁⠂⠄⡁⠂⠄⠡⠐⠠⠈⠄⡈⠌⠠⠁⠌⠠⢁⠂⠌⡐⠠⢈⠐⠠⢈⠐⠠⢁⠂⠄
  ____ _____  _ __   ______  ____   _____  _____ _____ ____  
 / ___|_   _|/ \\ \ / |  _ \|  _ \ / _ \ \/ |_ _| ____|  _ \ 
 \___ \ | | / _ \\ V /| |_) | |_) | | | \  / | ||  _| | | | |
  ___) || |/ ___ \| | |  __/|  _ <| |_| /  \ | || |___| |_| |
 |____/ |_/_/   \_|_| |_|   |_| \_\\___/_/\_|___|_____|____/ 
                                                             
PROXY CHECKER & AUTO-UPDATER FOR PROXYCHAINS v1.0.0
by @hashtagtodo | https://github.com/hashtagtodo/stay-proxied
"""

print(colored(ascii_art, "yellow"))


def check_if_root():
    if os.geteuid() != 0:
        print(
            colored(
                "Root permissions are required to run the script; please execute it with the `sudo` command.",
                "red",
            )
        )
        exit(1)


def check_proxy(proxy_url, proxy_type):
    url = "http://www.google.com"
    proxy = f"{proxy_type}://{proxy_url}"

    proxies = {"http": proxy, "https": proxy}

    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(colored(f"Proxy {proxy_url} ({proxy_type}) is available.", "green"))
            return True
        else:
            print(
                colored(
                    f"Proxy {proxy_url} ({proxy_type}) is not available. Status code: {response.status_code}",
                    "red",
                )
            )
            return False
    except requests.exceptions.ProxyError:
        print(
            colored(f"Proxy {proxy_url} ({proxy_type}) is invalid or blocked.", "red")
        )
    except requests.exceptions.ConnectTimeout:
        print(
            colored(
                f"Proxy {proxy_url} ({proxy_type}) is not responding in time.", "red"
            )
        )
    except requests.exceptions.RequestException as e:
        print(
            colored(
                f"Error occurred while checking the proxy {proxy_url} ({proxy_type}): {e}",
                "red",
            )
        )
    return False


def get_proxies(url, proxy_type, max_proxies):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        proxy_list = response.text.splitlines()

        for proxy in proxy_list:
            if len(new_proxies_list) >= max_proxies:
                break
            if proxy_type == "none":
                if "://" in proxy:
                    protocol, proxy_url = proxy.split("://")
                    if check_proxy(proxy_url, protocol):
                        new_proxies_list.append(
                            f"{protocol} {proxy_url.replace(':', ' ')}"
                        )
            else:
                proxy_url = proxy
                if check_proxy(proxy_url, proxy_type):
                    new_proxies_list.append(
                        f"{proxy_type} {proxy_url.replace(':', ' ')}"
                    )
    except requests.exceptions.RequestException as e:
        print(
            colored(f"Error occurred while retrieving proxies from {url}: {e}", "red")
        )


def update_proxychains_config(file_path, new_proxies):

    with open(file_path, "r") as file:
        lines = file.readlines()

    proxy_list_index = None
    for i, line in enumerate(lines):
        if line.strip() == "[ProxyList]":
            proxy_list_index = i
            break

    if proxy_list_index is None:
        raise ValueError("Could not find '[ProxyList]' in the configuration file.")

    new_content = lines[: proxy_list_index + 1]
    new_content.extend([f"{proxy}\n" for proxy in new_proxies])

    with open(file_path, "w") as file:
        file.writelines(new_content)


def load_sources(file_path):
    sources = []
    with open(file_path, "r") as file:
        for line in file:
            if "|" in line:
                protocol, url = line.strip().split("|", 1)
                sources.append((protocol, url))
            else:
                print(
                    colored(
                        f"Skipping invalid line in sources file: {line.strip()}", "red"
                    )
                )
    return sources


def load_config(file_path):
    with open(file_path, "r") as file:
        config = json.load(file)
    return config


if __name__ == "__main__":
    check_if_root()

    config = load_config("config.json")
    proxychains_conf_file = config.get("proxychains-path")
    max_proxies = int(config.get("max-proxys", 100))
    auto_update = config.get("auto-update", "1") == "1"
    new_proxies_list = []

    proxy_sources = load_sources("sources.txt")

    for proxy_type, url in proxy_sources:
        if len(new_proxies_list) >= max_proxies:
            break
        get_proxies(url, proxy_type, max_proxies)

    if new_proxies_list:
        if auto_update:
            update_proxychains_config(proxychains_conf_file, new_proxies_list)
            print("Proxychains configuration has been updated.")
        else:
            user_input = (
                input("Update proxychains configuration now? (y/n): ").strip().lower()
            )
            if user_input == "y":
                update_proxychains_config(proxychains_conf_file, new_proxies_list)
                print("Proxychains configuration has been updated.")
            else:
                print("Proxychains configuration update skipped.")
