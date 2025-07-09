{{
  config({    
    "materialized": "table",
    "full_refresh": true
  })
}}

WITH qa_test_Automationchetan_seed_job_Snowflake AS (

  SELECT * 
  
  FROM {{ ref('qa_test_Automationchetan_seed_job_Snowflake')}}

)

SELECT *

FROM qa_test_Automationchetan_seed_job_Snowflake
