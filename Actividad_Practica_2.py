import pytest
import Actividad

def test_gasto():       #Primera función para comprobar el mes que se gastó más
    mes = "Abril"
    assert mes == Actividad.mes_gasto()

def test_ahorro():
    resultado = 10304.0
    assert resultado == Actividad.mes_ahorro()

def test_media():
    resultado = -15374.333333333334
    assert resultado == Actividad.media_gasto()

def test_total():
    resultado = -184492.0
    assert resultado == Actividad.gasto_total()

def test_ingreso():
    resultado = 154677.0
    assert resultado == Actividad.ingreso_total()