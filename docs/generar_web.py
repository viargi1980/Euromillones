from pathlib import Path
from datetime import datetime

import pandas as pd
import joblib

WINDOW = 777

BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================
# CARGAR MODELOS
# ===============================

modelos_numeros = joblib.load(
    BASE_DIR / "artifacts" / "modelos_numeros.pkl"
)

modelos_estrellas = joblib.load(
    BASE_DIR / "artifacts" / "modelos_estrellas.pkl"
)

# ===============================
# CARGAR DATOS
# ===============================

df = pd.read_csv(
    BASE_DIR / "euromillions_limpio.csv"
)

rows = []

for _, row in df.iterrows():

    registro = {}

    for n in range(1, 51):
        registro[f"num_{n}"] = 0

    for e in range(1, 13):
        registro[f"star_{e}"] = 0

    for n in [
        row["n1"],
        row["n2"],
        row["n3"],
        row["n4"],
        row["n5"]
    ]:
        registro[f"num_{int(n)}"] = 1

    for e in [
        row["e1"],
        row["e2"]
    ]:
        registro[f"star_{int(e)}"] = 1

    rows.append(registro)

bin_df = pd.DataFrame(rows)

ultima_ventana = bin_df.iloc[-WINDOW:]

fila = {}

for n in range(1, 51):
    fila[f"freq_num_{n}"] = ultima_ventana[f"num_{n}"].sum()

for e in range(1, 13):
    fila[f"freq_star_{e}"] = ultima_ventana[f"star_{e}"].sum()

X_pred = pd.DataFrame([fila])

# ===============================
# PROBABILIDADES
# ===============================

probs_numeros = []

for numero, modelo in modelos_numeros.items():

    prob = modelo.predict_proba(X_pred)[0][1]

    probs_numeros.append({
        "numero": numero,
        "probabilidad": round(float(prob), 3)
    })

probs_numeros.sort(
    key=lambda x: x["probabilidad"],
    reverse=True
)

probs_estrellas = []

for estrella, modelo in modelos_estrellas.items():

    prob = modelo.predict_proba(X_pred)[0][1]

    probs_estrellas.append({
        "estrella": estrella,
        "probabilidad": round(float(prob), 3)
    })

probs_estrellas.sort(
    key=lambda x: x["probabilidad"],
    reverse=True
)

numeros = sorted(
    [x["numero"] for x in probs_numeros[:5]]
)

estrellas = sorted(
    [x["estrella"] for x in probs_estrellas[:2]]
)

fecha = datetime.now().strftime(
    "%d/%m/%Y %H:%M:%S"
)

# ===============================
# HTML
# ===============================

docs_dir = BASE_DIR / "docs"
docs_dir.mkdir(exist_ok=True)

html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Euromillones IA</title>

<style>

body {{
    font-family: Arial,sans-serif;
    background:#f3f4f6;
    text-align:center;
    padding:30px;
}}

.card {{
    background:white;
    max-width:1000px;
    margin:auto;
    padding:25px;
    border-radius:12px;
    box-shadow:0 2px 10px rgba(0,0,0,.1);
}}

.numero {{
    display:inline-block;
    width:60px;
    height:60px;
    line-height:60px;
    margin:5px;
    border-radius:50%;
    background:#2563eb;
    color:white;
    font-weight:bold;
    font-size:22px;
}}

.estrella {{
    display:inline-block;
    width:60px;
    height:60px;
    line-height:60px;
    margin:5px;
    border-radius:50%;
    background:#f59e0b;
    color:white;
    font-weight:bold;
    font-size:22px;
}}

table {{
    width:100%;
    border-collapse:collapse;
    margin-top:20px;
}}

th,td {{
    border:1px solid #ddd;
    padding:10px;
}}

th {{
    background:#e5e7eb;
}}

</style>

</head>

<body>

<div class="card">

<h1>🎲 Predicción Euromillones IA</h1>

<p>
📅 Última generación:
<strong>{fecha}</strong>
</p>

<h2>Combinación Recomendada</h2>

<div>
"""

for n in numeros:
    html += f'<span class="numero">{n}</span>'

html += "</div><br><div>"

for e in estrellas:
    html += f'<span class="estrella">⭐{e}</span>'

html += """
</div>

<h2>Top 10 números más probables</h2>

<table>
<tr>
<th>Número</th>
<th>Probabilidad</th>
</tr>
"""

for item in probs_numeros[:10]:

    html += f"""
<tr>
<td>{item["numero"]}</td>
<td>{item["probabilidad"]}</td>
</tr>
"""

html += """
</table>

<h2>Top estrellas</h2>

<table>
<tr>
<th>Estrella</th>
<th>Probabilidad</th>
</tr>
"""

for item in probs_estrellas[:5]:

    html += f"""
<tr>
<td>{item["estrella"]}</td>
<td>{item["probabilidad"]}</td>
</tr>
"""

html += """
</table>

</div>

</body>
</html>
"""

with open(
    docs_dir / "index.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(html)

print("✅ docs/index.html generado")