import mysql.connector
from settings.environments import ENV

conn = mysql.connector.connect(
  host=ENV["DB_HOST"],
  user=ENV["DB_USER"],
  password=ENV["DB_PASSWORD"],
  database=ENV["DB_NAME"]
)

mysql_cursor = conn.cursor()
