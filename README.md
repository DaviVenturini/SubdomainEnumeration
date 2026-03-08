# Subdomain Enumeration Tool

Ferramenta simples de **enumeração de subdomínios** desenvolvida em Python para estudos de segurança ofensiva, recon e laboratórios de pentest.

O script utiliza uma **wordlist de subdomínios comuns**, testa **HTTP e HTTPS** e usa **multithreading** para acelerar a descoberta.

---

## Funcionalidades

* Enumeração de subdomínios baseada em **wordlist**
* Teste automático em **HTTP e HTTPS**
* **Multithreading** para maior velocidade
* Suporte a **timeout configurável**
* Possibilidade de **salvar resultados em arquivo**
* Interface simples via **linha de comando**

---

## Bibliotecas utilizadas

O script utiliza as seguintes bibliotecas Python:

* `requests`
* `argparse`
* `os`
* `concurrent.futures` (ThreadPoolExecutor)

Obs: apenas `requests` precisa ser instalada manualmente, pois as outras já fazem parte da biblioteca padrão do Python.

Instalação da biblioteca necessária:

```
pip install requests
```

---

## Como usar

Execute o script informando o **domínio alvo**:

```
python SubdomainEnumeration.py dominio.com
```

---

## Exemplos

Executar com configuração padrão:

```
python SubdomainEnumeration.py google.com
```

Definir número de threads:

```
python SubdomainEnumeration.py google.com -t 50
```

Usar uma wordlist personalizada:

```
python SubdomainEnumeration.py google.com -w wordlist.txt
```

Salvar resultados em arquivo:

```
python SubdomainEnumeration.py google.com -o resultados.txt
```

Definir timeout das requisições:

```
python SubdomainEnumeration.py google.com --timeout 5
```

---

## Exemplo de saída

```
[+] 200 -> https://www.google.com
[+] 301 -> http://mail.google.com
[+] 302 -> https://docs.google.com

[+] Finalizado. Total encontrados: 3
```

---

## Aviso

Esta ferramenta foi criada **apenas para fins educacionais e laboratoriais**.

Utilize somente em:

* ambientes de laboratório
* programas de bug bounty autorizados
* domínios onde você possui permissão para testar

O uso indevido pode violar leis ou políticas de uso.

---

## Licença

Projeto disponibilizado sob licença **MIT**.
