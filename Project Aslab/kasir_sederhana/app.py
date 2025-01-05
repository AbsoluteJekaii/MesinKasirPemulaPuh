from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'key' 

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='kasir_sederhana',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            flash("Login berhasil", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Username atau password salah", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Anda telah logout", "info")
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if session['role'] == 'admin':
        return redirect(url_for('admin_dashboard'))
    elif session['role'] == 'kasir':
        return redirect(url_for('kasir_dashboard'))

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Anda tidak memiliki akses ke halaman ini", "danger")
        return redirect(url_for('login'))
    
    return render_template('admin_dashboard.html', username=session['username'])

@app.route('/kasir_dashboard')
def kasir_dashboard():
    if 'user_id' not in session or session['role'] != 'kasir':
        flash("Anda tidak memiliki akses ke halaman ini", "danger")
        return redirect(url_for('login'))
    
    return render_template('kasir_dashboard.html', username=session['username'])

@app.route('/products')
def products():
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
        connection.commit()
        flash("Produk berhasil ditambahkan", "success")
        return redirect(url_for('products'))
    
    return render_template('add_product.html')

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']
        cursor.execute("UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s", (name, price, stock, id))
        connection.commit()
        flash("Produk berhasil diubah", "success")
        return redirect(url_for('products'))

    return render_template('edit_product.html', product=product)

@app.route('/delete_product/<int:id>')
def delete_product(id):
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (id,))
    connection.commit()
    flash("Produk berhasil dihapus", "success")
    return redirect(url_for('products'))

@app.route('/transaction_history', methods=['GET', 'POST'])
def transaction_history():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cursor = connection.cursor()
    role = session.get('role')
    
    if role == 'admin':
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()
        if request.method == 'POST':
            transaction_id = request.form['transaction_id']
            cursor.execute("DELETE FROM transactions WHERE id=%s", (transaction_id,))
            connection.commit()
            flash("Transaction berhasil dihapus", "success")
        return render_template('transaction_admin.html', transactions=transactions)
    
    elif role == 'kasir':
        user_id = session['user_id']
        cursor.execute("SELECT * FROM transactions WHERE user_id=%s", (user_id,))
        transactions = cursor.fetchall()
        return render_template('transaction_kasir.html', transactions=transactions)
    
    return render_template('transaction.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if 'user_id' not in session or session['role'] != 'kasir':
        return redirect(url_for('login'))

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    if request.method == 'POST':
        if 'add_to_cart' in request.form:
            product_id = request.form['product_id']
            quantity = int(request.form['quantity'])
            cursor.execute("SELECT name, price, stock FROM products WHERE id=%s", (product_id,))
            product = cursor.fetchone()

            if product and product['stock'] >= quantity:
                total_price = product['price'] * quantity
                item = {
                    'product_id': product_id,
                    'product_name': product['name'],
                    'quantity': quantity,
                    'total_price': total_price
                }

                if 'cart' not in session:
                    session['cart'] = []

                session['cart'].append(item)
                flash("Produk berhasil ditambahkan ke keranjang.", "success")
                return redirect(url_for('payment')) 

        elif 'next' in request.form:
            if 'cart' in session and session['cart']:
                return redirect(url_for('total_payment'))
            else:
                flash("Silakan masukkan barang ke keranjang terlebih dahulu", "info")

    return render_template('payment.html', products=products)

@app.route('/total_payment', methods=['GET', 'POST'])
def total_payment():
    if 'user_id' not in session or session['role'] != 'kasir':
        return redirect(url_for('login'))

    if 'cart' not in session or not session['cart']:
        flash("Keranjang kosong. Silakan kembali dan tambahkan produk.", "info")
        return redirect(url_for('payment'))  

    cart = session['cart']
    grand_total = sum(item['total_price'] for item in cart)

    if request.method == 'POST':
        cursor = connection.cursor()
        user_id = session['user_id']
        for item in cart:
            cursor.execute("INSERT INTO transactions (user_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)",
                           (user_id, item['product_id'], item['quantity'], item['total_price']))
            cursor.execute("UPDATE products SET stock = stock - %s WHERE id=%s", (item['quantity'], item['product_id']))
        
        connection.commit()
        session.pop('cart', None) 
        flash("Transaksi selesai.", "success")
        return redirect(url_for('dashboard'))

    return render_template('total_payment.html', cart=cart, grand_total=grand_total)

if __name__ == '__main__':
    app.run(debug=True)
