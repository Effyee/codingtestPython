SELECT h.car_id,
       CASE
         WHEN EXISTS (
           SELECT 1
           FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h2
           WHERE h2.car_id = h.car_id
             AND h2.start_date <= DATE '2022-10-16'
             AND DATE '2022-10-16' <= h2.end_date
         ) THEN '대여중'
         ELSE '대여 가능'
       END AS availability
FROM (
  SELECT DISTINCT car_id
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) h
ORDER BY h.car_id DESC;
