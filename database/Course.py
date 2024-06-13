class Course:
    def __init__(self, db):
        self.db = db

    def add_course(self, course_name, instructor):
        self.db.execute_query('''
        INSERT INTO courses (course_name, instructor) VALUES (?, ?)
        ''', (course_name, instructor))

    def get_course(self, course_id):
        return self.db.fetch_one('''
        SELECT * FROM courses WHERE id=?
        ''', (course_id,))
    
    def get_courses(self):
        return self.db.fetch_all('''
        SELECT * FROM courses
        ''')

    def update_course(self, course_id, course_name=None, instructor=None):
        if course_name:
            self.db.execute_query('''
            UPDATE courses SET course_name=? WHERE id=?
            ''', (course_name, course_id))
        if instructor:
            self.db.execute_query('''
            UPDATE courses SET instructor=? WHERE id=?
            ''', (instructor, course_id))

    def delete_course(self, course_id):
        self.db.execute_query('''
        DELETE FROM courses WHERE id=?
        ''', (course_id,))