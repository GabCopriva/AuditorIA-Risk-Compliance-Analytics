🔍 AuditorIA: Risk & Compliance Analytics
O AuditorIA é uma solução de inteligência de dados aplicada a Finanças e Compliance, desenvolvida para automatizar a detecção de riscos financeiros em transações corporativas. Este projeto demonstra a intersecção entre Engenharia de Dados (Python) e Business Intelligence (Power BI) para transformar dados brutos em inteligência para tomada de decisão.

🚀 Arquitetura da Solução
O fluxo de dados foi desenhado para garantir reprodutibilidade e escalabilidade:

Ingestão e Saneamento (Python): Tratamento de bases brutas, normalização de formatos (datas, valores, chaves) e eliminação de ruídos.

Motor de Auditoria (Python): Aplicação automatizada de regras de negócio (Compliance Engine) para identificar desvios e anomalias.

Visibilidade Estratégica (Power BI): Modelagem de dados em Star Schema com medidas avançadas em DAX para monitoramento em tempo real.

🛠️ Tecnologias e Ferramentas
Linguagem: Python 3.x

Bibliotecas: Pandas (Manipulação e Engenharia de dados)

BI: Power BI Desktop (Modelagem, UX/UI e Dashboards)

Lógica Analítica: DAX (Data Analysis Expressions)

Output: MS Excel (Exportação de evidências de auditoria)

📊 Principais Análises & Regras de Compliance
O motor do projeto processa o histórico de movimentações focando nos seguintes pilares:

Identificação de Duplicidades: Cruzamento de múltiplos atributos (fornecedor, valor, data) para estorno ou bloqueio preventivo.

Análise de Valores Críticos: Filtro inteligente para movimentações acima de R$ 50.000,00.

Gestão de Risco: Cálculo de exposição financeira em valores nominais.

Índice de Conformidade: KPI dinâmico via DAX que reflete a saúde dos processos.

Análise de Top Offenders: Ranking de fornecedores com maior incidência de inconformidades.

🎯 Resultados Obtidos
O projeto entregou indicadores de alto impacto operacional:
Indicador, Valor
Transações Auditadas, 5.000
Duplicidades Detectadas, 171
Transações de Alto Risco, 217
Índice de Conformidade,"92, 54%"

📁 Estrutura do Repositório
├── data/           # Arquivos de exportação e evidências
├── dashboards/     # Arquivo .pbix do Power BI
├── scripts/        # Código-fonte Python (Limpeza e Motor de Regras)
└── README.md       # Documentação do projeto

📬 Contato
Gabriel Copriva de Souza Santos * LinkedIn
contatogabrielcopriva@gmail.com

Projeto desenvolvido para demonstração de competências em Data Analytics aplicado à Auditoria.
