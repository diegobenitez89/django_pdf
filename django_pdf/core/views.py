from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse
from django_pdf .utileria import render_pdf


class PDFPrueba(View):


    def get(selft, request, *args, **kwargs):
        datos = {
            "nombre": "Pepito",
            "apellido" :"Pistolero",
            "certificacion" :"El mas malo",
            }
       
        pdf = render_pdf("core/pdf.html", {"datos":datos})

        return HttpResponse(pdf, content_type="aplicacion/pdf")


