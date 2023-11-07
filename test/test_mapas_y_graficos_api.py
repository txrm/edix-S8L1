# coding: utf-8

"""
    AEMET OpenData

    AEMET OpenData es una API REST desarrollado por AEMET que permite la difusión y la reutilización de la información meteorológica y climatológica de la Agencia, en el sentido indicado en la Ley 18/2015, de 9 de julio, por la que se modifica la Ley 37/2007, de 16 de noviembre, sobre reutilización de la información del sector público. (IMPORTANTE: Para poder realizar peticiones, es necesario introducir en API Key haciendo clic en el círculo rojo de recurso REST).  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.mapas_y_graficos_api import MapasYGraficosApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMapasYGraficosApi(unittest.TestCase):
    """MapasYGraficosApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.mapas_y_graficos_api.MapasYGraficosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mapas_de_anlisis__ltima_pasada_(self):
        """Test case for mapas_de_anlisis__ltima_pasada_

        Mapas de análisis. Última pasada.  # noqa: E501
        """
        pass

    def test_mapas_significativos__tiempo_actual_(self):
        """Test case for mapas_significativos__tiempo_actual_

        Mapas significativos. Tiempo actual.  # noqa: E501
        """
        pass

    def test_mapas_significativos__tiempo_actual_1(self):
        """Test case for mapas_significativos__tiempo_actual_1

        Mapas significativos. Tiempo actual.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()