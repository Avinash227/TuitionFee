from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Student:
    def __init__(self, student_id, name, total_fee):
        self.student_id = student_id
        self.name = name
        self.total_fee = total_fee
        self.paid = 0

    def pay_fee(self, amount):
        if self.paid + amount <= self.total_fee:
            self.paid += amount
            return True
        return False

    def status(self):
        return "Paid in Full" if self.paid == self.total_fee else "Pending"

# In-memory list of students (not persistent!)
students = [Student(i + 1, f"Student {i + 1}", 1000) for i in range(10)]

@app.route('/')
def index():
    return render_template("index.html", students=students)

@app.route('/pay/<int:student_id>', methods=['POST'])
def pay(student_id):
    amount = float(request.form['amount'])
    student = students[student_id - 1]
    success = student.pay_fee(amount)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
