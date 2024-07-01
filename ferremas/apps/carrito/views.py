import json
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Carrito
from apps.producto.models import Producto
from apps.usuario.models import Usuario
# Create your views here.


class CarritoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        lista_herramientas = []
        valor_total = 0
        carritos = Carrito.objects.all()
        car = Carrito.objects.values()
                
        #print(carritos)
        if len(carritos)>0:
            print(carritos)
            for carrito in carritos: 
                nombre = carrito.producto.nomre
                cantidad = carrito.cantidad
                precio = carrito.producto.precio
                lista_herramientas.append({"id": carrito.id ,"nombre": nombre, "cantidad": cantidad, "precio": precio})  
                valor_total += precio *cantidad
            lista_herramientas.append({"total": valor_total,"id_carrito": car[0]['usuario_id']})
            datos={'message':"Success",'Articulos del Carrito ':lista_herramientas}
        else:
            datos={'message':"El Carrito esta vacio"}
        return JsonResponse(datos)
        
    '''
    def post(self, request):
            try:
                jd = json.loads(request.body)
                id_herramienta = jd.get('id')  # Asegúrate de obtener correctamente el id del producto desde el JSON
                cantidadjd = jd.get('cantidad')

                # Validación del producto existente
                herramienta = get_object_or_404(Producto, pk=id_herramienta)

                # Validación de stock
                if cantidadjd > herramienta.stock:
                    return JsonResponse({'error': 'La cantidad no puede sobrepasar el stock'}, status=status.HTTP_400_BAD_REQUEST)

                # Validación de carritos existentes y cantidad acumulada
                contador = Carrito.objects.filter(herramienta=herramienta).aggregate(total_cantidad=models.Sum('cantidad'))['total_cantidad'] or 0

                if contador + cantidadjd > herramienta.stock:
                    return JsonResponse({'error': 'Stock insuficiente'}, status=status.HTTP_400_BAD_REQUEST)

                # Creación del carrito
                user = Usuario.objects.get()  # Asegúrate de obtener el usuario adecuadamente
                Carrito.objects.create(usuario=user, herramienta=herramienta, cantidad=cantidadjd)
                
                return JsonResponse({'message': 'Success se ha agregado al carrito'}, status=status.HTTP_201_CREATED)
            
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Formato JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)
            
            except Producto.DoesNotExist:
                return JsonResponse({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    '''        
    def post(self, request):
        errors = []
        contador = 0
        jd = json.loads(request.body)
        id_herramienta = jd['id']
        cantidadjd = jd['cantidad']
        carritos = carrito.objects.values()
        herramientas = Producto.objects.filter(id=id_herramienta).values()

        print(herramientas)
        if len(herramientas)>0:
            print(carritos)
            if len(herramientas)>0:
                for carrito in carritos: 
                    if id_herramienta == carrito['herramienta_id']:
                        contador += carrito['cantidad']
            
            for herramienta in herramientas: 
                print(contador," mayor que ", herramienta['stock'])
                if contador >= herramienta['stock']:
                    errors.append({'codigo_producto': id_herramienta, 'error': 'Stock insuficiente', 'status': 'failed'})
                    return JsonResponse({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
                    
                else:
                    if cantidadjd > herramienta['stock']:
                        errors.append({'codigo_producto': id_herramienta, 'error': 'La cantidad no puede sobrepasar el stock', 'status': 'failed'})
                        return JsonResponse({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        user = Usuario.objects.get()
                        print(user.id)
                        herramienta = get_object_or_404(Producto, pk=id_herramienta)
                        carrito.objects.create(usuario_id=user.id,herramienta=herramienta,cantidad=cantidadjd)
                        datos={'message':"Success se a gregado al carrito"}
                        return JsonResponse(datos)
        else:
            errors.append({'codigo_producto': id_herramienta, 'error': 'No se a encontrado el producto', 'status': 'failed'})
            return JsonResponse({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

    

    def delete(self, request,id):
        print(id)
        carritos = list(Carrito.objects.filter(id=id).values())

        if len(carritos)>0:
            Carrito.objects.filter(id=id).delete()
            carritos_delete = list(Carrito.objects.filter(id=id).values())
            datos={'message':"Success",'El articulo se eliminado: ':carritos_delete}
        else:
            datos={'message':"El Articulo no se a encontrado"}
        return JsonResponse(datos)
    

class PagarCarritoAPIView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    
    def post(self, request):

        jd = json.loads(request.body)
        id_carrito = jd['id_carrito']
        confirmacion = jd['confirmacion']
        valor_total = 0
        CarroPay = carrito.objects.filter(usuario_id=id_carrito).all()
        lista_herramientas= []        
        #print(carritos)
        print(CarroPay)
        if confirmacion == "si":
            
            for carrito in CarroPay:
                nombre = carrito.herramienta.nombre
                cantidad = carrito.cantidad
                precio = carrito.herramienta.precio
                id_herramienta = carrito.herramienta.id
                id_car_herramienta = carrito.id
                valor_total += precio
                lista_herramientas.append({"nombre": nombre, "precio": precio,"id_herramienta":id_car_herramienta}) 
                herramientas = list(Producto.objects.filter(id=id_herramienta).values())
                stock = herramientas[0]['stock'] - cantidad
                herramienta = Producto.objects.get(id=id_herramienta)
                herramienta.stock = stock
                herramienta.save()
                carrito.objects.filter(id=id_car_herramienta).delete()




            lista_herramientas.append({"total": valor_total})
            
            datos={'message':"Success",'Detalle venta ':lista_herramientas,'Pago ':'terminado'}
        elif confirmacion == "no":
            datos={'message':"Success Se a vaciado el carrito"}
            for carrito in CarroPay:
                id_car_herramienta = carrito.id
                carrito.objects.filter(id=id_car_herramienta).delete()
        else:
            datos={'message':"Error debe confirmar la venta"}
        return JsonResponse(datos)  