Language- MS SQL Server
SET.NOCOUNT ON; ---

select sku,product_name from product a
where id not in (select product_id from invoice_item)

go
