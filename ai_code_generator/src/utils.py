import subprocess
from typing import List

def compile_and_run(code: str, language: str) -> str:
    if language == "python":
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True)
    elif language == "c":
        with open("temp.c", "w") as f:
            f.write(code)
        subprocess.run(["gcc", "-o", "temp", "temp.c"])
        result = subprocess.run(["./temp"], capture_output=True, text=True)
    elif language == "c++":
        with open("temp.cpp", "w") as f:
            f.write(code)
        subprocess.run(["g++", "-o", "temp", "temp.cpp"])
        result = subprocess.run(["./temp"], capture_output=True, text=True)
    elif language == "java":
        with open("Temp.java", "w") as f:
            f.write(code)
        subprocess.run(["javac", "Temp.java"])
        result = subprocess.run(["java", "Temp"], capture_output=True, text=True)
    else:
        return "Langage non supporté"

    return result.stdout

def get_supported_languages() -> List[str]:
    return ["python", "c", "c++", "java"]