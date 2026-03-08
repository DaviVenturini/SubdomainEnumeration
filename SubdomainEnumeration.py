# Script base para enumeração de subdomains
# Ferramenta pode ser usada para converter scripts Python em executáveis ​​do Windows? py2exe | PyInstaller


import requests
import argparse
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def testar_subdominio(sub, dominio, timeout):
    protocolos = ["http", "https"]

    for protocolo in protocolos:
        url = f"{protocolo}://{sub}.{dominio}"
        try:
            resposta = requests.get(url, timeout=timeout)
            return f"[+] {resposta.status_code} -> {url}"
        except requests.RequestException:
            continue

    return None

def main():
    parser = argparse.ArgumentParser(
        description="Enumerador de subdomínios com multithreading e suporte a HTTP/HTTPS"
    )
    parser.add_argument("dominio", help="Domínio alvo. Exemplo: google.com")
    parser.add_argument(
        "-w",
        "--wordlist",
        default="wordlist2-subdomains.txt", # substitua por outra wordlist que quiser.
        help="Caminho da wordlist (padrão: wordlist2-subdomains.txt)",
    )
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=20,
        help="Quantidade de threads (padrão: 20)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=3,
        help="Timeout das requisições em segundos (padrão: 3)",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Arquivo para salvar os resultados encontrados",
    )

    args = parser.parse_args()

    caminho_wordlist = args.wordlist
    if not os.path.isabs(caminho_wordlist):
        base_path = os.path.dirname(__file__)
        caminho_wordlist = os.path.join(base_path, caminho_wordlist)

    if not os.path.exists(caminho_wordlist):
        print(f"[-] Wordlist não encontrada: {caminho_wordlist}")
        return

    with open(caminho_wordlist, "r", encoding="utf-8") as f:
        subdominios = [linha.strip() for linha in f if linha.strip()]

    print(f"[+] Domínio alvo: {args.dominio}")
    print(f"[+] Wordlist: {caminho_wordlist}")
    print(f"[+] Threads: {args.threads}")
    print(f"[+] Timeout: {args.timeout}s")
    print(f"[+] Total de entradas: {len(subdominios)}")
    print()

    resultados = []

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        tarefas = {
            executor.submit(testar_subdominio, sub, args.dominio, args.timeout): sub
            for sub in subdominios
        }

        for future in as_completed(tarefas):
            resultado = future.result()
            if resultado:
                print(resultado)
                resultados.append(resultado)

    if args.output and resultados:
        with open(args.output, "w", encoding="utf-8") as f:
            for linha in resultados:
                f.write(linha + "\n")
        print(f"\n[+] Resultados salvos em: {args.output}")

    print(f"\n[+] Finalizado. Total encontrados: {len(resultados)}")

if __name__ == "__main__":
    main()