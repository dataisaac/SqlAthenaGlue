# SqlAthenaGlue

Este projeto é uma pipeline simples para processar arquivos CSV, convertê-los em formatos JSON e Parquet, e fazer upload do Parquet para o Amazon S3. Ideal para preparar dados para análise no AWS Glue e Athena.

## Funcionalidades
- Lê um arquivo CSV e converte para JSON e Parquet.
- Faz upload do arquivo Parquet para um bucket S3.
- Usa credenciais AWS via variáveis de ambiente (seguro).

## Requisitos
- Python 3.8+
- Pacotes: pandas, pyarrow, boto3
- Conta AWS com acesso ao S3

## Instalação
1. Clone o repositório:
   ```
   git clone https://github.com/dataisaac/SqlAthenaGlue.git
   cd SqlAthenaGlue
   ```

2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv38
   venv38\Scripts\activate  # No Windows
   ```

3. Instale as dependências:
   ```
   pip install pandas pyarrow boto3
   ```

## Configuração
Defina as variáveis de ambiente com suas credenciais AWS:
```
AWS_ACCESS_KEY_ID=sua-chave-aqui
AWS_SECRET_ACCESS_KEY=sua-chave-secreta-aqui
AWS_REGION=sa-east-1
```

No PowerShell:
```
$env:AWS_ACCESS_KEY_ID = "sua-chave"
$env:AWS_SECRET_ACCESS_KEY = "sua-chave-secreta"
$env:AWS_REGION = "sa-east-1"
```

## Uso
Execute o script principal:
```
python script.py
```

Isso processará `data/moviesAndTv.csv`, gerará JSON e Parquet em `output_files/`, e subirá o Parquet para o S3.

### Personalização
Edite `script.py` para mudar os caminhos ou bucket.

## Estrutura do Projeto
- `csvToParquet.py`: Função principal de processamento.
- `script.py`: Executor com parâmetros fixos.
- `data/`: Pasta com arquivos CSV de entrada.
- `output_files/`: Arquivos gerados (JSON e Parquet).

## Próximos Passos
- Configure um Crawler no AWS Glue para indexar o Parquet no S3.
- Use o Athena para consultar os dados com SQL.

## Erros e Aprendizados
Durante o desenvolvimento, enfrentei desafios como exposição de credenciais AWS e bloqueios no GitHub devido à proteção de secrets. Esses erros foram oportunidades valiosas para aprender:
- **Segurança:** A importância de usar variáveis de ambiente em vez de hardcodear credenciais.
- **Versionamento:** Como lidar com regras de repositório e push protection no GitHub.
- **Boas Práticas:** Refatorar código para ser mais seguro e reutilizável.

Esses aprendizados tornaram o projeto mais robusto e me prepararam para futuros desenvolvimentos na AWS.