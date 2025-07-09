SELECT
    c.comment_id,
    c.post_id,
    p.user_id,
    u.full_name,
    c.commenter_name,
    c.commenter_email,
    c.body
FROM {{ ref('stg_comments_clean') }} c
LEFT JOIN {{ ref('fact_posts') }} p ON c.post_id = p.post_id
LEFT JOIN {{ ref('dim_user') }} u ON p.user_id = u.user_id
