# Databricks notebook source
# DBTITLE 1,Comando 1
print("Olá mundo!!!")

# COMMAND ----------

# DBTITLE 1,Soma
print(f"Isso é uma soma de 2+2={2+2}")

# COMMAND ----------

# DBTITLE 1,Display Dados
df = spark.table("silver.olist.pedido")
df.display()

# COMMAND ----------


