from django.test import TestCase
from trainer.forms import ContactForm


# test for the contact form
class ContactTestCase(TestCase):
    def test_contactForm(self):
        form_data = {'from_email': 'kenya1@company.com', 'subject': 'test subject', 'message': 'sending a test message'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())


# tests for the functions in the views.py file
class ViewsTestCase(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_workoutProgram(self):
        response = self.client.get('/workout_program/')
        self.assertEqual(response.status_code, 200)

    def test_mealPlan(self):
        response = self.client.get('/meal_plan/')
        self.assertEqual(response.status_code, 200)

    # TODO unit test for successView not working
    # def test_successView(self):
    #     response = self.client.get('/contact_success/')
    #     self.assertEqual(response.status_code, 200)

    # TODO unit test for emailView not working
    # def test_emailView(self):
    #     response = self.client.get('/contact/')
    #     self.assertEqual(response.status_code, 200)
