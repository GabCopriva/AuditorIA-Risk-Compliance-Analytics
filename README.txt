# 🔍 AuditorIA: Risk & Compliance Analytics

O **AuditorIA** é uma solução de inteligência de dados aplicada a Finanças e Compliance, desenvolvida para automatizar a detecção de riscos financeiros em transações corporativas. 

O projeto combina **Python (Pandas)** para a engenharia de dados, limpeza e aplicação do motor de regras de conformidade, com o **Power BI (DAX)** para a criação de um ecossistema visual focado no monitoramento e mitigação de riscos operacionais.

---

## 🚀 Arquitetura da Solução

1. **Ingestão e Saneamento (Python):** Tratamento da base bruta de transações e padronização das colunas críticas (datas, valores e chaves únicas).
2. **Motor de Auditoria (Python):** Aplicação automatizada das regras de compliance para identificar desvios, gerando bases específicas de anomalias.
3. **Visibilidade Estratégica (Power BI):** Modelagem de dados com medidas avançadas em DAX e design focado em tomada de decisão (*Data-Driven*).

---

## 🛠️ Tecnologias e Ferramentas

* **Python 3.x**
* **Pandas** (Engenharia de dados e automação)
* **Microsoft Excel** (Armazenamento e exportação dos relatórios)
* **Power BI Desktop** (Modelagem, dashboards e UX/UI)
* **DAX - Data Analysis Expressions** (Indicadores analíticos dinâmicos)

---

## 📊 Principais Análises & Regras de Compliance

O motor do projeto analisa o histórico de movimentações focando nas seguintes frentes de auditoria:

* **Transações Duplicadas:** Cruzamento e identificação de registros idênticos (mesmo fornecedor, valor e data) que sinalizam falhas de processo ou pagamentos em duplicidade.
* **Valores Críticos:** Alerta automático para movimentações isoladas com valores acima de R$ 50.000,00.
* **Exposição Financeira:** Cálculo do volume total de capital em risco associado a transações não conformes.
* **Taxa de Risco:** Percentual de transações que apresentam alguma inconformidade em relação à base total.
* **Índice de Conformidade (DAX):** Indicador dinâmico que reflete a saúde financeira e a maturidade dos processos da empresa.
* **Ranking de Fornecedores:** Mapeamento e classificação dos prestadores de serviço com maior recorrência de inconformidades (*Top Offenders*).

---

## 🎯 Resultados Obtidos

Após o processamento e análise da base, o **AuditorIA** gerou os seguintes insights quantitativos:

* **5.000** transações corporativas auditadas e integradas.
* **171** duplicidades reais detectadas e isoladas para estorno/bloqueio.
* **217** transações classificadas como **Alto Risco** (necessitando de auditoria manual imediata).
* **92,54% de Índice de Conformidade**, fornecendo à diretoria uma visão clara da eficiência operacional da empresa.

---

## 📁 Estrutura do Repositório

* `scripts/`: Código-fonte em Python para tratamento e filtragem dos dados.
* `data/`: Relatórios gerados em Excel prontos para consumo.
* `dashboards/`: Arquivo `.pbix` do Power BI com o ecossistema visual de risco.

---

## 📬 Contato

Desenvolvido por Gabriel Copriva de Souza Santos -  https://www.linkedin.com/in/gabrielcopriva/ - contatogabrielcopriva@gmail.com
