import aiopg


async def close(cursor, connection):
    cursor.close()
    connection.close()


async def set_state(user_id, state):
    connection = await aiopg.connect(user="table_example",
                                     password="table_example",
                                     host="localhost",
                                     port="5432",
                                     database="table_example")
    cursor = await connection.cursor()

    await cursor.execute(f"update table_example set state = '{state}' where id_user = '{user_id}'")
    await close(cursor, connection)


async def get_state(user_id):
    connection = await aiopg.connect(user="table_example",
                                     password="table_example",
                                     host="localhost",
                                     port="5432",
                                     database="table_example")
    cursor = await connection.cursor()

    await cursor.execute(f"select state from table_example where id_user = '{user_id}'")
    result = await cursor.fetchall()
    await close(cursor, connection)
    return result[0][0]
