import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from hello import mensaje

def test_mensaje():
    assert mensaje() == "Hola desde el laboratorio CI/CD"