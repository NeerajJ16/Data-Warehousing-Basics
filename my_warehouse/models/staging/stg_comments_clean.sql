SELECT
    id           AS comment_id,
    postid       AS post_id,
    initcap(name)  AS commenter_name,
    lower(email)   AS commenter_email,
    body
FROM {{ source('public', 'stg_comments') }}
