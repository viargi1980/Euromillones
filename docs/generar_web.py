from pathlib import Path
import json
import re
import requests
from bs4 import BeautifulSoup


def obtener_bote():

    try:

        url = "https://www.euromillones.com.es/"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/131.0 Safari/537.36"
            )
        }

        r = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        r.raise_for_status()

        html = r.text

        patrones = [

            r'Bote de\s+(\d+)\s+millones',

            r'(\d+)\s+Millones de Euros',

            r'(\d+)\s+millones de euros',

            r'(\d+)\s+Millones de €'

        ]

        for patron in patrones:

            match = re.search(
                patron,
                html,
                re.IGNORECASE
            )

            if match:

                return f"{match.group(1)} M€"

        return "No disponible"

    except Exception as e:

        print("Error obteniendo bote:", e)

        return "No disponible"



BASE_DIR = Path(__file__).resolve().parent

with open(
    BASE_DIR / "prediccion.json",
    "r",
    encoding="utf-8"
) as f:
    prediccion = json.load(f)

bote = obtener_bote()

html = f"""
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>Euromillones IA</title>

<style>

:root {{

    --bg:#0f172a;
    --card:#111827;
    --card2:#1e293b;
    --text:#ffffff;
    --muted:#94a3b8;
    --accent:#3b82f6;
    --gold:#fbbf24;
    --green:#22c55e;
}}

* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

body {{
    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(59,130,246,.35),
            transparent 40%
        ),

        radial-gradient(
            circle at 80% 30%,
            rgba(168,85,247,.30),
            transparent 40%
        ),

        radial-gradient(
            circle at 50% 80%,
            rgba(34,197,94,.25),
            transparent 40%
        ),

        radial-gradient(
            circle at 90% 90%,
            rgba(236,72,153,.25),
            transparent 40%
        ),

        #0f172a;

    background-attachment: fixed;

    color: var(--text);

    font-family:
        Inter,
        Segoe UI,
        Arial,
        sans-serif;

    min-height: 100vh;

    overflow-x: hidden;

}}

.container {{

    max-width:900px;

    margin:auto;

    padding:40px 20px;
}}

.header {{

    text-align:center;

    margin-bottom:45px;
}}

.header h1 {{

    font-size:3rem;

    margin-bottom:10px;

    font-weight:800;

    background:
        linear-gradient(
            90deg,
            #60a5fa,
            #a78bfa,
            #f472b6
        );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}}

.header p {{

    color:var(--muted);
}}

.card {{

    background:
        rgba(17,24,39,.70);

    backdrop-filter:
        blur(20px);

    -webkit-backdrop-filter:
        blur(20px);

    border:
        1px solid rgba(255,255,255,.08);

    border-radius:24px;

    padding:40px;

    animation:fadeIn .8s ease;

    box-shadow:
        0 20px 80px rgba(0,0,0,.35);
}}

@keyframes fadeIn {{

    from {{

        opacity:0;

        transform:translateY(20px);
    }}

    to {{

        opacity:1;

        transform:translateY(0);
    }}
}}

.info {{

    text-align:center;

    color:var(--muted);

    margin-bottom:25px;
}}

.jackpot {{

    text-align:center;

    padding:18px;

    margin-bottom:35px;

    border-radius:18px;

    background:
        linear-gradient(
            135deg,
            rgba(34,197,94,.20),
            rgba(59,130,246,.20)
        );

    backdrop-filter:
        blur(10px);

    border:
        1px solid rgba(255,255,255,.10);

    color:white;

    font-size:1.2rem;

    font-weight:700;
}}

.section-title {{

    margin-bottom:20px;

    font-size:1.15rem;
}}

.numbers {{

    display:flex;

    justify-content:center;

    flex-wrap:wrap;

    gap:15px;

    margin-bottom:40px;
}}

.numero {{

    width:72px;

    height:72px;

    border-radius:50%;

    display:flex;

    align-items:center;

    justify-content:center;

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #60a5fa
        );

    font-size:1.5rem;

    font-weight:bold;

    color:white;

    box-shadow:
        0 10px 30px rgba(37,99,235,.35);

    transition:.3s;
}}

.numero:hover {{

    background:var(--accent);

    transform:translateY(-4px);
}}

.estrella {{

    min-width:90px;

    text-align:center;

    padding:12px 18px;

    border-radius:999px;

    background:
        linear-gradient(
            135deg,
            #f59e0b,
            #fbbf24
        );

    color:#111827;

    font-weight:700;

    box-shadow:
        0 8px 25px rgba(245,158,11,.25);
}}

.estrella {{

    min-width:80px;

    text-align:center;

    padding:12px 18px;

    border-radius:999px;

    background:var(--card2);

    color:var(--gold);

    font-weight:bold;
}}

.rank {{

    margin-bottom:18px;
}}

.rank-label {{

    display:flex;

    justify-content:space-between;

    margin-bottom:6px;
}}

.bar {{

    height:8px;

    background:var(--card2);

    border-radius:999px;

    overflow:hidden;
}}

.fill {{

    height:100%;

    border-radius:999px;

    background:linear-gradient(
        90deg,
        #2563eb,
        #60a5fa
    );
}}

.footer {{

    margin-top:35px;

    text-align:center;

    color:var(--muted);

    font-size:.9rem;
}}

@media(max-width:768px) {{

    .header h1 {{
        font-size:2rem;
    }}

    .numero {{

        width:60px;

        height:60px;

        font-size:1.2rem;
    }}

    .card {{
        padding:25px;
    }}
}}

body::before {{

    content:"";

    position:fixed;

    inset:0;

    background:

        radial-gradient(
            circle at 20% 20%,
            rgba(59,130,246,.35),
            transparent 35%
        ),

        radial-gradient(
            circle at 80% 30%,
            rgba(168,85,247,.30),
            transparent 35%
        ),

        radial-gradient(
            circle at 60% 80%,
            rgba(236,72,153,.20),
            transparent 35%
        );

    filter:blur(80px);

    z-index:-1;

    animation:aurora 15s infinite alternate;
}}

@keyframes aurora {{

    from {{
        transform:translateX(-40px);
    }}

    to {{
        transform:translateX(40px);
    }}
}}

</style>

</head>

<body>

<div class="container">

<div class="header">

    <h1>🎯 Euromillones IA</h1>

    <p>
        Predicción basada en Machine Learning
    </p>

</div>

<div class="card">

<div class="info">
    Generado el {prediccion["fecha_generacion"]}
</div>

<div class="jackpot">
    💰 Bote actual: {bote}
</div>

<h2 class="section-title">
🏆 Combinación recomendada
</h2>

<div class="numbers">
"""

for numero in prediccion["numeros"]:
    html += f"""
    <div class="numero">
        {numero}
    </div>
    """

html += """
</div>

<h2 class="section-title">
⭐ Estrellas más probables
</h2>

<div class="estrellas">
"""

for estrella in prediccion["top_estrellas"][:2]:

    html += f"""
    <div class="estrella">
        ⭐ {estrella["estrella"]}
    </div>
    """

html += """
</div>

<h2 class="section-title">
📈 Top números más probables
</h2>
"""

for item in prediccion["top_numeros"]:

    prob = item["probabilidad"] * 100

    html += f"""
    <div class="rank">

        <div class="rank-label">

            <span>
                Número {item["numero"]}
            </span>

            <span>
                {prob:.1f}%
            </span>

        </div>

        <div class="bar">

            <div
                class="fill"
                style="width:{prob:.1f}%"
            ></div>

        </div>

    </div>
    """

html += """
<div class="footer">
    Euromillones IA
</div>

</div>

</div>

</body>
</html>
"""
print(obtener_bote())

with open(
    BASE_DIR / "index.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(html)

print("✅ index.html generado")