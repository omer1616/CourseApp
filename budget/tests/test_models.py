from django.test import TestCase
from budget.models import Project, Category, Expense


class TestModels(TestCase):

    def setUp(self):
        self.project1 = Project.objects.create(
            name='Project 1',
            budget=1000
        )

        self.category1 = Category.objects.create(
            name='category1',
            project=self.project1
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEqual(self.project1.slug, 'project-1')

    def test_project_budget_left(self):


        expense1 = Expense.objects.create(
            project=self.project1,
            title="expense1",
            amount=100,
            category=self.category1
        )

        expense2 = Expense.objects.create(
            project=self.project1,
            title='expense2',
            amount=200,
            category=self.category1

        )

        self.assertEqual(self.project1.budget_left, 700)

    def test_project_total_transactions(self):

        expense3 = Expense.objects.create(
            project=self.project1,
            title='expense2',
            amount=200,
            category=self.category1

        )

        self.assertEqual(self.project1.total_transactions, 1)
