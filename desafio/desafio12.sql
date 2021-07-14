select 
	n.Name as country_name,
	c.Name as currency_name,
	round(avg(d.AverageRate),2 )as currency_rate,
	round(f.TaxRate ,2)as average_tax_rate
	from Person.CountryRegion as n
	inner join Sales.CountryRegionCurrency b
		on n.CountryRegionCode = b.CountryRegionCode
	inner join sales.Currency as c 
		on c.CurrencyCode = b.CurrencyCode
	inner join Sales.CurrencyRate as d
		on d.ToCurrencyCode = c.CurrencyCode
	inner join Person.StateProvince as e
		on n.CountryRegionCode = e.CountryRegionCode
	inner join Sales.SalesTaxRate as f
		on e.StateProvinceID = f.StateProvinceID
	group by n.Name,c.Name, f.TaxRate
	order by c.Name;