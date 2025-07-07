# Car-Sales-Data-Analysis-Using-SQL

## Project Overview
This project analyzes car sales data through various SQL queries to understand different aspects of car sales patterns. It uses a dataset representing car sales, including details such as sales price, state, make, model, condition, odometer readings, and other attributes. The goal is to explore how these factors influence the overall sales and pricing trends, providing insights for decision-making and optimization strategies in the automotive industry.

## Objectives
The main objectives of this analysis are:

* To determine the number of cars sold in each state and identify regional trends in car sales.
* To understand which car makes and models are most popular and their sales volume.
* To analyze the variations in sales prices across states and evaluate their average differences.
* To examine how car sales prices vary by year and month, providing insights into seasonal trends.
* To identify the most successful car makes and models in different body types.
* To investigate the impact of car conditions and odometer values on sales prices and volume.

## Business Problems and Solutions

### 1. Count of Cars Sold in Each State
```sql
SELECT 
    state, 
    COUNT(*) AS num_count 
FROM 
    car_sales 
GROUP BY 
    state;
```
### 2. Which kind of cars are more popular and how maney sales are being made for each make and model?
``` sql
select
make,
model,
count(*) as num_count
from car_sales_v
group by make, model
order by 3 desc;
```
### 3. Are they difference in sales price for each state and what is average difference for sales price for each state?
``` sql
select
state,
avg(sellingprice) as avg_selling_price
from car_sales_v
group by state
order by 2 asc;
```
### 4. What is the average sales price for cars sold for each month and year?
``` sql
select
sale_year,
sale_month,
avg(sellingprice) as avg_selling_price
from car_sales_v
group by 1, 2
order by 1, 2;
```

### 5. Which month of year have the highest sales?
``` sql
select 
sale_month,
count(*) as num_sales
from car_sales_v
group by 1
order by 1 asc;
```
### 6. What are the top 5 of most selling car within a body types, we will like to see make, model, body and number of sales?
``` sql
select
make, 
model,
body,
num_sales,
body_rank
from (
	select
    make,
    model,
    body,
    count(*) as num_sales,
    rank() over(partition by body order by count(*) desc) as body_rank
    from car_sales_v
    group by 1,2,3
)s
where body_rank <= 5;
```
### 7. What are sales higher than average for the model and how much high it is?
``` sql
select
make,
model,
vin,
sale_year,
sale_month,
sale_day,
sellingprice,
avg_model,
sellingprice/avg_model as price_ratio
from (
	select
	make,
	model,
	vin,
	sale_year,
	sale_month,
	sale_day,
	sellingprice,
	avg(sellingprice) over(partition by make, model) as avg_model
	from car_sales_v
)s
where sellingprice > avg_model
order by 9 desc;
```
### 8. How has the condition impacted on the price and how many are sold?
``` sql
select
case
	when conditions between 0 and 9 then '0 to 9'
    when conditions between 10 and 19 then '10 to 19'
    when conditions between 20 and 29 then '20 to 29'
    when conditions between 30 and 39 then '30 to 39'
    when conditions between 40 and 49 then '40 to 49'
end as car_condition_bucket,
count(*) as num_sales,
avg(sellingprice) as avg_selling_price
from car_sales_v
group by 1
order by 1;
```

### 10. How has the odometer values impacted the selling price?
``` sql
select
case
	when odometer < 100000 then '0 - 99,999'
	when odometer < 200000 then '100,000 - 199,999'
	when odometer < 300000 then '200,000 - 299,999'
	when odometer < 400000 then '300,000 - 399,999'
	when odometer < 500000 then '400,000 - 499,999'
	when odometer < 600000 then '500,000 - 599,999'
	when odometer < 700000 then '600,000 - 699,999'
	when odometer < 800000 then '700,000 - 799,999'
	when odometer < 900000 then '800,000 - 899,999'
	when odometer < 1000000 then '900,000 - 999,999'
end as odometer_bucket,
count(*) as num_sales,
avg(sellingprice) as avg_selling_price
from car_sales_v
group by 1
order by 1;
```

### 11. What is the max and min selling price for eash car make and sales count?
``` sql
select
make,
count(distinct model) as num_models,
count(*) as num_sales,
min(sellingprice) as min_price,
max(sellingprice) as max_price,
avg(sellingprice) as avg_selling_price
from car_sales_v
group by 1
order by 6 desc;
```

### 12. Are there any car sold more then one and what are the details?
``` sql
select
*
from (
	select
    *,
count(*) over(partition by vin) as vin_sales
from car_sales_v
)s 
where vin_sales > 1;
```

### 13. Top 10 seller 
``` sql
select
seller,
sum(sellingprice) as total_sales,
avg(sellingprice) as avg_selling_price
from car_sales_v
group by 1
order by 3 desc
limit 10;
```

### 13. How have the car make and interior impacted on the price?
``` sql
select
make,
interior,
count(*) as num_sales,
avg(sellingprice) as avg_selling_price
from car_sales_v
where interior != '' and interior != '-'
group by 1, 2
order by 4 desc;
```
## Findings and Conclusion
#### The findings from the analysis include:
State-wise Sales: There are notable differences in car sales across different states, with certain regions showing higher sales volumes. This trend could be influenced by local demand, demographics, and economic conditions.
Popular Cars: The analysis revealed the top-selling car makes and models. Popularity varies by region and car type, indicating that consumer preferences differ across different markets.
Sales Price Trends: States exhibit variations in the average selling price of cars. Understanding these price differences can help manufacturers and sellers adjust their strategies accordingly.
Seasonality: Sales are influenced by seasonal factors, with certain months showing higher sales than others. This could be valuable for marketing campaigns and inventory management.
Body Type Preferences: Certain car body types outperform others in terms of sales, suggesting that some categories, like SUVs or sedans, are preferred more frequently.
Impact of Condition and Odometer: Cars with better conditions and lower odometer readings generally command higher prices, which aligns with consumer preferences for newer or well-maintained vehicles. 

#### Conclusion: 
The analysis provides valuable insights into consumer behavior and sales patterns within the automotive industry. By understanding these trends, businesses can tailor their strategies to optimize sales, adjust pricing models, and identify target markets more effectively. The findings also offer a foundation for further analysis and decision-making in areas like inventory management, marketing, and customer targeting.
