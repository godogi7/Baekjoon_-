-- 코드를 입력하세요
SELECT
    extract(year from o.sales_date) as year,
    extract(month from o.sales_date) as month,
    u.gender,
    count(distinct o.user_id) as users
from online_sale as o
left join user_info u on o.user_id = u.user_id
where u.gender is not null
group by 1,2,3
order by 1,2,3;
