## 🚀 LaunchLab UniFAP — Guia de Execução do Desafio Semanal
Este é um repositório corporativo e pedagógico de alto desempenho. A sua célula deve seguir rigorosamente as diretrizes contidas neste documento para validar as competências e conquistar a certificação da semana.


## 🛠️ 1. Instruções Iniciais de Configuração (Proibido dar FORK)
O ecossistema do LaunchLab simula o ambiente de engenharia de software do mercado real. Por questões de governança de TI e compliance corporativo, o fluxo de clonagem do projeto deve seguir regras estritas:

1. NÃO DEIXE UM FORK: É terminantemente proibido utilizar o botão Fork do GitHub neste repositório. O fork vincula seu código publicamente ao perfil do professor, quebrando o isolamento das equipes.
2. USE O TEMPLATE: O integrante líder da célula deve clicar exclusivamente no botão verde "Use this template" ➔ "Create a new repository".
3. ALTERE O OWNER: Na tela de criação do novo repositório, mude obrigatoriamente o campo Owner (Dono) do seu perfil pessoal para a organização oficial do programa: LaunchLab-UniFAP.
4. NOMENCLATURA PADRÃO: Nomeie o repositório utilizando estritamente a tag da sua bancada: desafio-w[NUMERO_DA_SEMANA]-[CURSO]-celula[NUMERO_DA_BANCADA]. (Exemplo: desafio-w2-ads-celula04).
5. CONVITE AO PARCEIRO E MONITOR: Vá em Settings ➔ Collaborators ➔ Add people e convide o outro membro da sua dupla e o usuário do GitHub do seu Embaixador.


## 👥 2. Matriz de Papéis e Responsabilidades na Célula
As células operam como equipes autônomas focadas na identidade e no orgulho de cada curso. Ninguém trabalha isolado.
## 🚀 O Papel do Desenvolvedor de ADS

* Missão: Construir o motor operacional, a mecânica lógica e a estabilidade das funções do software.
* Responsabilidade: Implementar algoritmos limpos, garantir o tratamento completo de exceções em tempo de execução e assegurar o sucesso nos testes de integração automatizados do sistema.

## 💼 O Papel do Desenvolvedor de SI

* Missão: Desenvolver a arquitetura estrutural de dados, governança de TI e regras estratégicas de negócio do projeto.
* Responsabilidade: Estruturar os metadados corporativos, implementar funções de validação de viabilidade econômica/processos e redigir as seções de conformidade, compliance legal e impacto do sistema.

## 🛡️ O Papel do Aluno Embaixador

* Missão: Atuar como Líder Técnico e monitor preventivo de ritmo ao longo da semana.
* Responsabilidade: Auditar os gráficos de commits, remover impedimentos de versionamento de código e responder às Issues abertas pelas células utilizando exclusivamente o método socrático.


## ⚠️ 3. Política de Compliance e Uso de Inteligência Artificial (IA)
O uso de ferramentas de IA (como ChatGPT, GitHub Copilot ou Claude) no LaunchLab UniFAP é regulado por normas estritas de ética profissional:

* 🟢 O que é PERMITIDO (Uso como Assistente): Utilizar a IA para explicar mensagens de erro retornadas pelo console do terminal, sugerir conceitos de sintaxe estruturada ou auxiliar na formatação de arquivos markdown.
* 🔴 O que é PROIBIDO (Sujeito a Retenção de Medalha - ND): Gerar o código-fonte por completo via prompts, copiar e colar funções inteiras sem compreender a mecânica, ou utilizar robôs para redigir as análises textuais do relatório.
* A Auditoria Docente: O professor pode realizar inspeções e arguições orais surpresa. Se um aluno for questionado em sala e não souber explicar a arquitetura ou o funcionamento do código assinado por ele, a competência será marcada imediatamente como Não Desenvolvida (ND) para toda a célula, acionando o Contrato de Convivência.


## ▶️ 4. Execução e validação

O projeto utiliza somente a biblioteca padrão do **Python 3.9 ou superior** e
não exige dependências externas.

### Motor de coleta

O motor recebe volumes em metros cúbicos, acumula as entradas válidas e encerra
quando o total alcança 50 m³ ou quando o operador informa `-1`. Valores
negativos, textos e números não finitos são descartados com uma mensagem de
erro. Para executar:

```bash
python3 -m src.coleta_ads
```

Exemplo de entrada:

```text
20
35
```

Nesse cenário, o volume registrado é 55 m³ e o sistema sinaliza que a
capacidade máxima foi atingida. O último volume é preservado para que o dado
real recebido não seja ocultado.

### Governança financeira e ambiental

A regra de viabilidade usa os metadados de `src/governanca_si.py`. Uma viagem
com menos de 30% da capacidade de 50 m³ — isto é, menos de 15 m³ — recebe um
alerta de alto custo de ociosidade.

```bash
python3 -m src.governanca_si
```

### Testes

```bash
python3 -m unittest discover -s tests -v
```

