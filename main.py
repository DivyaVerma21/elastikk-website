from flask import Flask, render_template_string, request

app = Flask(__name__)

MESH_GRADIENT = "https://uploads-ssl.webflow.com/647886eeb6848a73ecd0a8c3/64c8f265b6b0ce7cd7ffc96d_Mesh-7.svg"

base_template = """
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <title>Elastikk AS – Frigjør kapasitet med teknologi</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Open+Sans:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --blue1: #0e273b;
            --blue2: #1056b8;
            --teal: #64dab7;
            --accent: #ffc529;
            --grey-bg: #f7f8fa;
            --container-bg: #fff;
        }
        body {
            font-family: 'Open Sans', Arial, sans-serif;
            background: var(--grey-bg) url('{{ mesh_gradient }}') no-repeat center center fixed;
            background-size: cover;
            margin: 0;
            color: #222;
        }
        header {
            background: rgba(14,39,59,0.97);
            color: white;
            padding: 2.8rem 0 2rem 0;
            text-align: center;
            box-shadow: 0 3px 15px rgba(16,86,184,0.05);
            background-image: url('{{ mesh_gradient }}'), linear-gradient(90deg, #0e273b 0%, #1056b8 70%, #64dab7 100%);
            background-blend-mode: overlay;
            background-size: cover;
            border-bottom-left-radius: 40px;
            border-bottom-right-radius: 40px;
        }
        h1 {
            margin-bottom: 0.5rem;
            font-family: 'Montserrat', Arial, sans-serif;
            font-size: 2.5rem;
            letter-spacing: 0.5px;
        }
        header p {
            font-weight: 600;
            font-size: 1.18rem;
            margin-top: 0.7rem;
            letter-spacing: 0.5px;
        }
        nav {
            background: var(--container-bg);
            padding: 1rem 0;
            box-shadow: 0 1px 8px rgba(0,0,0,0.03);
            display: flex;
            justify-content: center;
            gap: 1.2rem;
            border-bottom: 1px solid #eee;
        }
        nav a {
            color: var(--blue2);
            text-decoration: none;
            font-weight: 700;
            font-family: 'Montserrat', Arial, sans-serif;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            transition: background 0.2s, color 0.2s;
        }
        nav a.active {
            color: #fff;
            background: var(--blue2);
        }
        nav a.lang {
            background: var(--accent);
            color: var(--blue1);
            font-weight: bold;
            border-radius: 8px;
            margin-left: 10px;
        }
        nav a.lang.active {
            background: var(--blue2);
            color: #fff;
        }
        .container {
            max-width: 950px;
            margin: 3rem auto;
            background: var(--container-bg);
            padding: 2.5rem 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 18px rgba(16,86,184,0.12);
            backdrop-filter: blur(1px);
        }
        h2, h3 {
            color: var(--blue2);
            font-family: 'Montserrat', Arial, sans-serif;
        }
        h2 { font-size: 2.1rem; margin-bottom: 1rem;}
        h3 { font-size: 1.25rem; margin-top: 2rem;}
        ul {
            margin-top: 1rem;
            padding-left: 1.5em;
        }
        ul li { margin-bottom: 0.7em; font-size: 1.06rem;}
        a.button, .container a:not(.button) {
            display: inline-block;
            padding: 0.57rem 1.35rem;
            color: var(--blue1);
            background: var(--accent);
            font-weight: bold;
            border-radius: 8px;
            text-decoration: none;
            margin: 1.3rem 0 0.6rem 0;
            font-family: 'Montserrat', Arial, sans-serif;
            transition: background 0.2s, color 0.2s;
        }
        .container a:not(.button):hover, a.button:hover {
            background: var(--blue2);
            color: #fff;
        }
        footer {
            background: linear-gradient(90deg, #0e273b 0%, #1056b8 70%, #64dab7 100%);
            color: white;
            font-size: 1.07rem;
            text-align: center;
            padding: 2rem 0 1.2rem 0;
            border-top-left-radius: 40px;
            border-top-right-radius: 40px;
            margin-top: 5rem;
        }
        @media (max-width: 750px) {
            .container { margin: 1.3rem; padding: 1rem;}
            h1 { font-size: 2rem;}
            nav { flex-direction: column; gap: 0.5rem; }
        }
    </style>
</head>
<body>
    <header>
        <h1>Elastikk AS</h1>
        <p>{% if lang == 'no' %}Kapasitetskrisen er her. Hva gjør vi nå?{% else %}The Capacity Crisis is Here. What do we do now?{% endif %}</p>
    </header>
    <nav>
        <a href="{{ url_for('home') }}" class="{% if lang == 'no' and request.path == '/' %}active{% elif lang == 'en' and request.path == '/en' %}active{% endif %}">{% if lang == 'no' %}Hjem{% else %}HOME{% endif %}</a>
        <a href="{{ url_for('solutions', lang=lang) }}" class="{% if (lang == 'no' and request.path.startswith('/losninger')) or (lang == 'en' and request.path.startswith('/en/solutions')) %}active{% endif %}">{% if lang == 'no' %}Våre løsninger{% else %}Our Solutions{% endif %}</a>
        <a href="{{ url_for('contact', lang=lang) }}" class="{% if (lang == 'no' and request.path.startswith('/kontakt')) or (lang == 'en' and request.path.startswith('/en/contact')) %}active{% endif %}">{% if lang == 'no' %}Kontakt{% else %}Contact{% endif %}</a>
        <a href="{{ url_for('partners', lang=lang) }}" class="{% if (lang == 'no' and request.path.startswith('/partnere')) or (lang == 'en' and request.path.startswith('/en/partners')) %}active{% endif %}">{% if lang == 'no' %}Partnere{% else %}Partners{% endif %}</a>
        <a href="{{ url_for('home_en') }}" class="lang {% if lang == 'en' %}active{% endif %}">English</a>
        <a href="{{ url_for('home') }}" class="lang {% if lang == 'no' %}active{% endif %}">Norsk</a>
    </nav>
    <div class="container">
        {{ content|safe }}
    </div>
    <footer>
        <p>{% if lang == 'no' %}© 2025 Elastikk AS. Org.nr 934 898 230. Laget med energi ⚡️ i Halden, Norge 🇳🇴.{% else %}© 2025 Elastikk AS. Org.no 934 898 230. Made with energy ⚡️ in Halden, Norway 🇳🇴.{% endif %}</p>
    </footer>
</body>
</html>
"""

