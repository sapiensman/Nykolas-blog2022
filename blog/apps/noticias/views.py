from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Noticia

@login_required
def Listar_Noticias(request):
	contexto = {}
	n = Noticia.objects.all() #RETORNA UNA LISTA DE OBJETOS
	contexto['noticias'] = n

	#x = Noticia.objects.get(pk = 1)
	#print(f"1 SOLA: {x}")
	
	#f = Noticia.objects.filter(categoria_noticia = 1)
	#print(f"SOLO DEPORTES: {f}")

	return render(request, 'noticias/listar.html', contexto)

@login_required
def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
	contexto['noticia'] = n

	return render(request, 'noticias/detalle.html',contexto)

#{'nombre':'nicolas', 'apellido':'Tortosa', 'edad':33}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE

'''