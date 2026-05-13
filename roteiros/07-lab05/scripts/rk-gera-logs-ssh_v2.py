import random
import os
from datetime import datetime

def carregar_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        exit()
    with open(nome_arquivo, 'r') as f:
        linhas = [linha.strip() for linha in f if linha.strip()]
    if not linhas:
        print(f"Erro: Arquivo '{nome_arquivo}' está vazio.")
        exit()
    return linhas

def gerar_logs():
    # 1. Quantidade de logs
    try:
        qtd_logs = int(input("Quantidade de Logs a gerar: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return

    # 2. Tipo de log e cenário
    print("\nDeseja gerar:")
    print("[1] Logs SSH com Tentativas com Sucesso (Accepted)")
    print("[2] Logs SSH com Falhas de Acesso de várias Origens")
    print("[3] Logs SSH com Falhas de Acesso com um IP de Origem (Força Bruta)")
    opcao = input("Opção: ")

    if opcao not in ['1', '2', '3']:
        print("Opção inválida.")
        return

    # 3. Nome do arquivo
    nome_arquivo = input("\nNome do arquivo gerado (padrão: teste.log): ").strip()
    if not nome_arquivo:
        nome_arquivo = "teste.log"

    # Carregar dados dos arquivos auxiliares
    lista_usuarios = carregar_arquivo('users.txt')
    lista_ips_total = carregar_arquivo('ips.txt')

    logs_gerados = []
    timestamp_base = datetime.now()

    # --- LÓGICA DO CENÁRIO 1: SUCESSO ---
    if opcao == '1':
        status = "Accepted password"
        usuario_fixo = random.choice(lista_usuarios)
        # No máximo 3 IPs de origem aleatórios do arquivo ips.txt
        ips_pool = random.sample(lista_ips_total, min(3, len(lista_ips_total)))
        
        for i in range(qtd_logs):
            ip = random.choice(ips_pool)
            timestamp = timestamp_base.strftime("%b %d %H:%M:%S")
            porta = random.randint(30000, 65000)
            log = f"{timestamp} server-ssh sshd[1001]: {status} for {usuario_fixo} from {ip} port {porta} ssh2"
            logs_gerados.append(log)

    # --- LÓGICA DO CENÁRIO 2: FALHAS DE VÁRIAS ORIGENS ---
    elif opcao == '2':
        status = "Failed password"
        # Criação de pool para limitar repetição de IP em no máximo 3 vezes
        pool_ips = []
        for ip in lista_ips_total:
            pool_ips.extend([ip] * 3)
        random.shuffle(pool_ips)

        for i in range(qtd_logs):
            # Se o pool esvaziar antes de atingir a quantidade de logs, reinicia o pool
            if not pool_ips:
                for ip in lista_ips_total:
                    pool_ips.extend([ip] * 3)
                random.shuffle(pool_ips)
            
            ip = pool_ips.pop()
            user = random.choice(lista_usuarios)
            timestamp = timestamp_base.strftime("%b %d %H:%M:%S")
            porta = random.randint(30000, 65000)
            log = f"{timestamp} server-ssh sshd[1002]: {status} for {user} from {ip} port {porta} ssh2"
            logs_gerados.append(log)

    # --- LÓGICA DO CENÁRIO 3: FORÇA BRUTA (UM IP ÚNICO) ---
    elif opcao == '3':
        status = "Failed password"
        # Um único IP de origem aleatório para todos os logs
        ip_unico = random.choice(lista_ips_total)
        
        for i in range(qtd_logs):
            user = random.choice(lista_usuarios)
            timestamp = timestamp_base.strftime("%b %d %H:%M:%S")
            porta = random.randint(30000, 65000)
            log = f"{timestamp} server-ssh sshd[1003]: {status} for {user} from {ip_unico} port {porta} ssh2"
            logs_gerados.append(log)

    # Gravação dos resultados
    with open(nome_arquivo, 'w') as f:
        f.write("\n".join(logs_gerados) + "\n")

    print(f"\nSucesso! Arquivo '{nome_arquivo}' gerado com {len(logs_gerados)} linhas.")

if __name__ == "__main__":
    gerar_logs()
