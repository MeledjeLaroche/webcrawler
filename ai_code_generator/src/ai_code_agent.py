import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class AICodeAgent:
    def __init__(self):
        self.model_name = "bigcode/starcoder"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_code(self, prompt: str, language: str) -> str:
        full_prompt = f"Tu es un expert en développement {language} spécialisé dans la création de modèles d'IA et le développement rapide d'applications. Génère du code optimisé pour les performances, supportant le multiprocessing, le multithreading et CUDA si applicable.\n\nTâche: {prompt}\n\nCode:"
        inputs = self.tokenizer.encode(full_prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(
                inputs,
                max_length=800,
                num_return_sequences=1,
                temperature=0.7,
                top_p=0.95,
                do_sample=True
            )
        generated_code = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_code.split("Code:")[1].strip()

    def optimize_code(self, code: str, language: str) -> str:
        optimization_prompt = f"Optimise ce code {language} pour les performances, en utilisant le multiprocessing, le multithreading et CUDA si applicable :\n\n{code}"
        return self.generate_code(optimization_prompt, language)

    def process_request(self, task: str, language: str, optimize: bool = False) -> str:
        generated_code = self.generate_code(task, language)
        if optimize:
            generated_code = self.optimize_code(generated_code, language)
        return generated_code