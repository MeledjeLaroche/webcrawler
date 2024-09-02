import unittest
from src.ai_code_agent import AICodeAgent

class TestAICodeAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AICodeAgent()

    def test_generate_code(self):
        task = "Créer une fonction qui calcule la factorielle d'un nombre"
        language = "python"
        code = self.agent.generate_code(task, language)
        self.assertIsInstance(code, str)
        self.assertIn("def factorial", code)

    def test_optimize_code(self):
        original_code = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        """
        language = "python"
        optimized_code = self.agent.optimize_code(original_code, language)
        self.assertIsInstance(optimized_code, str)
        self.assertNotEqual(original_code, optimized_code)

if __name__ == '__main__':
    unittest.main()