O GitHub Actions executa a compilação, os testes unitários e os dois fluxos de
integração em pushes e pull requests. Ele também valida o padrão Conventional
Commits.

## 📑 5. Relatório de Entrega da Célula (Preenchimento Obrigatório)
Instrução: Edite as seções abaixo preenchendo as evidências críticas da dupla até o prazo limite estipulado no ciclo semanal.
## 📂 Identificação

* Curso: Sistemas de Informação
* Membro 1 (Nome & GitHub): @viniciuslacerd4 - Vinícius Lacerda Borges
* Membro 2 (Nome & GitHub): @matheusbwv - Matheus Wenes
* Embaixador Vinculado: @CaioTarso - Caio Tarso

## 🌍 Seção de Análise Crítica (Formação Geral)

Com base no cenário proposto da semana, descreva qual o impacto humano, social, ético ou ambiental da tecnologia que sua célula colocou em produção. Como as decisões de código impactam o mundo físico e a vida do cidadão/empresa?

💬 RESPOSTA DA CÉLULA: O monitoramento do volume transportado ajuda a reduzir
viagens com baixa ocupação, que aumentam o custo operacional, o consumo de
combustível e a emissão de dióxido de carbono. Ao mesmo tempo, registrar quando
a capacidade foi atingida torna visíveis situações que precisam de avaliação
operacional. Como entradas incorretas poderiam produzir decisões financeiras e
ambientais equivocadas, o sistema rejeita valores negativos, não numéricos e
não finitos. O alerta deve apoiar, e não substituir, a decisão humana: coletas
urgentes ou serviços essenciais podem justificar uma viagem abaixo do limite
econômico estabelecido.

## 🌱 Seção de Compliance Ambiental e Green IT

O monitoramento estruturado do volume transportado transforma dados
operacionais da frota em evidências para a governança de TI. Ao registrar a
capacidade máxima de 50 m³ e considerar como economicamente inviáveis as viagens
com carga inferior a 15 m³, o sistema identifica situações de ociosidade que
aumentam o custo por operação e o consumo desnecessário de combustível. Esses
parâmetros tornam a decisão auditável, pois a mesma regra pode ser aplicada e
conferida em todas as execuções.

Sob a perspectiva de *Green IT*, consolidar cargas e evitar o deslocamento de
veículos com baixa ocupação reduz a quantidade de viagens, o consumo de
combustíveis fósseis e, consequentemente, as emissões de dióxido de carbono. Os
indicadores de redução de CO₂ e economia de combustível permitem acompanhar
tanto o impacto ambiental quanto a eficiência financeira da operação.

Entretanto, o alerta produzido pelo sistema deve apoiar, e não substituir, a
decisão humana. Situações urgentes ou serviços essenciais podem justificar uma
viagem abaixo do limite de 15 m³. Por isso, a governança deve manter o parâmetro
documentado, revisar periodicamente os indicadores e registrar as exceções,
conciliando eficiência econômica, responsabilidade ambiental e continuidade do
serviço.

## 💻 Seção de Engenharia e Governança de TI

Justifique a decisão de arquitetura técnica adotada pela célula nesta entrega. Como as regras de negócio de ADS e as estruturas de dados de SI foram construidas para garantir que a solução seja escalável e de fácil manutenção?

💬 RESPOSTA DA CÉLULA: Separamos o motor operacional da regra de governança.
`src/coleta_ads.py` cuida da leitura, validação e acumulação dos volumes, enquanto
`src/governanca_si.py` concentra os metadados e a classificação de eficiência
financeira. As funções possuem responsabilidades, entradas e retornos claros e
usam somente a biblioteca padrão do Python, reduzindo acoplamento e facilitando
a manutenção. O limite financeiro deriva dos metadados de capacidade e ocupação
mínima, evitando números sem explicação dentro da regra. Testes unitários cobrem
entradas válidas, sentinela, erros, limites e resultados de governança, e o
workflow executa esses testes e os fluxos integrados a cada alteração.

## 🛠️ Diário de Bordo da Bancada

* Maior travamento técnico superado pela dupla durante a semana: integrar o
  motor de coleta com as regras de governança e localizar a causa das falhas da
  automação. O histórico mostrou que todos os workflows falhavam porque o
  arquivo havia sido criado como `coelta_ads.py`, enquanto a automação procurava
  `coleta_ads.py`. Também foi necessário esclarecer que o percentual de 30%
  representa ocupação mínima, corrigir o nome do metadado e cobrir os casos de
  entrada inválida com testes.
* Como a intervenção ou a Issue aberta para o Embaixador ajudou a destravar a
  célula: o embaixador Caio Tarso preparou o repositório, enviou os convites de
  acesso e acompanhou a equipe, oferecendo suporte e orientação conforme as
  dúvidas surgiram. Esse apoio ajudou a organizar o fluxo de branches e commits
  e a integrar as contribuições no mesmo repositório.



## Lembrete de Fechamento: Garanta que todo o projeto esteja commitado na branch principal ('main') e responda ao Micro Simulado individual no AVA antes do prazo limite.
