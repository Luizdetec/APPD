# Aplicação de Previsão de Propagação de Doenças

Esta aplicação em Python utiliza Flask como framework web, HTML, CSS, Bootstrap para o front-end, e Postgresql para armazenamento de dados. O objetivo da aplicação é prever a propagação de uma doença na sociedade usando o modelo SIR (Susceptíveis-Infectados-Recuperados) e exibir visualmente a evolução ao longo do tempo.

## Configuração do Ambiente

Certifique-se de ter Python e Postgresql instalados no seu sistema.

Além disso, é necessário configurar o banco de dados Postgresql. Você pode fazer isso executando os seguintes comandos no terminal:

```bash
psql -U postgres
CREATE DATABASE previsao_doencas;
\c previsao_doencas
CREATE TABLE doencas (
	id_doenca SERIAL PRIMARY KEY,
	nome_doenca VARCHAR(255) NOT NULL UNIQUE,
	beta NUMERIC(10,2) NOT NULL CHECK (beta >= 0),
	gamma NUMERIC(10,2) NOT NULL CHECK (gamma >= 0),
	tempo INT NOT NULL CHECK (tempo > 0)
);
```

## Executando a Aplicação

Para iniciar a aplicação, utilize o seguinte comando:

```bash
python app.py
```

## Funcionalidades

1. **Modelo SIR:** A aplicação utiliza o modelo SIR para prever a propagação da doença ao longo do tempo.

2. **Gráfico de Propagação:** Um gráfico é gerado para mostrar a proporção da população ao longo dos dias para os grupos de Suscetíveis, Infectados e Recuperados.

3. **Doenças Padrão e Personalizadas:** A aplicação possui três doenças padrão (H1N1, COVID19 e gripe) e permite aos usuários adicionar suas próprias doenças com valores personalizados de beta e gamma e o tempo (em dias) de simulação.

4. **Armazenamento no Banco de Dados:** As informações sobre as doenças, incluindo nome, beta e gamma, são armazenadas no banco de dados Postgresql.

## Uso da Aplicação

1. **Página Inicial:** Ao acessar a aplicação, você verá as opções para escolher entre as doenças padrão ou adicionar uma nova doença personalizada.

2. **Adicionar Doença Personalizada:** Se escolher adicionar uma doença personalizada, você precisará fornecer o nome da doença, o valor de beta e gamma, e o tempo de duração da doença.

3. **Visualização do Gráfico:** Após escolher a doença, o gráfico será gerado, mostrando a evolução da propagação ao longo do tempo.

4. **Armazenamento de Dados:** As informações sobre a doença adicionada são armazenadas no banco de dados para referência futura.

**Divirta-se explorando a propagação de doenças com a nossa aplicação!**
```
