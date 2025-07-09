SELECT
    p.post_id,
    p.user_id,
    u.full_name,
    p.title,
    p.body
FROM {{ ref('stg_posts_clean') }} p
LEFT JOIN {{ ref('dim_user') }} u ON p.user_id = u.user_id
