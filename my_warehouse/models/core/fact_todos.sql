SELECT
    t.todo_id,
    t.user_id,
    u.full_name,
    t.todo_title,
    t.is_completed
FROM {{ ref('stg_todos_clean') }} t
LEFT JOIN {{ ref('dim_user') }} u ON t.user_id = u.user_id
