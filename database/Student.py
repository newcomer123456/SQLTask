class Student:
    def __init__(self, db):
        self.db = db

    def add_student(self, name, age, major):
        self.db.execute_query('''
        INSERT INTO students (name, age, major) VALUES (?, ?, ?)
        ''', (name, age, major))

    def get_student(self, student_id):
        return self.db.fetch_one('''
        SELECT * FROM students WHERE id=?
        ''', (student_id,))
    
    def get_students(self):
        return self.db.fetch_all('''
        SELECT * FROM students
        ''')

    def update_student(self, student_id, name=None, age=None, major=None):
        if name:
            self.db.execute_query('''
            UPDATE students SET name=? WHERE id=?
            ''', (name, student_id))
        if age:
            self.db.execute_query('''
            UPDATE students SET age=? WHERE id=?
            ''', (age, student_id))
        if major:
            self.db.execute_query('''
            UPDATE students SET major=? WHERE id=?
            ''', (major, student_id))

    def delete_student(self, student_id):
        self.db.execute_query('''
        DELETE FROM students WHERE id=?
        ''', (student_id,))