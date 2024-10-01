# Databricks notebook source
# Databricks notebook source
print("Hello World!")


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello world from SQL!"

# COMMAND ----------

# Title 1
## Title 2
### Title 3


text with a **bold** and *italicized* in it.

Ordered list
1. first
1. second
1. third


Unordered list
* coffee
* tea
* milk


Images:
![Associate-badge](https://www.databricks.com/wp-content/uploads/2022/04/associate-badge-eng.svg)


| user_id | user_name |
|---------|-----------|
|    1    |    Adam   |
|    2    |    Sarah  |
|    3    |    John   |


inks (or Embedded HTML): <a href="https://docs.databricks.com/notebooks/notebooks-manage.html" target="_blank"> Managing Notebooks documentation</a>


# COMMAND ----------

# MAGIC %run ../Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()
dbutils.fs.help()

files = dbutils.fs.ls('/databricks-datasets')
print(files)
display(files) #display works way better than print - gives table
