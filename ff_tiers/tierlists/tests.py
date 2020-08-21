import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Plot

def create_plot(plot_name, days, scoring_format='STND', position='QB'):
    """
    Create a plot with the given plot_name and published the given days from now.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Plot.objects.create(plot_name=plot_name, creation_date=time)

class PlotModelTestCase(TestCase):
    def setUp(self):
        """ Creates two Plot objects to be used testing Plot Class. """ 
        create_plot(plot_name='test plot 1', days=0)
        create_plot(plot_name='test plot 2', days=0)

    def test_string_representation(self):
        """ String representation of Plots are the same as plot_name. """
        test_plot = Plot.objects.get(plot_name='test plot 1')
        self.assertEqual(str(test_plot), test_plot.plot_name)

    def test_was_created_today(self):
        """ Plots created today are correctly identified. """
        test_plot_1 = Plot.objects.get(plot_name='test plot 1')
        test_plot_2 = Plot.objects.get(plot_name='test plot 2')
        self.assertTrue(Plot.was_created_today(test_plot_1))
        self.assertTrue(Plot.was_created_today(test_plot_1))

    def test_verbose_name_plural(self):
        """ Verbose plural name of Plot should be plots. """
        self.assertEqual(str(Plot._meta.verbose_name_plural), "plots")

class PlotsIndexViewTestCase(TestCase):
    def test_no_plots(self):
        """ if no plots exist, an appropriate message is displayed. """
        response = self.client.get(reverse('tierlists:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No plots are available")
        self.assertQuerysetEqual(response.context['latest_plot_list'], [])

    def test_past_plot(self):
        """ Plots with a creation_date in the past are displayed. """
        create_plot(plot_name="test past plot", days=-30)
        response = self.client.get(reverse('tierlists:index'))
        self.assertQuerysetEqual(
            response.context['latest_plot_list'],
            ['<Plot: test past plot>']
        )

    def test_future_plot(self):
        """ Plots with a creation_date in the future won't be displayed. """
        create_plot(plot_name="test future plot", days=+30)
        response = self.client.get(reverse('tierlists:index'))
        self.assertContains(response, "No plots are available")
        self.assertQuerysetEqual(response.context['latest_plot_list'], [])

    def test_future_plot_and_past_plot(self):
        """
        Even if both past and future plots exist, only the past plots
        are displayed.
        """
        create_plot(plot_name="test past plot", days=-30)
        create_plot(plot_name="test future plot", days=+30)
        response = self.client.get(reverse('tierlists:index'))
        self.assertQuerysetEqual(
            response.context['latest_plot_list'],
            ['<Plot: test past plot>']
        )

    def test_two_past_questions(self):
        """
        The plots index page will display multiple plots.
        """
        create_plot(plot_name="test past plot 1", days=-30)
        create_plot(plot_name="test past plot 2", days=-5)
        response = self.client.get(reverse('tierlists:index', current_app='tierlists'))
        self.assertQuerysetEqual(
            response.context['latest_plot_list'],
            ['<Plot: test past plot 2>', '<Plot: test past plot 1>']
        )

