
import re
from tkinter import N
from django.http import HttpResponse
from django.shortcuts import render

def get_catalog_context():
	products = [
		{
			'image': 'deps/images/goods/kitchen table 2.jpg',
			'title': 'Чайный столик и два стула',
			'description': 'Набор из стола и двух стульев в минималистическом стиле.',
			'id': '02265',
			'price': 100,
			'discount': 10,
		},
		{
			'title': 'Комплект постельного белья \'Звёздное небо\'',
			'description': 'Постельное белье из 100% хлопка с нанесением уникального рисунка звёздного неба.',
			'id': '33512',
			'price': 80,
			'discount': None
		},
		{
			'image': 'deps/images/goods/flower.jpg',
			'title': 'Кофейный стол \'Винтаж\'',
			'description': 'Круглый кофейный стол с винтажной отделкой из массива дерева.',
			'id': '45578',
			'price': 120,
			'discount': 20
		},
		{
			'image': 'deps/images/goods/plants.jpg',
			'title': 'Кресло-качалка \'Уютное\'',
			'description': 'Мягкое кресло-качалка с подушкой для уютного отдыха и чтения.',
			'id': '78963',
			'price': 150,
			'discount': 25
		},
		{
			'image': 'deps/images/goods/sofa.jpg',
			'title': 'Набор кухонных ножей \'Профессионал\'',
			'description': 'Комплект из 5 профессиональных ножей с удобными ручками из нержавеющей стали.',
			'id': '12458',
			'price': 70,
			'discount': 10
		},
		{
			'image': 'deps/images/goods/strange table.jpg',
			'title': 'Коврик для йоги \'Эко-френдли\'',
			'description': 'Экологически чистый коврик для йоги из натурального каучука.',
			'id': '96325',
			'price': 30,
			'discount': None
		}
	]
	for product in products:
		discount = product.get('discount')
		if discount:
			product['discounted_price'] = product['price'] - (product['price'] * discount / 100)

	context = {
		'title': 'Catalog',
		'description': 'This page is about bla bla, and other blabla blog',
		'products': products
	}
	return context

def catalog(request):
	return render(request, 'goods/catalog.html', get_catalog_context())

def product(request):
	return render(request, 'goods/product.html')