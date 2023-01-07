import psycopg2
import psycopg2.extras

# Database config TODO:
hostname = ''
database = ''
username = ''
pwd = ''
port_id = 5432
conn = None

try:
    with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('DROP TABLE IF EXISTS purchase_history')
            cur.execute('DROP TABLE IF EXISTS users')

            # Create purchase history table
            purchase_hist_script = ''' CREATE TABLE IF NOT EXISTS purchase_history(
                                    id              serial PRIMARY KEY,
                                    product_name    varchar(255) NOT NULL,
                                    link            varchar(255) NOT NULL,
                                    price           varchar(255) NOT NULL) '''
            cur.execute(purchase_hist_script)

            # Create users table
            users_script = ''' CREATE TABLE IF NOT EXISTS users(
                            id          serial PRIMARY KEY,
                            username    varchar(255) NOT NULL,
                            pwd_hash    varchar(255) NOT NULL)'''
            cur.execute(users_script)
            '''
            # Example CRUD operations
            insert_script = 'INSERT INTO purchase_history (product_name, link, price) VALUES (%s, %s, %s)'
            insert_values = [('MED1', 'https://www.google.com/', '10'), ('MED2', 'https://www.google.com/', '20'),
                             ('MED3', 'https://www.google.com/', '30')]
            for record in insert_values:
                cur.execute(insert_script, record)

            update_script = 'UPDATE purchase_history SET price = 100 WHERE id = 1'
            cur.execute(update_script)

            delete_script = 'DELETE FROM purchase_history WHERE product_name = %s'
            delete_record = ('MED2',)
            cur.execute(delete_script, delete_record)

            cur.execute('SELECT * FROM purchase_history ORDER BY product_name')
            for record in cur.fetchall():
                print(record['product_name'], record['price'])
            '''

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()