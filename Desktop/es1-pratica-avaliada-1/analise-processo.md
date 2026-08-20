# Felipe Faria de Carvalho Tavares

# Análise de Processo - AgileTech Solutions

# a) Manifesto Ágil e Práticas Adotadas

## Aplicação dos 4 Valores do Manifesto Ágil no Contexto da AgileTech
1. **Indivíduos e interações mais que processos e ferramentas:** Como a AgileTech possui uma equipe pequena de 5 desenvolvedores e 1 Product Owner, a comunicação direta e constante é mais eficaz do que a criação de fluxos burocráticos. 
2. **Software em funcionamento mais que documentação abrangente:** A empresa possui um histórico de projetos anteriores onde a documentação extensa ficava rapidamente desatualizada[cite: 1]. Focar em entregar software funcionando atende à pressão por entregas rápidas para demonstrar valor[cite: 1].
3. **Colaboração com o cliente mais que negociação de contratos:** O cliente é participativo, porém tem disponibilidade limitada[cite: 1]. Trabalhar de forma colaborativa quando ele está disponível garante alinhamento.
4. **Responder a mudanças mais que seguir um plano:** Os requisitos iniciais do sistema web são vagos e estão sujeitos a mudanças frequentes[cite: 1]. Responder rapidamente é fundamental.

## Justificativa: Abordagem Ágil vs. Processo Tradicional (Cascata)
O modelo Cascata exige que requisitos e design sejam definidos e documentados antes da implementação. Dado que a AgileTech sofre com requisitos vagos e mudanças frequentes[cite: 1], o Cascata causaria atrasos. A abordagem ágil permite adaptação contínua e entregas rápidas para validação de mercado[cite: 1].

## 3 Práticas Ágeis para Adoção Imediata
1. **Sprints (Ciclos Curtos):** Para lidar com a pressão de demonstrar valor rapidamente ao mercado[cite: 1].
2. **Daily Stand-up:** Para alinhar a equipe diariamente, já que o cliente tem tempo limitado e os requisitos mudam muito[cite: 1].
3. **Refinamento do Backlog:** Encontros para detalhar histórias de usuário, resolvendo o problema dos requisitos iniciais vagos[cite: 1].

---

# b) Programação em Pares (Pair Programming)

## Conceito e Benefícios
Dois desenvolvedores trabalham juntos no mesmo computador. O "Piloto" digita o código e o "Navegador" revisa em tempo real e pensa na arquitetura.
**Benefícios:** Redução de bugs, compartilhamento de conhecimento e maior aderência ao código limpo.

## Desafios no Contexto EAD
* Latência de internet e problemas de conexão ao compartilhar tela.
* Conflitos de agenda, pois alunos em EAD geralmente possuem horários flexíveis.
* Dificuldade de comunicação não-verbal.

## Adaptações Viáveis para Equipes Remotas
1. **Ferramentas Síncronas (Live Share):** Usar extensões no VS Code para editar o mesmo código simultaneamente, exigindo menos internet.
2. **Ping-Pong Assíncrono:** Um desenvolvedor escreve o teste automatizado e envia; o outro, no seu horário, escreve a implementação e cria um novo teste, respeitando a flexibilidade de horários.

---

# c) Dificuldades Essenciais de Brooks

## Dificuldades Mais Relevantes
1. **Mutabilidade:** O software sofre pressão por mudanças. O cenário tem requisitos vagos que mudam frequentemente[cite: 1].
2. **Invisibilidade:** O software é abstrato, gerando ansiedade e pressão por demonstrações rápidas para provar valor[cite: 1].

## Mitigação Através de Métodos Ágeis
* **Para a Mutabilidade:** O escopo é gerenciado em um Backlog priorizado, e as mudanças são bem-vindas a cada nova Sprint.
* **Para a Invisibilidade:** Cerimônias como a "Sprint Review" tornam o progresso visível ao cliente frequentemente através de software funcional[cite: 1].