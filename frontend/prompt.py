#Emmanuel was here 15-05-24 21:37


database_schema = """### Database Schema
This query will run on a database whose schema is represented in this string:

CREATE TABLE FACTURASVENTA (
  NUMSERIE NVARCHAR PRIMARY KEY, -- Unique ID, identifies the series of the transaction.
  NUMFACTURA INTEGER, -- Consecutive number of the transaction, unique within the same series.
  CODCLIENTE INTEGER, -- Code that relates the invoice to a specific client in the CUSTOMER table.
  FECHA DATETIME, -- Date of the invoice.
  TOTALIMPUESTOS FLOAT, -- Total sum of the taxes applied to the transaction.
  TOTALNETO FLOAT -- Net value of the invoice before taxes.
); –- Stores the information for each sales invoice, including global transaction data.

CREATE TABLE ALBVENTACAB (
  NUMSERIE NVARCHAR, -- ID alphanumeric to connect with ALBVENTALIN
  NUMALBARAN INTEGER, -- ID integer to connect with ALBVENTALIN
  NUMSERIEFAC NVARCHAR, -- ID of sell, joins FACTURASVENTA
  NUMFAC INTEGER -- ID of transaction, joins FACTURASVENTA
); -- Acts as a header for the sales delivery notes, relating to the sales invoices.

CREATE TABLE ALBVENTALIN (
  NUMSERIE NVARCHAR, -- Alphanomeric ID the transaction, connect each packing slip line to its corresponding header in ALBVENTACAB.
  NUMALBARAN INTEGER, -- Number of transaction, connect each packing slip line to its corresponding header in ALBVENTACAB.
  DESCRIPCION NVARCHAR, -- Name of the product
  REFERENCIA NVARCHAR, -- ID of the product
  UNIDADESTOTAL FLOAT, -- Amount of product bought
  CODALMACEN NVARCHAR -- ID of the Warehouse of the transaction 
); -- Details each item sold on a packing slip, including reference, description, units, total per item, and tax.

CREATE TABLE CLIENTES (
  CODCLIENTE INTEGER PRIMARY KEY, -- Unique identification code for each customer.
  NOMBRECLIENTE NVARCHAR, -- Name of the client
  E_MAIL NVARCHAR, -- Email of the client
  DIRECCION1 NVARCHAR, -- Address of the client
  TELEFONO1 NVARCHAR -- Phone of the client
); –- Contains details of each customer, such as their ID, name, email, address, among others.

CREATE TABLE ALMACEN (
   CODALMACEN NVARCHAR, -- Unique identification code for each Warehaouse
   NOMBREALMACEN NVARCHAR -- Name of the Wharehouse
); -- Contains the data of the stores operated by the company, their location, telephone number, among others.

CREATE TABLE COSTESPORALMACEN ( 
CRECODALMACEN NVARCHAR, -- Unique identification code for each Warehaouse
CODARTICULO INT, -- Unique ID of each product
COSTESTOCK FLOAT --IS THE WEIGHTED AVERAGE COST OF THE PRODUCT
); -- Contains the cost of the products specified by each sales warehouse, i.e. the product may have different costs depending on the sales warehouse.

-- COSTERPORALMACEN.CODARTICULO can be joined with ARTICULOS.CODARTIOCULO
-- COSTESPORALMACEN.CODALMACEN can be joined with ALMACEN.CODALMACEN
-- FACTURASVENTA.NUMSERIE can be joined with ALBVENTACAB.NUMSERIEFAC
-- FACTURASVENTA.NUMFACTURA can be joined with ALBVENTACAB.NUMFAC
-- CLIENTES.CODCLIENTE can be joined with FACTURASVENTA.CODCLIENTE
-- ALBVENTACAB.NUMSERIE can be joined with ALBVENTALIN.NUMSERIE
-- ALBVENTACAB.NUMALBARAN can be joined with ALBVENTALIN.NUMALBARAN
-- ALMACEN.CODALMACEN can be joined with ALBVENTALIN.CODALMACEN
"""

SQL_CODER_PROMPT = """### Task
Generate a SQL query to answer [QUESTION]{question}[/QUESTION]

### Instructions
- If you cannot answer the question with the available database schema, return 'I do not know'
- Remember that the details of each sell is in the table ALBVENTALIN
-

{database_schema}

### Answer
Given the database schema, here is the SQL query that answers [QUESTION]{question}[/QUESTION]
[SQL]
"""

DECIDE_FUNCTION = """You have 2 options avaiable which you have to choose depending on the user's request, 
1. Just answer to the user (if the message contains simple phrases, general requests or is asking about info not avaiable in the schema)
2. Query a database and answer the users question (JUST if the users is requesting any information avaiable in the schema {})
If you choose option 1, then just answer like always, but if you choose option 2, then just say 'query'""".format(database_schema)

ANSWER_WITH_DATA = """Answer the user's message with the data you just fetched:
{data}. Also, that data was extracted with the following SQL query {query}, explain each table column based on the query so the user can know where did the data come from. Make sure the database schema keeps private, just say where the data came from without saying explicitly any database field, column, or SQL code. Say any number or constraint shown in the SQL query."""

MSSQL_TRANSLATOR = "You are an SQL expert, you will be given a MYSQL query, your job is to traduct from MySQL to MSSQL Server queries, just return the query"

THINK_STEPS = "Carefully analyze and outline the necessary steps to address the user's query without using bullet points or providing SQL code. Focus on identifying the precise data the user is interested in and any constraints mentioned, using only the relevant tables and fields from the provided schemas: {database_schema}. Ensure your response remains concise, within a single, succinct paragraph, and is written in English. Pay close attention to avoiding extended explanations and unnecessary examples. Do not give any conclusion, just analyze".format(database_schema=database_schema)