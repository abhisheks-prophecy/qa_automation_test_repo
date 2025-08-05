WITH customers AS (

  SELECT * 
  
  FROM {{ ref('customers')}}

)

SELECT *

FROM customers
