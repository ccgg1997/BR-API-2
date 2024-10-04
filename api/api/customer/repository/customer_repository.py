from api.customer.models import Customer


class CustomerRepository:

    @staticmethod
    def create_customer(nombre, duenio, telefono, direccion, barrio, activo):
        customer = Customer(
            nombre=nombre,
            duenio=duenio,
            telefono=telefono,
            direccion=direccion,
            barrio=barrio,
            activo=activo,
        )
        customer.save()
        return customer

    @staticmethod
    def get_all():
        return Customer.objects.all()

    @staticmethod
    def get_by_id(id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            return None

    @staticmethod
    def update_customer(id, nombre, duenio, telefono, direccion, barrio, activo):
        customer = CustomerRepository.get_by_id(id)
        if customer is not None:
            customer.nombre = nombre
            customer.duenio = duenio
            customer.telefono = telefono
            customer.direccion = direccion
            customer.barrio = barrio
            customer.activo = activo
            customer.save()
        return customer

    @staticmethod
    def delete_customer(id):
        customer = CustomerRepository.get_by_id(id)
        if customer is not None:
            customer["activo"] = False
            customer.save()
        return customer
