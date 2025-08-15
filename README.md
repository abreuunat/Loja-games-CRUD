# 🎮 Sistema de Gerenciamento de Jogos e Compras

Este projeto é uma aplicação **Flask + SQLite** para gerenciar **jogos** e **compras** de clientes.  
O sistema permite cadastrar, listar, editar e excluir jogos, bem como registrar compras associadas a esses jogos.

---

## 📌 Entidades

### 1. **Jogo**
Representa um jogo disponível para compra.

| Campo       | Tipo   | Descrição |
|-------------|--------|-----------|
| `id`        | INTEGER (PK) | Identificador único do jogo |
| `titulo`    | TEXT | Nome do jogo |
| `genero`    | TEXT | Gênero do jogo (Ação, RPG, Esporte, etc.) |
| `plataforma`| TEXT | Plataforma disponível (PC, PS5, Xbox, etc.) |
| `preco`     | REAL | Valor do jogo |

---

### 2. **Compra**
Registra uma compra feita por um cliente, vinculada a um jogo.

| Campo         | Tipo   | Descrição |
|---------------|--------|-----------|
| `id`          | INTEGER (PK) | Identificador único da compra |
| `data_compra` | DATE | Data em que a compra foi realizada |
| `cliente_nome`| TEXT | Nome do cliente que realizou a compra |
| `jogo_id`     | INTEGER (FK) | Referência ao jogo comprado |

---

## 🔗 Relacionamento
- **1 Jogo → N Compras**  
  Um jogo pode ser comprado várias vezes, mas cada compra está vinculada a apenas **um jogo**.


### Executando o projeto
1. Criar ambiente virtual
    ```
    python -m venv venv
    ```
2. Ativar ambiente virtual
    ```
    source venv\Scripts\activate
    ```
   2.1. Atualizar o pip
   ```
    pip install --upgrade pip
    ```
3. Instalar o Flask
    ```
    pip install Flask
    ```
4. Executar o script `run.py`
```
python run.py
```