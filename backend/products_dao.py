from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.product_name, products.uom, products.price_per_unit, uom.uomcol "
            " FROM grocery_store.products inner join grocery_store.uom on products.uom=uom.uom_id;")

    cursor.execute(query)
    response = []
    for(product_id,name, uom_id, price_per_unit, uomcol) in cursor:
        response.append(
            {
            "product_id": product_id,
            "name": name,
            "uom_id": uom_id, 
            "price_per_unit": price_per_unit,
            "measure: ": uomcol
            }
        )


    connection.close()

    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into grocery_store.products (product_name, uom, price_per_unit) " 
             "values (%s, %s, %s); ")
    data = (product['product_name'], product['uom'], product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM grocery_store.products where product_id="+ str(product_id))
    cursor.execute(query)
    connection.commit()



if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 11))


