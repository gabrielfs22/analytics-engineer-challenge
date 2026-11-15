# AGENTS.md — Analytics Engineer Challenge

Modelo dimensional (star schema) de dados de logística com dbt + DuckDB, processamento e exportação de CSV em Python. Detalhes em `README.md`.

## Regras
- Não instalar dependências sem autorização do usuário.
- Não modificar arquivos fora da pasta do projeto sem autorização.
- Escopo estrito: implementar só o que a tarefa pede.
- Nunca declarar teste como aprovado sem executá-lo e ler a saída.
- Transformações ficam nos modelos dbt (`dbt_project/`); Python só processa e exporta.
- Não versionar credenciais de e-mail/SFTP nem dados brutos novos sem autorização.

## Knowledge OS (contexto global)
- O conhecimento aprovado (decisões, pesquisa, estado do projeto) vive no repositório separado `knowledge-os`, aberto como pasta irmã no workspace `AI-Workspace.code-workspace`. Ponto de entrada: `vault/99-indexes/Home.md`.
- **Este repositório é a fonte de verdade da implementação.** Em conflito entre o Vault e o código daqui, vale o código; sinalize a divergência em vez de corrigir o Vault silenciosamente.
- Propostas de conhecimento vão para `vault/00-inbox/` do `knowledge-os` (nunca promover a `canonical` sem revisão do usuário). Regras completas: `AGENTS.md` do `knowledge-os`.
- Se o Vault não estiver acessível no workspace, siga apenas este arquivo; não procure nem crie o Vault em outros locais.

## Estrutura
- `dbt_project/` modelos, seeds e testes dbt
- `notebooks/` limpeza e exportação
- `src/`, `tests/` código Python e testes
- `run_pipeline.py`, `Makefile` orquestração

## Validação
```
dbt test --project-dir dbt_project --profiles-dir dbt_project
pytest
```
