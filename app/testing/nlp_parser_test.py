from app.services.nlp_parser import KeywordExtractor

samples = [
    # Español - ciencia
    "Deseo una investigacion relacionada a la microbiologia, al ADN de las personas y que sea representativo",
    "Estudio sobre células madre y regeneración tisular",
    "Quiero informacion sobre inteligencia artificial y aprendizaje automatico",
    "Busco articulos cientificos sobre quimica organica y farmacos",
    "Análisis de proteínas en bioinformática y genómica",
    "Investigación de vacunas contra virus RNA",
    "Estudio de metabolismo celular y vías bioquímicas",

    # Inglés - ciencia
    "This study focuses on quantum computing and entanglement in physics",
    "Machine learning applications in drug discovery",
    "Deep learning models for natural language processing",
    "Renewable energy sources and solar panel efficiency",
    "Neural networks applied to medical image segmentation",
    "Climate change effects on ocean currents and biodiversity",
    "CRISPR gene editing in model organisms",

    # Español-Inglés mixto
    "Aplicaciones de blockchain en financial technology",
    "Estudio sobre artificial intelligence aplicada a medicina",
    "Quimica organica synthesis of new pharmaceuticals",

    # Francés
    "Recherche sur l'intelligence artificielle et apprentissage automatique",
    "Analyse des protéines et génomique",
    "Chimie organique et développement de médicaments",

    # Alemán
    "Studie zur Zellbiologie und molekularen Mechanismen",
    "Maschinelles Lernen für medizinische Bildanalyse",
    "Organische Chemie und pharmazeutische Synthese",

    # Portugués
    "Pesquisa sobre biotecnologia e engenharia genética",
    "Aplicações de inteligência artificial em saúde",
    "Química orgânica e desenvolvimento de fármacos",

    # Japonés (transliterado)
    "人工知能と機械学習の応用に関する研究",
    "細胞生物学と分子生物学の分析",
    "有機化学と薬物開発の研究",

    # Irrelevante / conversación
    "Hola que hora es",
    "Respondeme si los humanos pueden vivir en marte",
    "Cuál es la capital de Francia",
    "Me puedes dar un resumen del partido de fútbol de ayer",

    # Ambiguo / general
    "Información sobre ciencias",
    "Deseo saber sobre investigación en computación",
    "Quiero conocer temas de biología y química",

    # Nombres propios / lugares
    "Estudio sobre genes BRCA1 y BRCA2 en pacientes de USA",
    "Investigación de la biodiversidad en Amazon rainforest",
    "Experimentos en MIT sobre física cuántica",

    # Con números, fórmulas o técnicas
    "Medición de pH, NaCl y concentración de ATP en muestras celulares",
    "Síntesis de C6H12O6 y derivados en química orgánica",
    "Secuenciación de ADN y análisis de SNPs",

    # Casos de prueba extremos / mezclas
    "Data science, estadística y análisis de big data",
    "Física teórica y experimental: partículas subatómicas y neutrinos",
    "Ingeniería genética y modificación de organismos",
    "Aplicación de IA en diagnósticos médicos y farmacología",
]

extractor = KeywordExtractor(api_key="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")

for str in samples:
    print(extractor.extract(str))


#for str in samples:
#        keywords = extractor.extract(str)
#        print(f"- {str}:")
#        for k in keywords:
#            print(f"\t{k}")