NORWEGIAN = {
    'home_content': """
        <h2>Frigjør kapasitet med teknologi, ikke bare kabel</h2>
        <p>Elektrifiseringen skyter fart, og etterspørselen etter nettkapasitet er rekordhøy. Over 30 000 MW står i kø for tilkobling, og hvert MW i venteposisjon koster samfunnet over 2,4 millioner kroner. Presset på nettselskapene øker.</p>
        <p>Det er ikke lenger nok å bygge nytt – vi må bruke nettet smartere.</p>
        <a href="/losninger" class="button">Se hvordan Elastikk fungerer →</a>
    """,
    'solutions_content': """
        <h2>Våre løsninger</h2>
        <h3>AI-modellen som konkretiserer det alle «vet»</h3>
        <p>
        Energikrisen i 2021 markerte et vendepunkt i Norge. Elastikk er en AI-modell basert på prissignaler og forbruksdata fra 2021 til i dag, for å simulere og kvantifisere hvordan strømforbruket utvikler seg – helt ned på timesnivå.
        </p>
        <ul>
            <li>Ser hvordan ulike tiltak påvirker forbruket på kort og lang sikt</li>
            <li>Gir nettselskapene grunnlag for planlegging og styring</li>
            <li>Løsningen er en skybasert API-tjeneste</li>
        </ul>
        <h3>Tariffadministrator</h3>
        <p>Et webverktøy for effektiv prissignalering. Øk utnyttelse i eksisterende nett, frigjør kapasitet gjennom smartere prising, og påvirk forbruket – helt uten fysiske inngrep.</p>
        <a href="/kontakt" class="button">Be om demo!</a>
        <h3>Bygg fremtidens nett – uten å vente på nettutbygging</h3>
        <p>
        Med Elastikk kan nettselskaper møte kravene i en ny energivirkelighet: redusere KILE-kostnader, prioritere nettinvesteringer og dokumentere effekten av tariffendringer.
        </p>
    """,
    'contact_content': """
        <h2>Kontakt</h2>
        <ul>
            <li>E-post: <a href="mailto:contact@elastikk.com">contact@elastikk.com</a></li>
            <li>Tlf: <a href="tel:+4795212502">+47 952 12 502</a></li>
            <li><a href="https://poc.elastikk.com/" class="button">Logg inn!</a></li>
            <li><a href="#" class="button">Book et møte!</a></li>
        </ul>
    """,
    'partners_content': """
        <h2>Våre partnere</h2>
        <ul>
            <li>Innovasjon Norge – etableringsstøtte for innovasjon og vekst</li>
            <li>Microsoft for Startups Founders Hub</li>
        </ul>
    """
}

