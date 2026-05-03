# smart-attendance-system
Sistema distribuído de controle de presença via QR Code, desenvolvido com foco em alta concorrência, prevenção de fraudes e integração institucional.

## Equipe
1. Emanuel Gimarães
2. Evelen Pinheiro
3. Marcos Braga
4. Robson Campos
5. Samuel Couto

## Descrição
O sistema automatiza o registro de presença em salas de aula utilizando QR Codes dinâmicos. A aplicação valida a presença através de geolocalização e verificação de rede, garantindo que o aluno esteja fisicamente presente no local da aula. O backend é integrado ao Google OAuth2 para permitir que alunos e professores acessem o sistema usando suas contas institucionais da UFVJM.

## Arquitetura & Design
O projeto foi estruturado seguindo princípios de DDD (Domain-Driven Design) e Arquitetura Limpa, separando responsabilidades em camadas:
- Interfaces: Endpoints REST e Serializers.
- Infrastructure: Implementação de banco de dados, integração com Redis e adaptadores de autenticação social.
- Domain/UseCases: Lógica de negócio central (registro de presença, validação de geolocalização).

### Decisões Técnicas
- Autenticação: Stateless usando JWT (JSON Web Tokens) via SimpleJWT.
- Social Auth: Integração com Google OAuth2 via django-allauth.
- Segurança: Credenciais sensíveis protegidas por variáveis de ambiente (.env).
- Escalabilidade: Cache de QR Codes com Redis e comunicação assíncrona via RabbitMQ (em desenvolvimento).

## Tech Stack
- Framework: Django & Django REST Framework (DRF)
- Database: PostgreSQL (Persistência)
- Cache: Redis (Frequência e Tokens temporários)
- Auth: Google OAuth2 & JWT
- DevOps: Python Dotenv

## Rotas da API

### Autenticação (Acesso Público)
| Método | Rota | Descrição |
| --- | --- | --- |
| `POST` | `/api/register` | Criação de Conta Manual. |
| `POST` | `/api/login` | Login tradicional retornando JWT Access/Refresh. |
| `POST` | `/api/auth/google` | Login institucional Google (Envia `access_token` do Google). |

### Gerenciamento (Protegidas - Requer JWT)
| Endponit | Descrição | Permissões |
| --- | --- | --- |
| `/api/students` | CRUD de Alunos e Perfis | Admin / Professor |
| `/api/professors` | CRUD de Professores | Admin |
| `/api/disciplines` | Gestão de Disciplinas e Matrículas | Admin / Professor |
| `/api/rooms` | Cadastro de Salas e Coordenadas GPS | Admin |
| `/api/class_sessions` | Criação e Gestão de Aulas | Admin / Professor |
| `/api/attendances` | Registro e Consulta de Presenças | Admin / Professor / Aluno |

## Como Executar o Projeto
1. Clone o repositório
```
git clone -b development --single-branch https://github.com/MarcosBraga1/smart-attendance-system.git
cd smart-attendance-system
```

2. Configure o Ambiente Virtual e Instale as Dependências
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Variáveis de Ambiente
   
Renomeie o arquivo `.env.example` para `.env` e preencha com suas credenciais locais.
```
cp .env.example .env
```
*Certifique-se de preencher GOOGLE_CLIENT_ID e GOOGLE_CLIENT_SECRET obtidos no Google Cloud Console.*

5. Migração e Execução
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
