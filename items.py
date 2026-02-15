import db

def add_item(title, author, review, user_id):
    sql = "INSERT INTO items (title, author, review, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, author, review, user_id])

def get_items():
    sql = "SELECT id, title, author, review, user_id FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = "SELECT id, title, author, review, user_id FROM items WHERE id = ?"
    result = db.query(sql, [item_id])
    return result[0] if result else None

def get_items_by_user(user_id):
    sql = "SELECT id, title, author, review FROM items WHERE user_id = ? ORDER BY id DESC"
    return db.query(sql, [user_id])

def update_item(item_id, title, author, review):
    sql = "UPDATE items SET title = ?, author = ?, review = ? WHERE id = ?"
    db.execute(sql, [title, author, review, item_id])

def delete_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def search_items(query):
    sql = "SELECT id, title, author, review FROM items WHERE title LIKE ? OR author LIKE ?"
    like_query = f"%{query}%"
    return db.query(sql, [like_query, like_query])


def get_categories():
    sql = "SELECT id, name FROM categories ORDER BY name"
    return db.query(sql)


def add_item_categories(item_id, category_ids):
    db.execute("DELETE FROM item_categories WHERE item_id = ?", [item_id])
    for cat_id in category_ids:
        db.execute("INSERT INTO item_categories (item_id, category_id) VALUES (?, ?)", [item_id, cat_id])


def add_comment(item_id, user_id, text):
    sql = "INSERT INTO comments (item_id, user_id, text) VALUES (?, ?, ?)"
    db.execute(sql, [item_id, user_id, text])


def get_comments(item_id):
    sql = """SELECT comments.id, comments.text, comments.user_id, users.username, comments.created_at
             FROM comments JOIN users ON comments.user_id = users.id
             WHERE item_id = ? ORDER BY comments.created_at"""
    return db.query(sql, [item_id])
