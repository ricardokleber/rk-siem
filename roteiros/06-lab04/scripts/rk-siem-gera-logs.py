import random
import time
from datetime import datetime

# Bancos de dados fictícios para os logs
IPS = ["192.168.1.10", "10.0.0.5", "172.16.0.2", "45.33.11.2", "185.22.14.5", "200.150.10.1", "8.8.8.8"]
USERS = ["root", "admin", "user1", "guest", "webmaster", "support", "devops", "db_admin"]
PAGES = ["/index.html", "/login", "/admin/dashboard", "/api/v1/user", "/wp-login.php", "/config.php"]
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "curl/7.68.0",
    "python-requests/2.25.1"
]

def generate_apache_log():
    ip = random.choice(IPS)
    date = datetime.now().strftime('%d/%b/%Y:%H:%M:%S +0000')
    method = random.choice(["GET", "POST", "PUT", "DELETE"])
    page = random.choice(PAGES)
    status = random.choice([200, 201, 404, 500, 403, 301])
    size = random.randint(150, 8000)
    agent = random.choice(USER_AGENTS)
    return f'{ip} - - [{date}] "{method} {page} HTTP/1.1" {status} {size} "-" "{agent}"'

def generate_ssh_log():
    ip = random.choice(IPS)
    user = random.choice(USERS)
    date = datetime.now().strftime('%b %d %H:%M:%S')
    host = "host04"
    
    if random.random() > 0.6: # 40% de chance de sucesso, 60% de falha
        return f'{date} {host} sshd[{random.randint(1000, 9999)}]: Failed password for {user} from {ip} port {random.randint(30000, 60000)} ssh2'
    else:
        return f'{date} {host} sshd[{random.randint(1000, 9999)}]: Accepted password for {user} from {ip} port {random.randint(30000, 60000)} ssh2'

def main():
    print("--- Gerador de Logs Customizado ---")
    
    # 1. Escolha do tipo
    print("\n[1] Apache2 (HTTP)")
    print("[2] SSH (Auth)")
    service_choice = input("Escolha o tipo de log (1 ou 2): ")

    # 2. Quantidade de linhas
    try:
        num_lines = int(input("Quantas linhas de log deseja gerar? "))
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
        return

    # 3. Nome do arquivo
    output_file = input("Digite o nome do arquivo de saída (ex: teste.log): ")

    print(f"\nIniciando geração de {num_lines} linhas em '{output_file}'...")

    try:
        with open(output_file, "w") as f:
            for i in range(num_lines):
                if service_choice == "1":
                    line = generate_apache_log()
                else:
                    line = generate_ssh_log()
                
                f.write(line + "\n")
                
                # Exibe progresso a cada 10% para não travar o terminal em arquivos gigantes
                if num_lines > 100 and i % (num_lines // 10) == 0:
                    print(f"Progresso: {round((i/num_lines)*100)}%...")

        print(f"\nSucesso! Arquivo '{output_file}' gerado com {num_lines} linhas.")
    
    except Exception as e:
        print(f"Ocorreu um erro ao gravar o arquivo: {e}")

if __name__ == "__main__":
    main()
