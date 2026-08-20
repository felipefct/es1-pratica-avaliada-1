# Felipe Faria de Carvalho Tavares

# Estruturação de Processo: XP e Scrum

# Link do Quadro Kanban (GitHub Projects): [ https://github.com/users/felipefct/projects/1/views/1 ]

## Integração de Práticas XP e Framework Scrum

A equipe adotará o framework Scrum para o gerenciamento e fluxo de trabalho, enquanto as práticas de Extreme Programming (XP) atuarão na camada de engenharia e qualidade de código[cite: 1].

## 5 Práticas de XP Adotadas
1. **Design Simples (YAGNI):** Focar em resolver os problemas atuais sem tentar antecipar complexidades não solicitadas (ex: refatoração da classe Usuario).
2. **Programação em Pares (Pair Programming):** Desenvolvedores codificando juntos para melhorar qualidade e disseminar conhecimento.
3. **Integração Contínua (CI):** Código integrado e testado diversas vezes ao dia no repositório.
4. **Refatoração:** Melhorar a estrutura do código continuamente sem alterar seu comportamento externo, mantendo-o limpo.
5. **Propriedade Coletiva do Código:** Qualquer desenvolvedor pode e deve melhorar qualquer parte do código quando necessário.

## Fluxo de Trabalho Semanal da Equipe
* **Segunda-feira:** Sprint Planning (Planejamento da Sprint e seleção de itens do Backlog).
* **Terça a Sexta-feira:** Daily Scrum (15 min) diário para alinhamento. Desenvolvimento aplicando Pair Programming e Integração Contínua.
* **Última Sexta-feira da Sprint:** Sprint Review (apresentar o incremento ao cliente) seguido da Sprint Retrospective (melhoria contínua da equipe)[cite: 1].

---

## Cronograma de uma Sprint de 2 Semanas

| Dia | Evento / Cerimônia | Duração | Participantes | Práticas XP em Ação |
|---|---|---|---|---|
| **Semana 1 - Seg** | Sprint Planning | 2 a 4 horas | PO, Desenvolvedores | Design Simples (estimativas) |
| **Semana 1 - Ter a Sex** | Daily Scrum | 15 min / dia | Desenvolvedores | Pair Programming, CI |
| **Semana 2 - Seg a Qui** | Daily Scrum | 15 min / dia | Desenvolvedores | Refatoração, Propriedade Coletiva |
| **Semana 2 - Sex** | Sprint Review | 1 a 2 horas | PO, Devs, Cliente | Software Funcionando |
| **Semana 2 - Sex** | Sprint Retrospective | 1 hora | PO, Desenvolvedores | Avaliação do processo |

**Entregas Esperadas ao Final da Sprint:** Um incremento de software funcional, devidamente testado (via Integração Contínua) e aprovado pelo Product Owner, pronto para ir para produção.

---

## Comparativo: Scrum vs Kanban

| Característica | Scrum | Kanban | Combinação (Scrumban) |
|---|---|---|---|
| **Quando usar** | Projetos com requisitos que mudam, mas que podem ser planejados em ciclos. | Projetos com fluxo contínuo de demandas e sustentação (ex: correções de bugs). | Quando se deseja planejar ciclos (Sprints) mas ter um fluxo visual forte das tarefas. |
| **Cadência** | Iterações fixas (Sprints de 1 a 4 semanas). | Fluxo contínuo, entregas feitas assim que a tarefa termina. | Sprints fixas com gestão visual contínua. |
| **Papéis** | Bem definidos (Product Owner, Scrum Master, Developers). | Não prescreve papéis obrigatórios. | Mantém os papéis do Scrum. |
| **Limites de Trabalho (WIP)**| Indireto, limitado pelo que cabe na Sprint. | Direto, limite rigoroso por coluna no quadro Kanban. | Limites de WIP aplicados às Sprints do Scrum. |