SELECT 
  du.full_name,
  du.company_name,
  COUNT(DISTINCT fp.post_id) AS post_count,
  COUNT(DISTINCT fc.comment_id) AS comment_count,
  COUNT(DISTINCT ft.todo_id) AS total_todos,
  COUNT(CASE WHEN ft.is_completed THEN 1 END) AS completed_todos
FROM 
  dim_user du
LEFT JOIN 
  fact_posts fp ON fp.user_id = du.user_id
LEFT JOIN 
  fact_comments fc ON fc.user_id = du.user_id
LEFT JOIN 
  fact_todos ft ON ft.user_id = du.user_id
GROUP BY 
  du.full_name, du.company_name
ORDER BY 
  post_count DESC