-- 코드를 입력하세요
SELECT 
    USER_ID, 
    PRODUCT_ID
FROM 
    ONLINE_SALE 
group by
    user_id, product_id
having
    count(distinct sales_date) > 1
ORDER BY user_id, product_id DESC;

-- 동일 회원의 동일한 상품 재구매한 데이터 구하기
/*어떻게 찾나? 
user_id and product_id 
*/