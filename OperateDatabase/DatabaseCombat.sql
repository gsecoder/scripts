-- -*- encoding: utf-8 -*-
-- @File    :   DatabaseCombat.sql
-- @Time    :   2019/11/4 20:32
-- @Author  :   Crisimple
-- @Github :    https://crisimple.github.io/
-- @Contact :   Crisimple@foxmail.com
-- @License :   (C)Copyright 2017-2019, Micro-Circle
-- @Desc    :   None

SELECT * FROM PythonDatabases.news;

UPDATE PythonDatabases.news
SET title = 'news19', content = 'news19Content', types = 'baijia19'
WHERE id = 19;

UPDATE PythonDatabases.news
SET title = CASE
    WHEN id = 1 THEN 'news1'
    WHEN id = 2 THEN 'news2'
    WHEN id = 3 THEN 'news3'
    END
WHERE id in (1, 2, 3)
