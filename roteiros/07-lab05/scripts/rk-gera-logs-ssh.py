import random
import os
from datetime import datetime

def generate_random_ip():
    """Gera um endereço IP IPv4 aleatório."""
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def load_users(filename="users.txt"):
    """Carrega usuários de um arquivo externo com tratamento de encoding."""
    if os.path.exists(filename):
        # Usando errors='ignore' ou encoding latin-1 para evitar quebras por caracteres especiais
        try:
            with open(filename, "r", encoding="latin-1") as f:
                users = [line.strip() for line in f if line.strip()]
            if users:
                print(f"--- Sucesso: {len(users)} usuários carregados de '{filename}'. ---")
                return users
        except Exception as e:
            print(f"Erro ao ler arquivo de usuários: {e}")
    
    print(f"--- Aviso: Arquivo '{filename}' não encontrado ou problemático. Usando padrão 'root'. ---")
    return ["root"]

def generate_ssh_log(event_type, users_list):
    """Gera uma linha de log SSH sorteando um usuário da lista."""
    ip = generate_random_ip()
    user = random.choice(users_list) 
    date = datetime.now().strftime('%b %d %H:%M:%S')
    host = "host04"
    port = random.randint(30000, 60000)
    pid = random.randint(1000, 9999)
    
    status = "Accepted" if event_type == "1" else "Failed"
        
    return f'{date} {host} sshd[{pid}]: {status} password for {user} from {ip} port {port} ssh2'

def main():
    print("--- RK-SIEM : Gerador de Logs SSH ---")
    
    # 1. Carrega a lista
    current_users = load_users("users.txt")
    
    # 2. Escolha do Evento
    print("\nQual tipo de evento SSH deseja gerar?")
    print("[1] Accepted (Sucesso)")
    print("[2] Failed (Falha)")
    event_choice = input("Escolha (1 ou 2): ")

    if event_choice not in ["1", "2"]:
        print("Opção inválida.")
        return

    # 3. Quantidade de linhas
    try:
        num_lines = int(input("Quantas linhas de log deseja gerar? "))
    except ValueError:
        print("Erro: Insira um número inteiro.")
        return

    output_file = input("Nome do arquivo de saída (ex: ssh.log): ")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for i in range(num_lines):
                line = generate_ssh_log(event_choice, current_users)
                f.write(line + "\n")
                
                if num_lines >= 10 and i % (max(1, num_lines // 10)) == 0:
                    print(f"Progresso: {round((i / num_lines) * 100)}%...")

        print(f"\nConcluído! Arquivo '{output_file}' gerado com {num_lines} linhas.")
    
    except Exception as e:
        print(f"Erro ao gravar arquivo de saída: {e}")

if __name__ == '__main__':
    main()
