SELECT
    id                          AS user_id,
    initcap(trim(name))         AS full_name,
    lower(trim(email))          AS email,
    username,
    nullif(trim(phone), '')     AS phone,
    lower(website)              AS website,

    -- straight from nested JSON ↓ (Pandas flattened them)
    initcap("company_name")           AS company_name,
    initcap("company_bs")             AS company_bs,
    initcap(company_catchPhrase)    AS company_catchphrase,

    initcap("address_city")     AS city,
    "address_zipcode"           AS zipcode,
    cast("address_geo_lat" AS float)  AS latitude,
    cast("address_geo_lng" AS float)  AS longitude

FROM {{ source('public', 'stg_users') }}
WHERE email IS NOT NULL