from flask import Flask
import random as r

app = Flask(__name__)
link = '<iframe src="https://www.meteoblue.com/es/tiempo/semana/bogot%c3%a1_colombia_3688689?day=2&utm_source=weather_widget&utm_medium=linkus&utm_content=daily&utm_campaign=Weather%2BWidget" width="200" height="300"></iframe>'
h1 = '<h1>Dependecias Tecnologicas</h1>'
h2 = '<h2>estas expuesto?</h2>'
p = '<p>en los ultimops años esta problematica a aumentado de manera preocupante</p>'
a = '<a href= "/factos">una lista de datos</a>'
a2 = '<a href= "/factos_random">dato aleatorio</a>'
facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la adicción tecnológica es una de las áreas más relevantes de la investigación científica moderna.",
            "Según un estudio de Penn State , el 77 % afirmó que la sociedad en su conjunto dependía demasiado de la tecnología para tener éxito.",
            "Según Trendhunter , el 66% de la población sufre de nomofobia en la actualidad.",
            "El tipo de entretenimiento que obtenemos hoy en día a través de la tecnología se conoce como entretenimiento pasivo",
            "Según DoSomething.org , aproximadamente el 37 % de los jóvenes de entre 12 y 17 años han sufrido acoso cibernético. El 30 % lo ha sufrido más de una vez.",
            "En 2019, más de 37 millones de estadounidenses viajaron al extranjero . En 2002, menos de veinte años antes, esa cifra era de 23 millones. No cabe duda de que esto se debe en gran medida a los avances tecnológicos, que han hecho que viajar sea más asequible y accesible."
            "Provoca liberación de dopamina, igual que otras adicciones, generando placer inmediato y dependencia.",
            "Según el escritor Max Read de NYMag , …menos del 60 por ciento del tráfico web es humano; algunos años, según algunos investigadores, una considerable mayoría es bot´.",
            "los investigadores han encontrado evidencia de que las personas que abusan de la tecnología pueden desarrollar una química cerebral y patrones neuronales similares a los de quienes son adictos a sustancias"]
@app.route("/")
def hello_world():
    return h1 + h2 + p + a + "<br>" + a2

@app.route("/factos")
def factos():
    facts_html = '<h1>Factos</h1><ul>'
    for fact in facts_list:
        facts_html += f'<li>{fact}</li>'
    facts_html += '</ul>'
    return facts_html

@app.route("/factos_random")
def random_factos():
    fact= r.choice(facts_list)
    
    return f"<h1>Facto Aleatorio</h1><p>{fact}</p>"+"<a href"> "/"

app.run(debug=True)