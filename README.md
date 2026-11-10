# Business Risk Stratification and Decision Support System

## Project Overview

The Business Risk Stratification and Decision Support System is a web-based application developed to assess business risk exposure and support decision-making in Zimbabwe's Fast-Moving Consumer Goods (FMCG) sector.

The project uses a hybrid GARCH and machine learning approach to analyse market volatility, identify demand patterns and support production and pricing decisions. It considers financial, operational and market factors that influence business performance in an unstable economic environment.

The system provides analytical outputs and decision-support recommendations to help businesses make informed decisions about production quantities, inventory levels, pricing and profitability.

## Project Objectives

- Classify business risk exposure by assessing financial, operational and market risks.
- Forecast market volatility by analysing pricing fluctuations and daily returns.
- Support production planning by estimating production quantities, costs and potential profit.
- Examine the relationship between business performance and broader economic conditions.
- Recommend adaptive product pricing based on cost fluctuations and consumer demand.

## Key Features

- **Business Risk Classification:** Assesses business risk exposure using financial, operational and market indicators.
- **Market Volatility Forecasting:** Applies GARCH modelling to analyse historical price movements and forecast volatility.
- **Demand Forecasting:** Uses machine learning models to identify demand patterns and support purchasing and production decisions.
- **Production Optimisation:** Supports production planning by evaluating costs, capacity, demand and inventory levels.
- **Adaptive Pricing:** Analyses production costs, market trends and demand to support product pricing decisions.
- **Profitability Analysis:** Provides analytical outputs for evaluating revenue, costs, profit and break-even points.

## Technologies and Tools

- **Programming Language:** Python
- **Web Framework:** Flask
- **Database:** SQLite
- **Database Management:** SQLAlchemy, Flask-Migrate
- **Data Analysis:** Pandas, NumPy
- **Data Visualisation:** Matplotlib, Seaborn
- **Machine Learning:** XGBoost, Random Forest, Prophet
- **Statistical Modelling:** GARCH
- **Authentication:** Flask-Login

## Models and Analytical Techniques

The project combines statistical modelling and machine learning techniques:

- **GARCH:** Analyses historical market volatility and forecasts changes in volatility over time.
- **XGBoost:** Supports demand-related prediction and analysis.
- **Random Forest:** Supports business risk classification.
- **Prophet:** Supports time-series forecasting.

The models contribute to different parts of the system's analytical and decision-support processes.

## Data and Variables

The project uses a dataset covering 25 FMCG product entries across different product categories, including food, beverages, household and personal-care products.

The analysis considers variables such as:

- Product demand rate.
- Operational and production costs.
- Retail and estimated wholesale prices.
- Retail markup.
- Stock-out rate.
- Consumer purchasing frequency.
- Inflation and Consumer Price Index (CPI) changes.
- GDP growth.
- Currency-use and dollarisation indicators.

These variables are used to examine product-level performance, market conditions and potential business risks.

## Data Sources

The project draws on publicly available economic information and market-related sources, including:

- [Reserve Bank of Zimbabwe (RBZ) – USD Consumer Price Index](https://www.rbz.co.zw/index.php/research/markets/inflation/29-inflation/1477-consumer-price-index-usd-august-2025)
- [World Bank – Zimbabwe GDP Growth](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=ZW)
- [Control Risks – Zimbabwe's ZiG and Dollarisation](https://www.controlrisks.com/our-thinking/insights/can-zimbabwe-zig-zag-away-from-the-dollar)
- [OK Zimbabwe Online Catalogue](https://okonline.co.zw/catalogue/)
- [National Foods – Product Information](https://www.shumba.africa/shumba-brand/national-foods-ltd/)

**Data note:** Where actual wholesale prices were not publicly available, wholesale price values were estimated using assumed retail-to-wholesale markup relationships. These estimates are modelling assumptions and should not be interpreted as verified company wholesale prices.

## Methodology

The project follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modelling
5. Evaluation
6. Deployment

This approach provides a structured process for understanding the business problem, preparing data, developing analytical models and integrating the results into a decision-support application.

## System Outputs

The application provides analytical outputs to support business decision-making, including:

- Business risk classifications.
- Historical and forecast market volatility.
- Product demand forecasts.
- Production quantity recommendations.
- Revenue, cost and profitability analysis.
- Break-even analysis.
- Adaptive pricing insights.

The outputs are intended to support decisions relating to inventory management, production planning and pricing in changing market conditions.

## Project Significance

The project demonstrates how statistical modelling, machine learning and web-based application development can be combined to address business decision-making challenges in Zimbabwe's FMCG sector.

By integrating economic indicators, product-level data and predictive modelling, the system provides a structured approach to understanding business risks and evaluating possible responses to market uncertainty.

## Author

**Faith Jenesa**

Data Science and Informatics Graduate | First Class Honours
