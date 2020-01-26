import psycopg2
#connect to the db
def conn():
    # con = psycopg2.connect(
    #     host = "",
    #     database = "company",
    #     user = "postgres",
    #     password = 36016778
    # )
    con = psycopg2.connect(database="projV0", user="postgres", password="12", host="127.0.0.1", port="5432")

    #cursor
    cur = con.cursor();
    #sql = "select first_name from sabtenam where first_name = %s"
    #res1=cur.execute(sql,('sahar'))
   # print(res1)
    sql = "select first_name from sabtenam where first_name = %s and password = %s"
    res1=cur.execute(sql,(name_in,password_in))
    #res2=cur.execute("select * from sabtenam where first_name = %s" values())
    rows=cur.fetchall()
    for r in rows:
      print(f"first_name : {r[1]}")
   # cur.execute("insert into emp (empname,salary) values('sam',-45)")
    #exwcute query
    #cur.execute("select id,first_name from sabtenam")
    #rows = cur.fetchall()
    #for r in rows:
     #   print(f"id : {r[0]} , name : {r[1]}")

    #commit the transcaction
    con.commit()

    #close the cursor
    cur.close()

    #close the connection
    con.close()
if __name__ == "__main__":
        import sys
        conn()