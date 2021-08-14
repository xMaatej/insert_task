from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIRequestFactory

from rest.models import Category, Offer
from rest.views import CategoryList, OffersList


class ViewSetTests(TestCase):
    def test_categories(self):
        request = APIRequestFactory().get("")
        category_detail = CategoryList.as_view(actions={'get': 'retrieve'})
        category = Category.objects.create(name="Cloths")
        response = category_detail(request, pk=category.pk)
        self.assertEqual(response.status_code, 200)
    #
    # def test_categories(self):
    #     request = APIRequestFactory().get("")
    #     offer_detail = OffersList.as_view(actions={'get': 'retrieve'})
    #     offer = Offer.objects.create(title="Cloths")
    #     response = offer_detail(request, pk=offer.pk)
    #     self.assertEqual(response.status_code, 200)

