"""Provides responses for corresponding URLs."""

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Provide main page for cooking app."""
    return HttpResponse("Landing page")


def recipe_book(request):
    """Provide recipe database interface."""
    return HttpResponse("Livre des Recettes")


def recipe(request, recipe_id):
    """Provide individual recipe interface."""
    return HttpResponse(f"This is the recipe for {recipe_id}")


def shopping_list(request):
    """Provide shopping list interface."""
    return HttpResponse("Liste d'épicerie; TODO")


def meal_planner(request):
    """Provide meal planner interface."""
    return HttpResponse("Plan de repas; TODO")


def food_storage(request):
    """Provide food storage interface."""
    return HttpResponse("Garde-manger aujourd'hui; TODO")
