SELECT SUM(amount)
FROM billing
WHERE MONTH(charged_datetime)=3 AND YEAR(charged_datetime)=2012;