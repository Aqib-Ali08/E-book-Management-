from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ebooks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    year = db.Column(db.Integer)

# Home page
@app.route('/')
def index():
    ebooks = Ebook.query.all()
    return render_template('index.html', ebooks=ebooks)

# Add e-book
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_ebook = Ebook(
            title=request.form['title'],
            author=request.form['author'],
            genre=request.form['genre'],
            year=request.form['year']
        )
        db.session.add(new_ebook)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

# Update e-book
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    ebook = Ebook.query.get(id)
    if request.method == 'POST':
        ebook.title = request.form['title']
        ebook.author = request.form['author']
        ebook.genre = request.form['genre']
        ebook.year = request.form['year']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', ebook=ebook)

# Delete e-book
@app.route('/delete/<int:id>')
def delete(id):
    ebook = Ebook.query.get(id)
    db.session.delete(ebook)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context(): 
        db.create_all()     
    app.run(debug=True)      