ENGLISH = {
    'home_content': """
        <h2>Free Up Capacity with Technology, Not Just Cables</h2>
        <p>Electrification is accelerating, and demand for grid capacity is at a record high. Over 30,000 MW are waiting in line for connection, and each MW in the queue costs society over 2.4 million NOK. Pressure on grid companies is increasing.</p>
        <p>Building new alone is no longer enough – we need to use the grid smarter.</p>
        <a href="/en/solutions" class="button">See How Elastikk Works →</a>
    """,
    'solutions_content': """
        <h2>Our Solutions</h2>
        <h3>The AI Model That Measures What Everyone “Knows”</h3>
        <p>
        The energy crisis of 2021 marked a turning point in Norway. Elastikk is an AI model based on price signals and consumption data from 2021 to today, simulating and quantifying electricity use – down to the hour.
        </p>
        <ul>
            <li>Shows how different measures affect consumption short- and long-term</li>
            <li>Provides grid companies with new planning and management tools</li>
            <li>Offered as a cloud-based API service</li>
        </ul>
        <h3>Tariff Administrator</h3>
        <p>A web tool for efficient price signaling. Increase utilization of existing networks, free up capacity through smarter pricing, and influence consumption – all without physical upgrades.</p>
        <a href="/en/contact" class="button">Request a Demo!</a>
        <h3>Build the Grid of the Future – Without Waiting for Extensions</h3>
        <p>
        With Elastikk, companies can meet the demands of a new energy reality: reduce outage costs, prioritize investments, and document the effects of tariff changes.
        </p>
    """,
    'contact_content': """
        <h2>Contact</h2>
        <ul>
            <li>Email: <a href="mailto:contact@elastikk.com">contact@elastikk.com</a></li>
            <li>Phone: <a href="tel:+4795212502">+47 952 12 502</a></li>
            <li><a href="https://poc.elastikk.com/" class="button">Log in!</a></li>
            <li><a href="#" class="button">Book a meeting!</a></li>
        </ul>
    """,
    'partners_content': """
        <h2>Our Partners</h2>
        <ul>
            <li>Innovation Norway – establishment support for innovation and growth</li>
            <li>Microsoft for Startups Founders Hub</li>
        </ul>
    """
}

@app.route("/")
def home():
    return render_template_string(
        base_template,
        content=NORWEGIAN["home_content"],
        lang="no",
        mesh_gradient=MESH_GRADIENT,
        request=request
    )

@app.route("/losninger")
def solutions():
    return render_template_string(
        base_template,
        content=NORWEGIAN["solutions_content"],
        lang="no",
        mesh_gradient=MESH_GRADIENT,
        request=request
    )

@app.route("/kontakt")
def contact():
    return render_template_string(
        base_template,
        content=NORWEGIAN["contact_content"],
        lang="no",
        mesh_gradient=MESH_GRADIENT,
        request=request
    )

@app.route("/partnere")
def partners():
    return render_template_string(
        base_template,
        content=NORWEGIAN["partners_content"],
        lang="no",
        mesh_gradient=MESH_GRADIENT,
        request=request
    )

@app.route("/en")
def home_en():
    return render_template_string(
        base_template,
        content=ENGLISH["home_content"],
        lang="en",
        mesh_gradient=MESH_GRADIENT,
        request=request
    )

@app.route("/en/solutions")
def solutions_en():
    return render_template_string(
        base_template,
        content=ENGLISH["solutions_content"],
        lang="en",
        mesh_gradient=MESH_GRADIENT,
        request=request
    )

@app.route("/en/contact")
def contact_en():
    return render_template_string(
        base_template,
        content=ENGLISH["contact_content"],
        lang="en",
        mesh_gradient=MESH_GRADIENT,
        request=request
    )

@app.route("/en/partners")
def partners_en():
    return render_template_string(
        base_template,
        content=ENGLISH["partners_content"],
        lang="en",
        mesh_gradient=MESH_GRADIENT,
        request=request
    )

if __name__ == "__main__":
    app.run(debug=True)
