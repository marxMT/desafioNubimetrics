select 
sp.CountryRegionCode as country_region_code,
avg(all st.TaxRate) as average_taxRate
from [Person].[StateProvince] as sp 
inner join [Sales].[SalesTaxRate] as st
ON sp.StateProvinceID = st.StateProvinceID
group by sp.CountryRegionCode;