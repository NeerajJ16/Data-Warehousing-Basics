SELECT
    user_id,
    full_name,
    email,
    phone,
    website,
    company_name,
    company_bs,
    company_catchphrase,
    city,
    zipcode,
    latitude,
    longitude
FROM {{ ref('stg_users_clean') }}
