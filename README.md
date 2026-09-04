
# EU & Portugal Renewable Energy Tracker
Projeto de análise de dados sobre o progresso de Portugal e da União Europeia face à meta de energia renovável para 2030, usando dados abertos do Eurostat.

## Objetivo
Este projeto responde a uma pergunta central: que países da UE estão mais próximos (ou mais longe) de cumprir a meta europeia de energia renovável para 2030 de 42,5% (ou da meta mais ambiciosa de 45%), e como se posiciona Portugal nessa comparação?

Foi construído como projeto pessoal de aprendizagem, cobrindo todo o ciclo de um pipeline de dados: extração via API, transformação e limpeza com pandas, análise exploratória e estatística, e visualização interativa num dashboard público.

# Fontes de Dados
Todos os dados usados são públicos e provenientes do Eurostat:

**sdg_07_40** — Share of renewable energy in gross final energy consumption by sector
**env_air_gge** — Greenhouse gas emissions by source sector
**demo_pjan** — Population on 1 January by age and sex

Os dados brutos estão disponíveis em data/raw/, e o dataset processado final em data/raw/processed/eu_renewable_emissions.csv.

## Principais Conclusões
- Portugal está a 6,2 pontos percentuais da meta europeia de 42,5% (2024), posicionando-se como um dos países líderes da UE em adoção de renováveis, atrás apenas de Suécia, Finlândia, Dinamarca, Letónia, Áustria e Estónia.
- O setor elétrico português já ultrapassou a meta europeia desde 2013; é o setor de transportes que mais atrasa a média nacional.
- Portugal esteve consistentemente acima da média europeia em energia renovável desde 2005.
- Segundo uma regressão linear validada estatisticamente, ao ritmo histórico Portugal deverá atingir a meta europeia (42,5%) em 2031, e a sua própria meta nacional mais ambiciosa (51%) em 2041.
- Em emissões de gases com efeito de estufa, Portugal está sistematicamente abaixo da média europeia nos três principais gases analisados (CO2, CH4, N2O).
- Não foi encontrada correlação clara entre percentagem de energia renovável e emissões per capita; outros fatores, como estrutura industrial e consumo total, parecem pesar mais.

## Como Correr o Projeto Localmente
 
1. Clonar o repositório:
```
git clone <url-do-repositorio>
```
 
2. Instalar as dependências:
```
pip install pandas eurostat matplotlib statsmodels scikit-learn
```
 
3. Correr o script de extração de dados:
```
python etl/extract.py
```
 
4. Explorar os notebooks, pela ordem:
```
notebooks/01_explore_raw_data.ipynb
notebooks/02_exploratory_analysis.ipynb
notebooks/03_forecast_and_gases.ipynb
```
 
## Licença
 
Este projeto está licenciado sob os termos definidos no ficheiro `LICENSE`.