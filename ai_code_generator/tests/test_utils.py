import unittest
from src.utils import compile_and_run, get_supported_languages

class TestUtils(unittest.TestCase):
    def test_compile_and_run_python(self):
        code = "print('Hello, World!')"
        result = compile_and_run(code, "python")
        self.assertEqual(result.strip(), "Hello, World!")

    def test_get_supported_languages(self):
        languages = get_supported_languages()
        self.assertIsInstance(languages, list)
        self.assertIn("python", languages)
        self.assertIn("c", languages)
        self.assertIn("c++", languages)
        self.assertIn("java", languages)

if __name__ == '__main__':
    unittest.main()