# Write your MySQL query statement below
select today.id from Weather as today

 where Exists
    (select 1 from Weather as yesterday
    where yesterday.temperature < today.temperature
    and 
    datediff(today.recordDate,yesterday.recordDate) = 1);