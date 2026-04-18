![](../assets/rk-siem-titulo_instalacao.png)
***
### RK-SIEM :: Instalação

***
#### Baixe e comece a usar já:

###### 1.Pra começar verifique se o limite de mapas de memória virtual do kernel do seu Linux está configurado adequadamente: 

```
cat /proc/sys/vm/max_map_count
```

Se o valor estiver menor que **262.144** você deverá ajustá-lo (caso contrário o docker irá falhar ao iniciar).

###### Edite o arquivo /etc/sysctl.conf e adicione a linha:
```
vm.max_map_count=262144
```
#### 2. Baixe o docker-compose.yml pronto: 

```
git clone https://github.com/ricardokleber/rk-siem.git
```
#### 3. Entre no diretório do projeto: 
```
cd rk-siem
```
#### 4. Baixe as imagens dos contêineres para sua estação: 
```
docker compose pull
```
#### 5. Inicie o docker com o Indexador do RK-SIEM (rk-siem-core): 
```
docker compose up -d rk-siem-core
```
Aguarde alguns instantes (1 a 2 minutos em média) para o **rk-siem-core** executar o Java com todos os módulos e configurações padrões.

#### 6. Inicie o docker com a Interface Web do RK-SIEM (rk-siem-ui): 
```
docker compose up -d rk-siem-ui
```
Aguarde alguns instantes (1 minuto em média) para o **rk-siem-ui** executar, ativar configurações padrões e disponibilizar o acesso web.

#### 7. Pronto!!! Agora é só acessar em seu navegador a interface Web do RK-SIEM: 
```
http://localhost:5601
```
![](assets/rk-siem-login.png)

**Username:** *admin* | **Password:** *admin*

***

**Vídeos do RK-SIEM (Youtube):**

<a href="https://www.youtube.com/playlist?list=PLzEiYA7yCrq9-Dub9qwmFJFbh2NMoOjTh" target="_blank"><img width="400" height="120" alt="assistavideo" src="assets/rk-siem-youtube.png" /></a>