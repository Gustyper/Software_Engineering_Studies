# test_adapters.py

import unittest
import pandas as pd
from unittest.mock import patch # Ferramenta para simular (mockar) dependências

# Importe as classes que você quer testar
from adapters import CSVAdapter, APIAdapter, ObjectAdapter
from dataIterator import Iterator
from main import Objeto # Importando a classe Objeto para usar nos testes

class TestAdapters(unittest.TestCase):

    def test_api_adapter_transforma_corretamente(self):
        """
        Testa se o APIAdapter converte o dicionário em uma lista de valores.
        Este é o teste mais simples, pois não tem dependências externas.
        """
        # Arrange (Organizar)
        adapter = APIAdapter()
        expected_output = ["um", "dois", "tres", "quatro", "cinco"]

        # Act (Agir)
        actual_output = adapter.get_data()

        # Assert (Verificar)
        self.assertEqual(actual_output, expected_output)

    #----------------------------------------------------------------------

    def test_object_adapter_transforma_lista_encadeada(self):
        """
        Testa se o ObjectAdapter percorre a lista encadeada e extrai os valores.
        """
        # Arrange
        # Recriamos a mesma estrutura de objetos do seu main.py
        obj3 = Objeto("coco")
        obj2 = Objeto(2, obj3)
        obj1 = Objeto(1, obj2)
        
        adapter = ObjectAdapter(obj1)
        expected_output = [1, 2, "coco"]

        # Act
        actual_output = adapter.get_data()

        # Assert
        self.assertEqual(actual_output, expected_output)

    #----------------------------------------------------------------------

    @patch('adapters.pd.read_csv') # Onde mockar: no módulo 'adapters' onde 'pd.read_csv' é chamado
    def test_csv_adapter_com_arquivo_mockado(self, mock_read_csv):
        """
        Testa o CSVAdapter sem ler um arquivo de verdade.
        Nós "mockamos" a função pd.read_csv para retornar um DataFrame falso.
        """
        # Arrange
        # Crie um DataFrame falso que o read_csv "retornará"
        dados_falsos = pd.DataFrame({
            'Coluna1': [10, 20],
            'Coluna2': ['A', 'B']
        })
        mock_read_csv.return_value = dados_falsos # Configure o mock
        
        # O caminho do arquivo agora é irrelevante, pois a leitura não acontecerá
        adapter = CSVAdapter("caminho/falso.csv")
        expected_output = [[10, 'A'], [20, 'B']]

        # Act
        actual_output = adapter.get_data()

        # Assert
        self.assertEqual(actual_output, expected_output)
        mock_read_csv.assert_called_once_with("caminho/falso.csv") # Verifica se a função foi chamada

#----------------------------------------------------------------------

class TestIterator(unittest.TestCase):
    
    def test_iterator_percorre_lista_corretamente(self):
        """
        Testa se a classe Iterator retorna os itens na ordem correta.
        """
        # Arrange
        dados = [100, 200, 300]
        meu_iterador = Iterator(dados)

        # Act & Assert
        self.assertEqual(next(meu_iterador), 100)
        self.assertEqual(next(meu_iterador), 200)
        self.assertEqual(next(meu_iterador), 300)
        # esse next é uma função built-in do python que pega o próximo valor de um iterador

        # Assert - Verifica se StopIteration é levantado no final
        with self.assertRaises(StopIteration):
            next(meu_iterador)

# Para rodar os testes se executar este arquivo diretamente
if __name__ == '__main__':
    unittest.main()