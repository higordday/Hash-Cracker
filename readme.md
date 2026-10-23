
# 🔓 Hash Cracker

Script em **Python** para "crackear" hashes por ataque de dicionário (wordlist), com suporte a múltiplos formatos e múltiplas threads.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## ✨ Funcionalidades

- Suporte a múltiplos algoritmos de hash: `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `md5`
- Aceita um hash único, vários hashes separados por `:` ou um arquivo com uma lista de hashes
- Detecção automática do formato do hash quando não especificado
- Ataque de dicionário (wordlist) com múltiplas threads em paralelo
- Saída colorida no terminal com o resultado de cada tentativa

## 🛠️ Tecnologias

| Dependência | Uso |
| --- | --- |
| [hashlib](https://docs.python.org/3/library/hashlib.html) | Geração dos hashes (biblioteca padrão do Python) |
| [threading](https://docs.python.org/3/library/threading.html) | Execução das tentativas em paralelo (biblioteca padrão) |
| [argparse](https://docs.python.org/3/library/argparse.html) | Leitura dos argumentos de linha de comando (biblioteca padrão) |
| [colorama](https://pypi.org/project/colorama/) | Saída colorida no terminal |

## 📁 Estrutura do projeto

```
Hash-Cracker/
├── main.py       # Script principal
└── .gitignore
```

## 🚀 Como executar

### Pré-requisitos

- [Python 3](https://www.python.org/downloads/) instalado

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/higordday/Hash-Cracker.git

# 2. Acesse a pasta do projeto
cd Hash-Cracker

# 3. Instale as dependências
pip install colorama
```

### Execução

```bash
python main.py --hashes <hash> --wordlist <arquivo.txt>
```

#### Argumentos

| Argumento | Obrigatório | Descrição |
| --- | --- | --- |
| `-v`, `--hashes` | ✅ | Hash único, múltiplos (`hash1:hash2:hash3`) ou caminho de um arquivo de texto com uma lista de hashes |
| `-w`, `--wordlist` | ✅ | Caminho do arquivo de wordlist |
| `-f`, `--default-format` | ❌ | Formato do hash (`sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `md5`). Se omitido, todos os formatos são testados |

#### Exemplos

```bash
# Hash único, com detecção automática do formato
python main.py --hashes 5f4dcc3b5aa765d61d8327deb882cf99 --wordlist rockyou.txt

# Múltiplos hashes, com formato definido
python main.py --hashes 5f4dcc3b5aa765d61d8327deb882cf99:e99a18c428cb38d5f260853678922e03 --wordlist rockyou.txt --default-format md5

# Lista de hashes a partir de um arquivo
python main.py --hashes hashes.txt --wordlist rockyou.txt
```