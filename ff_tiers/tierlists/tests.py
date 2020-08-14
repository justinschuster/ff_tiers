from django.test import TestCase
from django.utils import timezone

from .models import Plot

class PlotTestCase(TestCase):
    def setUp(self):
        Plot.objects.create(
            plot_name="test_plot_1",
            creation_date=timezone.now(),
            scoring_format='HPPR',
            position='WR'
        )
        Plot.objects.create(
            plot_name="test_plot_2",
            creation_date=timezone.now(),
            scoring_format='FPPR',
            position='RB'
        )

    def test_was_created_today(self):
        """ Plots created today are correctly identified. """
        test_plot_1 = Plot.objects.get(plot_name='test_plot_1')
        test_plot_2 = Plot.objects.get(plot_name='test_plot_2')
        self.assertTrue(Plot.was_created_today(test_plot_1))
        self.assertTrue(Plot.was_created_today(test_plot_1))
