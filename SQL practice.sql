use sql_store;
-- SELECT 
--  name,
--  unit_price,
--  unit_price * 1.1 AS new_price  #use of alias. By using this we can give ne new column name by applying mathamatical operatins on the previous column 
# eg  unit_price * 1.1 this is old column and methametical operation applied on that column and result as new_price by using alias AS
--  FROM products
-- SELECT * FROM ORDERS
-- WHERE ORDER_DATE >='2019-01-01' # Use of where clause with arthamatic operations like >,<,=< ,=>,=, !=.... the order of using clauses are select --> where --> groupby     
--  SELECT * FROM ORDER_ITEMS
--  where ORDER_ID = 6 AND  (quantity * unit_price > 30 )  #use of AND Oprator (both coditions should be considered)
--  
select  * from products 
where quantity_in_stock in (49, 38, 72) # use of IN operator ..by using this we can implement mutiple OR condtitions by using single IN 
                                         #eg: where quantity_in_stock = 49 OR 38 OR 72 	THIS IS REPLACED BY where quantity_in_stock in (49, 38, 72)
