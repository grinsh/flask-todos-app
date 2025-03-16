import unittest
from main import app, db, Task


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # יוצרת אפליקציית Flask לבדיקות
        self.app = app.test_client()
        self.app.testing = True

        # יוצרת מסד נתונים זמני לבדיקות
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # מוחקת את מסד הנתונים לאחר כל בדיקה
        with app.app_context():
            db.drop_all()

    def test_index(self):
        # בודקת את הדף הראשי
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
          # בודקת הוספת משימה חדשה
          response = self.app.post('/', data=dict(title='Test Task'))
          self.assertEqual(response.status_code, 302)  # בדוק הפניה מחדש
          with app.app_context():
              task = Task.query.filter_by(title='Test Task').first()
              self.assertIsNotNone(task)

    def test_delete_task(self):
        # בודקת מחיקת משימה
        with app.app_context():
            task = Task(title='Task to Delete')
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.app.get(f'/delete/{task_id}')
        self.assertEqual(response.status_code, 302)  # בדוק הפניה מחדש
        with app.app_context():
            task = Task.query.get(task_id)
            self.assertIsNone(task)



if __name__ == '__main__':
    unittest.main()
