SELECT
    id          AS todo_id,
    userid      AS user_id,
    initcap(title) AS todo_title,
    completed::boolean           AS is_completed
FROM {{ source('public', 'stg_todos') }}
