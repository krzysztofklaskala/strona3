from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'mysecretkey'  # Klucz do sesji, wymagany do działania flash()

# Przechowywanie użytkowników
users = []

# Strona główna
@app.route('/')
def home():
    return render_template('index.html', users=users)

# Formularz dodawania użytkownika
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if not username or not email:
            flash('Wszystkie pola muszą być wypełnione!', 'danger')
            return redirect(url_for('add_user'))
        
        # Dodanie użytkownika do listy
        user = {
            'username': username,
            'email': email,
            'joined': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        users.append(user)
        flash('Użytkownik został dodany!', 'success')
        return redirect(url_for('home'))
    
    return render_template('add_user.html')

# Strona o nas
@app.route('/about')
def about():
    return render_template('about.html')

# Strona kontaktowa
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Strona błędu
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
