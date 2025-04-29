from behave import given, when, then

@given('ingreso el numero uno "{num1}" ')
def step_ingreso_el_numero_uno(context, num1):
    context.num1 = int(num1)

@given('ingreso el numero dos "{num2}" ')
def step_ingreso_el_numero_dos(context, num2):
    context.num2 = int(num2)

@when('presiono el boton suma ')
def step_presiono_el_boton_suma(context):
    context.resultado = context.num1+context.num2   

@then('el resultado deberia ser "{result}" ')
def step_el_resultado_deberia_ser(context, result):
    assert context.resultado == int(result)