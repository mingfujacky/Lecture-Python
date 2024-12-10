-- 從 students 表格中回傳全部欄位的資料
SELECT * FROM students;

-- 從 students 表格中選取姓名、班級、成績三個欄位
SELECT 姓名, 班級, 成績 FROM students;

-- 顯示 1 年 2 班的資料
SELECT 姓名, 班級, 成績
FROM Students
WHERE 班級 = '1 年 2 班';

-- 顯示 1 年 2 班以外的資料
SELECT 姓名, 班級, 成績
FROM Students
WHERE 班級 <> '1 年 2 班';

-- 使用班級名稱來進行排序
SELECT 姓名, 班級, 成績
FROM Students
WHERE 班級 <> '1 年 2 班'
ORDER BY 班級;

-- 使用班級名稱和成績來進行排序
SELECT 姓名, 班級, 成績
FROM Students
WHERE 班級 <> '1 年 2 班'
ORDER BY 班級, 成績;

-- 使用班級名稱和成績來進行排序 (成績由高排到低)
SELECT 姓名, 班級, 成績 
FROM Students
WHERE 班級 <> '1 年 2 班'
ORDER BY 班級, 成績 DESC;

-- 查詢張小婷同學
SELECT 姓名, 班級, 成績 
FROM students 
WHERE 姓名 = '張小婷';

-- 查詢所有姓「張」的同學
SELECT 姓名, 班級, 成績 
FROM students 
WHERE 姓名 LIKE '張%';

-- 替詢所有姓「張」，名字只有兩個字的同學
SELECT 姓名, 班級, 成績 
FROM students 
WHERE 姓名 LIKE '張_';

-- 查詢成績大於且等於 80 分
SELECT 姓名, 班級, 成績 
FROM students 
WHERE 成績 >= 80;

-- 查詢成績介於 80 和 90 分
SELECT 姓名, 班級, 成績 
FROM students 
WHERE 成績 >= 80 AND 成績 <90;

-- 使用 BETWEEN 關鍵字來查詢分數區間
SELECT 姓名, 班級, 成績 
FROM students 
WHERE 成績 BETWEEN 80 AND 90;

-- 查詢出成績在 80 到 90 之間，且班級是「1 年 1 班」或「1 年 2 班」的學生
SELECT 姓名, 班級, 成績 
FROM students 
WHERE 成績 BETWEEN 80 AND 90 AND (班級 = '1 年 1 班' OR 班級 = '1 年 2 班');

-- 使用 IN 關鍵字來簡化多個 OR 條件的使用
SELECT 姓名, 班級, 成績 
FROM students 
WHERE 成績 BETWEEN 80 AND 90 AND (班級 IN ('1 年 1 班', '1 年 2 班'));

-- 計算成績欄的平均值、加總值、最大值、最小值、計數
SELECT AVG(成績), SUM(成績), MAX(成績), MIN(成績), COUNT(成績)
FROM students; 

-- 使用 AS 關鍵字設定別名
SELECT AVG(成績) AS 成績平均, MAX(成績) AS 最高分
FROM students; 

-- 四捨五入到小數第一位
SELECT ROUND(AVG(成績),1) AS 成績平均
FROM students; 

-- 四捨五入到整數位
SELECT ROUND(AVG(成績)) AS 成績平均
FROM students; 

-- 查詢各班的成績平均，並將分數由高至低排序
SELECT 班級, ROUND(AVG(成績)) AS 成績平均
From students
GROUP BY 班級
ORDER BY 成績平均 DESC;

-- 查詢成績平均大於且等於 80 的班級，並將分數由高至低排序
SELECT 班級, ROUND(AVG(成績)) AS 成績平均
From students
GROUP BY 班級
HAVING 成績平均 >= 80
ORDER BY 成績平均 DESC;

-- 計算整個表格的行數
SELECT COUNT(*)
FROM students;

-- 計算「社團」欄的行數 (會忽略空白值)
SELECT COUNT(社團)
FROM students;

-- 計算有多少種社團
SELECT COUNT(DISTINCT 社團)
FROM students;

-- 列出社團的編號名稱
SELECT DISTINCT 社團
FROM students;

-- 列出社團的編號名稱 (不包含空值)
SELECT DISTINCT 社團
FROM students
WHERE 社團 IS NOT NULL
ORDER BY 社團;

-- 建立名為 clubs 的表格，包含社團編號 (主鍵) 和社團名稱兩個欄位
CREATE TABLE clubs (
社團編號 INT PRIMARY KEY,
社團名稱 VARCHAR(15)
);

-- 刪除名為 clubs2 的表格
DROP TABLE clubs2;

-- 插入資料到社團表格
INSERT INTO clubs (社團編號, 社團名稱)
VALUES (101, '吉他社'), (102, '籃球社'), (103, '美術社'), (104, NULL);

SELECT * FROM clubs;

-- 更新資料
UPDATE clubs
SET 社團名稱 = '舞蹈社'
WHERE 社團編號 = 104;

-- 刪除資料
DELETE
FROM clubs
WHERE 社團編號 = 104;

-- 查詢學生報名的社團名稱 (LEFT JOIN)
Select students.姓名, students.社團, clubs.社團名稱
From Students
LEFT JOIN clubs 
On students.社團 = clubs.社團編號
WHERE 班級 = '1 年 1 班'

-- 查詢學生報名的社團名稱 (INNER JOIN)
Select students.姓名, students.社團, clubs.社團名稱
From Students
INNER JOIN clubs 
On students.社團 = clubs.社團編號
WHERE 班級 = '1 年 1 班'

