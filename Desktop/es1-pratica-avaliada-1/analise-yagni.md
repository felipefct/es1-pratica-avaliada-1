# Felipe Faria de Carvalho Tavares

# Análise de Violação do Princípio YAGNI

Conforme o princípio YAGNI (*You Aren't Gonna Need It*), devemos implementar apenas o que é necessário para os requisitos atuais (cadastrar, fazer login, listar)[cite: 1]. O código original violava isso ao tentar prever funcionalidades futuras[cite: 3].

## Atributos Desnecessários Removidos
**Na classe `Usuario`:**
* `id`, `data_cadastro`, `ultimo_login`
* `perfil`, `permissoes`, `configuracoes`, `historico_logins`
* `foto_perfil_url`, `telefone`, `endereco`, `empresa`, `cargo`, `departamento`
* *Por que violam YAGNI?* Nenhum desses atributos é exigido no momento para o cadastro básico ou login[cite: 1]. Eles antecipam um sistema de perfis, auditoria de acessos e dados de RH/pessoais que não foram solicitados, adicionando complexidade inútil[cite: 3].

## Métodos Desnecessários Removidos
**Na classe `Usuario`:**
* `_gerar_id`, `adicionar_permissao`, `remover_permissao`, `tem_permissao`, `atualizar_configuracao`
* `registrar_login`, `exportar_json`, `exportar_xml`, `atualizar_foto_perfil`, `atualizar_dados_profissionais`
* *Por que violam YAGNI?* Métodos focados em exportação de dados, gestão de cargos, permissões granulares e upload de fotos não fazem parte das funcionalidades básicas solicitadas (cadastro, login, listagem)[cite: 1, 3].

**Na classe `GerenciadorUsuarios`:**
* `_atualizar_cache`, `buscar_por_id`, `buscar_por_perfil`, `buscar_por_permissao`
* `exportar_todos_json`, `importar_usuarios_json`, `gerar_relatorio_atividade`
* *Por que violam YAGNI?* O uso de sistema de cache em memória, importação/exportação de lotes e geração de relatórios de métricas antecipa problemas de escala e gestão que a startup ainda não possui, encarecendo a manutenção do código sem necessidade[cite: 3].