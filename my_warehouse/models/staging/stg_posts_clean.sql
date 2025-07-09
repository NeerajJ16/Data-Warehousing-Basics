SELECT
    id            AS post_id,
    "userid"      AS user_id,          -- note: Pandas lower-cased ⇒ userid
    initcap(title) AS title,
    body
FROM {{ source('public', 'stg_posts') }}
