from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.name

# Create some initial student records
with app.app_context():
    db.create_all()

    # Check if students table is empty
    if Student.query.count() == 0:
        # Add sample students
        student1 = Student(name='John Doe', age=18)
        student2 = Student(name='Jane Smith', age=17)
        student3 = Student(name='David Johnson', age=19)

        # Add students to the session
        db.session.add(student1)
        db.session.add(student2)
        db.session.add(student3)

        # Commit the changes
        db.session.commit()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/students')
def students():
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/request', methods=['GET', 'POST'])
def request_tutoring():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        student = Student(name=name, age=age)
        db.session.add(student)
        db.session.commit()

        return render_template('request_success.html', name=name)

    return render_template('request.html')

if __name__ == '__main__':
    app.run(debug=True)
