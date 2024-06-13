class StudentsCourses:
    def __init__(self, db):
        self.db = db

    def add_students_courses(self, course_id, student_id):
        self.db.execute_query('''
        INSERT INTO studentscourses (course_id, student_id) VALUES (?, ?)
        ''', (course_id, student_id))

    def get_students_courses(self, id):
        return self.db.fetch_one('''
        SELECT * FROM studentscourses WHERE id=?
        ''', (id,))
    
    def get_courses(self):
        return self.db.fetch_all('''
        SELECT * FROM studentscourses
        ''')

    def update_course(self, id, course_id=None, student_id=None):
        if course_id:
            self.db.execute_query('''
            UPDATE studentscourses SET course_id=? WHERE id=?
            ''', (course_id, id))
        if student_id:
            self.db.execute_query('''
            UPDATE studentscourses SET student_id=? WHERE id=?
            ''', (student_id, id))

    def delete_course(self, id):
        self.db.execute_query('''
        DELETE FROM studentscourses WHERE id=?
        ''', (id,))
    
    def get_students_by_course_id(self, course_id):
        return self.db.fetch_all('''
        SELECT * FROM studentscourses WHERE course_id=?
        ''', (course_id,))