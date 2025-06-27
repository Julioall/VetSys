import json
import os
from datetime import datetime

def guardar_banco(lista, arquivo):
    def serializar(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj.__dict__

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4, default=serializar)

def carregar_banco(arquivo, entidade):
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)

            # Verifica se é Agendamento e converte data
            if entidade.__name__ == "Agendamento":
                for a in dados:
                    a["data_hora"] = datetime.fromisoformat(a["data_hora"])
            return [entidade(**item) for item in dados]
    return []
