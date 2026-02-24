import os
import openai
from dotenv import load_dotenv
import json
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("API_KEY")

script_dir = Path(__file__).parent
with open(script_dir / "prompt_template.md", encoding="utf-8") as f:
    PROMPT_TEMPLATE = f.read()

def extract_entities(text, prompt_template, model="gpt-5-mini"):
    """
    Extract structured entities from invoice text.
    
    Args:
        text: Raw text from invoices
        prompt_template: Custom prompt template
        model: Model to use
    
    Returns:
        JSON string with extracted entities
    """
    prompt = prompt_template.replace('{text}', text)
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": """
             Eres una herramienta extractora de datos de facturas mediante la técnica Named Entity Recognition (NER).
             Solo procesas textos de facturas y devuelves los datos en formato JSON.
             """},
            {"role": "user", "content": prompt}
        ],
        temperature=1
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    data_folder = script_dir / "invoices"
    output_folder = script_dir / "output"
    output_folder.mkdir(exist_ok=True)
    
    txt_files = list(data_folder.rglob("*.txt"))
    
    for txt_file in txt_files:
        with open(txt_file, encoding="utf-8") as f:
            texto = f.read()
        
        resultado = extract_entities(texto, PROMPT_TEMPLATE).strip()
        output_file = output_folder / f"{txt_file.stem}.json"
        
        data = json.loads(resultado)
        data["ID_FACTURA"] = txt_file.stem
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
