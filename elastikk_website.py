from flask import Flask, render_template_string, url_for, request

app = Flask(__name__)

base_template = """
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <title>Elastikk AS – Frigjør kapasitet med teknologi</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Open+Sans:wght@400;700&display=swap" rel="stylesheet">
    <style>
        html, body {
            height: 100%%;
            margin: 0;
            padding: 0;
        }
        body {
            min-height: 100vh;
            background: url('{{ sunrise_img }}') no-repeat center center fixed;
            background-size: cover;
            font-family: 'Open Sans', Arial, sans-serif;
            color: #fff;
        }
        .overlay {
            min-height: 100vh;
            background: rgba(22,38,52,0.48);
            width: 100%%;
            position: absolute;
            z-index: 0;
            top: 0;
            left: 0;
        }
        .main-content {
            position: relative;
            z-index: 2;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        header {
            width: 100%%;
            background: transparent;
            display: flex;
            align-items: center;
            padding: 2.2rem 5vw 1.1rem 5vw;
            box-sizing: border-box;
            position: relative;
        }
        .logo-img {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            margin-right: 20px;
            background: white;
            object-fit: contain;
            box-shadow: 0 4px 16px rgba(16,86,184,0.13);
        }
        .brand-title {
            font-family: 'Montserrat', Arial, sans-serif;
            font-size: 2.4rem;
            font-weight: 700;
            letter-spacing: 1px;
            color: #fff;
            text-shadow: 0 2px 10px rgba(20,33,61,0.13);
            margin-right: auto;
        }
        .nav-bar {
            margin-left: auto;
            display: flex;
            align-items: center;
            gap: 2vw;
            padding: 0;
        }
        .nav-link {
            text-decoration: none;
            font-weight: 600;
            font-family: 'Montserrat', Arial, sans-serif;
            font-size: 1.1rem;
            padding: 0.4rem 1.05rem;
            border-radius: 7px;
            color: #fff;
            background: rgba(15,86,184,0.07);
            transition: background .2s, color .2s;
        }
        .nav-link.active, .nav-link.selected {
            background: #ffc529;
            color: #203040;
            box-shadow: 0 2px 12px rgba(255,197,41,0.07);
        }
        .header-actions {
            display: flex;
            align-items: center;
            gap: 1.1rem;
            margin-left: 2vw;
        }
        .action-btn {
            font-size: 1.02rem;
            padding: 0.45rem 1.12rem;
            border-radius: 8px;
            border: none;
            background: #ffc529;
            font-family: 'Montserrat', Arial, sans-serif;
            font-weight: bold;
            color: #223350;
            box-shadow: 0 2px 8px rgba(255,197,41,0.09);
            text-decoration: none;
            transition: background .2s, color .2s;
        }
        .action-btn:hover {
            color: #fff;
            background: #1056b8;
        }
        .lang-switcher {
            margin-left: 1.3vw;
            border-radius: 5px;
            font-size: 1rem;
            font-family: 'Montserrat', Arial, sans-serif;
            padding: 0.32rem 0.9rem;
            border: 1.5px solid #ffc529;
            color: #ffc529;
            background: rgba(15,86,184,0.10);
            font-weight: bold;
            box-shadow: 0 2px 12px rgba(32,48,64,0.04);
            outline: none;
            transition: border .2s,color .2s;
        }
        .lang-switcher:focus {
            border: 2px solid #ffc529;
            background: #fff;
            color: #203040;
        }
        .content-area {
            margin: 7vh auto 3vh auto;
            padding: 0 3vw;
            max-width: 920px;
            text-shadow: 0 2px 8px rgba(16,86,184,0.22);
        }
        h2, h3 {
            color: #ffc529;
            font-family: 'Montserrat', Arial, sans-serif;
            text-shadow: 0 2px 10px rgba(16,86,184,0.16);
        }
        h2 { font-size: 2.05rem; margin-bottom: 1.2rem; }
        h3 { font-size: 1.15rem; margin-top: 1.7rem;}
        p, ul, a { font-size: 1.1rem; }
        ul li { margin-bottom: 0.7em; }
        a.button, .content-area a.button {
            display: inline-block;
            padding: 0.56rem 1.18rem;
            color: #203040;
            background: #ffc529;
            font-weight: bold;
            border-radius: 7px;
            text-decoration: none;
            margin: 1.05rem 0 0.8rem 0;
            font-family: 'Montserrat', Arial, sans-serif;
            transition: background 0.2s, color 0.2s, border 0.2s;
            box-shadow: 0 1px 6px rgba(255,197,41,0.08);
        }
        a.button:hover, .content-area a.button:hover {
            background: #fff;
            color: #1056b8;
            border: 1.5px solid #ffc529;
        }
        .plain-link {
            color: #ffc529;
            text-decoration: underline;
            font-weight: 700;
            font-size: 1.14rem;
            background: transparent;
            border: none;
            transition: color .16s;
        }
        .plain-link:hover {
            color: #fff;
            text-decoration: underline;
        }
        @media (max-width: 800px) {
            header, .content-area { padding: 1rem 5vw;}
            .brand-title { font-size: 1.3rem; }
            .logo-img { width: 30px; height: 30px; margin-right: 10px;}
            .nav-link { font-size: 1rem; padding: 0.3rem 0.8rem;}
            .action-btn { font-size: 0.97rem; padding: 0.33rem 0.8rem;}
        }
    </style>
    <script>
        function languageSwitch(selectObj) {
            let lang = selectObj.value;
            let path = window.location.pathname;
            if (lang === "en") {
                if (path.startsWith("/en")) return;
                if (path === "/losninger") window.location.href = "/en/solutions";
                else if (path === "/kontakt") window.location.href = "/en/contact";
                else if (path === "/partnere") window.location.href = "/en/partners";
                else window.location.href = "/en";
            } else {
                if (!path.startsWith("/en")) return;
                if (path === "/en/solutions") window.location.href = "/losninger";
                else if (path === "/en/contact") window.location.href = "/kontakt";
                else if (path === "/en/partners") window.location.href = "/partnere";
                else window.location.href = "/";
            }
        }
    </script>
</head>
<body>
    <div class="overlay"></div>
    <div class="main-content">
        <header>
            <img src="{{ logo_img }}" alt="Elastikk Logo" class="logo-img">
            <span class="brand-title">Elastikk AS</span>
            <nav class="nav-bar">
                <a href="{{ url_for('home') }}" class="nav-link {% if lang == 'no' and request.path == '/' %}active{% endif %}">{% if lang == 'no' %}Hjem{% else %}Home{% endif %}</a>
                <a href="{{ url_for('solutions', lang=lang) }}" class="nav-link {% if (lang == 'no' and request.path.startswith('/losninger')) or (lang == 'en' and request.path.startswith('/en/solutions')) %}active{% endif %}">{% if lang == 'no' %}Våre løsninger{% else %}Our Solutions{% endif %}</a>
                <a href="{{ url_for('contact', lang=lang) }}" class="nav-link {% if (lang == 'no' and request.path.startswith('/kontakt')) or (lang == 'en' and request.path.startswith('/en/contact')) %}active{% endif %}">{% if lang == 'no' %}Kontakt{% else %}Contact{% endif %}</a>
                <a href="{{ url_for('partners', lang=lang) }}" class="nav-link {% if (lang == 'no' and request.path.startswith('/partnere')) or (lang == 'en' and request.path.startswith('/en/partners')) %}active{% endif %}">{% if lang == 'no' %}Partnere{% else %}Partners{% endif %}</a>
                <select class="lang-switcher" onchange="languageSwitch(this)">
                    <option value="no" {% if lang == 'no' %}selected{% endif %}>Norsk</option>
                    <option value="en" {% if lang == 'en' %}selected{% endif %}>English</option>
                </select>
            </nav>
            <div class="header-actions">
                <a href="https://poc.elastikk.com/" class="action-btn" target="_blank">{% if lang == 'no' %}Logg inn{% else %}Log in{% endif %}</a>
                <a href="#" class="action-btn">{% if lang == 'no' %}Book et møte{% else %}Book a meeting{% endif %}</a>
            </div>
        </header>
        <div class="content-area">
            {{ content|safe }}
        </div>
    </div>
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
        <p>Energikrisen i 2021 markerte et vendepunkt i Norge. Elastikk er en AI-modell basert på prissignaler og forbruksdata fra 2021 til i dag, for å simulere og kvantifisere hvordan strømforbruket utvikler seg – helt ned på timesnivå.</p>
        <ul>
            <li>Ser hvordan ulike tiltak påvirker forbruket på kort og lang sikt</li>
            <li>Gir nettselskapene grunnlag for planlegging og styring</li>
            <li>Løsningen er en skybasert API-tjeneste</li>
        </ul>
        <h3>Tariffadministrator</h3>
        <p>Et webverktøy for effektiv prissignalering. Øk utnyttelse i eksisterende nett, frigjør kapasitet gjennom smartere prising, og påvirk forbruket – helt uten fysiske inngrep.</p>
        <a href="/kontakt" class="button">Be om demo!</a>
        <h3>Bygg fremtidens nett – uten å vente på nettutbygging</h3>
        <p>Med Elastikk kan nettselskaper møte kravene i en ny energivirkelighet: redusere KILE-kostnader, prioritere nettinvesteringer og dokumentere effekten av tariffendringer.</p>
    """,
    'contact_content': """
        <h2>Kontakt</h2>
        <p>E-post: <a href="mailto:contact@elastikk.com" class="plain-link">contact@elastikk.com</a></p>
        <p>Tlf: <a href="tel:+4795212502" class="plain-link">+47 952 12 502</a></p>
        <p><a href="https://poc.elastikk.com/" target="_blank" class="plain-link">Logg inn</a></p>
        <p><a href="#" class="plain-link">Book et møte</a></p>
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
        <p>The energy crisis of 2021 marked a turning point in Norway. Elastikk is an AI model based on price signals and consumption data from 2021 to today, simulating and quantifying electricity use – down to the hour.</p>
        <ul>
            <li>Shows how different measures affect consumption short- and long-term</li>
            <li>Provides grid companies with new planning and management tools</li>
            <li>Offered as a cloud-based API service</li>
        </ul>
        <h3>Tariff Administrator</h3>
        <p>A web tool for efficient price signaling. Increase utilization of existing networks, free up capacity through smarter pricing, and influence consumption – all without physical upgrades.</p>
        <a href="/en/contact" class="button">Request a Demo!</a>
        <h3>Build the Grid of the Future – Without Waiting for Extensions</h3>
        <p>With Elastikk, companies can meet the demands of a new energy reality: reduce outage costs, prioritize investments, and document the effects of tariff changes.</p>
    """,
    'contact_content': """
        <h2>Contact</h2>
        <p>Email: <a href="mailto:contact@elastikk.com" class="plain-link">contact@elastikk.com</a></p>
        <p>Phone: <a href="tel:+4795212502" class="plain-link">+47 952 12 502</a></p>
        <p><a href="https://poc.elastikk.com/" target="_blank" class="plain-link">Log in</a></p>
        <p><a href="#" class="plain-link">Book a meeting</a></p>
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
        is_home=True,
        sunrise_img=url_for('static', filename='sunrise.jpg'),
        logo_img=url_for('static', filename='elastikk_logo.jpg'),
        request=request
    )

@app.route("/losninger")
def solutions():
    return render_template_string(
        base_template,
        content=NORWEGIAN["solutions_content"],
        lang="no",
        is_home=False,
        sunrise_img=url_for('static', filename='sunrise.jpg'),
        logo_img=url_for('static', filename='elastikk_logo.jpg'),
        request=request
    )

@app.route("/kontakt")
def contact():
    return render_template_string(
        base_template,
        content=NORWEGIAN["contact_content"],
        lang="no",
        is_home=False,
        sunrise_img=url_for('static', filename='sunrise.jpg'),
        logo_img=url_for('static', filename='elastikk_logo.jpg'),
        request=request
    )

@app.route("/partnere")
def partners():
    return render_template_string(
        base_template,
        content=NORWEGIAN["partners_content"],
        lang="no",
        is_home=False,
        sunrise_img=url_for('static', filename='sunrise.jpg'),
        logo_img=url_for('static', filename='elastikk_logo.jpg'),
        request=request
    )

@app.route("/en")
def home_en():
    return render_template_string(
        base_template,
        content=ENGLISH["home_content"],
        lang="en",
        is_home=True,
        sunrise_img=url_for('static', filename='sunrise.jpg'),
        logo_img=url_for('static', filename='elastikk_logo.jpg'),
        request=request
    )

@app.route("/en/solutions")
def solutions_en():
    return render_template_string(
        base_template,
        content=ENGLISH["solutions_content"],
        lang="en",
        is_home=False,
        sunrise_img=url_for('static', filename='sunrise.jpg'),
        logo_img=url_for('static', filename='elastikk_logo.jpg'),
        request=request
    )

@app.route("/en/contact")
def contact_en():
    return render_template_string(
        base_template,
        content=ENGLISH["contact_content"],
        lang="en",
        is_home=False,
        sunrise_img=url_for('static', filename='sunrise.jpg'),
        logo_img=url_for('static', filename='elastikk_logo.jpg'),
        request=request
    )

@app.route("/en/partners")
def partners_en():
    return render_template_string(
        base_template,
        content=ENGLISH["partners_content"],
        lang="en",
        is_home=False,
        sunrise_img=url_for('static', filename='sunrise.jpg'),
        logo_img=url_for('static', filename='elastikk_logo.jpg'),
        request=request
    )

if __name__ == "__main__":
    app.run(debug=True)
