from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tutors.db"
db = SQLAlchemy(app)


class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    profession = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.name


with app.app_context():
    db.create_all()

    if Tutor.query.count() == 0:
        tutor1 = Tutor(name="John Doe", age=30, profession="Math")
        tutor2 = Tutor(name="Jane Smith", age=27, profession="Chemistry")
        tutor3 = Tutor(name="David Johnson", age=32, profession="Biology")

        db.session.add(tutor1)
        db.session.add(tutor2)
        db.session.add(tutor3)

        db.session.commit()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/tutors")
def tutors():
    tutors = Tutor.query.all()
    return render_template("tutors.html", tutors=tutors)


@app.route("/request", methods=["GET", "POST"])
def request_tutoring():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        profession = request.form.get("profession")

        tutor = Tutor(name=name, age=age, profession=profession)
        db.session.add(tutor)
        db.session.commit()

        return render_template("request_success.html", name=name)

    return render_template("request.html")


if __name__ == "__main__":
    app.run(debug=True)
