def howarts_dev():

    casas = {
        "Frontend": 0,
        "Backend": 0,
        "Mobile": 0,
        "Data": 0,
    }

    preguntas = {
    "¿Qué tipo de desafíos disfrutas más?": [
        ("Resolver problemas de lógica y estructuras de datos", {"Backend": 2, "Data": 1}),
        ("Diseñar interfaces atractivas e interactivas", {"Frontend": 2, "Mobile": 1}),
        ("Crear aplicaciones móviles eficientes y fluidas", {"Mobile": 2, "Frontend": 1}),
        ("Analizar datos y encontrar patrones", {"Data": 2, "Backend": 1})
    ],
    "¿Cuál de estos proyectos te interesa más?": [
        ("Un sistema de bases de datos optimizado", {"Backend": 2, "Data": 1}),
        ("Una web con animaciones avanzadas", {"Frontend": 2, "Mobile": 1}),
        ("Una aplicación móvil de e-commerce", {"Mobile": 2, "Frontend": 1}),
        ("Un modelo de machine learning", {"Data": 2, "Backend": 1})
    ],
    "¿Qué herramienta te gustaría dominar?": [
        ("SQL y bases de datos", {"Backend": 2, "Data": 1}),
        ("JavaScript y React", {"Frontend": 2, "Mobile": 1}),
        ("Swift o Kotlin", {"Mobile": 2, "Frontend": 1}),
        ("Python para análisis de datos", {"Data": 2, "Backend": 1})
    ],
    "¿Cuál de estas frases te representa más?": [
        ("Me gusta optimizar algoritmos", {"Backend": 2, "Data": 1}),
        ("Me encanta hacer diseños impactantes", {"Frontend": 2, "Mobile": 1}),
        ("Me interesa la experiencia de usuario en móviles", {"Mobile": 2, "Frontend": 1}),
        ("Analizar grandes volúmenes de datos es mi pasión", {"Data": 2, "Backend": 1})
    ],
    "¿Cuál es tu lenguaje de programación favorito?": [
        ("Python o Java", {"Backend": 2, "Data": 1}),
        ("JavaScript o TypeScript", {"Frontend": 2, "Mobile": 1}),
        ("Swift o Kotlin", {"Mobile": 2, "Frontend": 1}),
        ("SQL o R", {"Data": 2, "Backend": 1})
    ],
    "Si tuvieras que elegir un framework, ¿cuál sería?": [
        ("Django o Spring Boot", {"Backend": 2, "Data": 1}),
        ("React o Angular", {"Frontend": 2, "Mobile": 1}),
        ("Flutter o React Native", {"Mobile": 2, "Frontend": 1}),
        ("TensorFlow o Pandas", {"Data": 2, "Backend": 1})
    ],
    "¿Cuál de estas tareas te resulta más interesante?": [
        ("Crear APIs y administrar servidores", {"Backend": 2, "Data": 1}),
        ("Hacer interfaces atractivas y accesibles", {"Frontend": 2, "Mobile": 1}),
        ("Optimizar el rendimiento de una app móvil", {"Mobile": 2, "Frontend": 1}),
        ("Realizar análisis predictivos con datos", {"Data": 2, "Backend": 1})
    ],
    "Si fueras a desarrollar un producto, ¿qué te gustaría hacer?": [
        ("Un sistema robusto con gran escalabilidad", {"Backend": 2, "Data": 1}),
        ("Una web que sea visualmente impresionante", {"Frontend": 2, "Mobile": 1}),
        ("Una app que funcione rápido en cualquier dispositivo", {"Mobile": 2, "Frontend": 1}),
        ("Un sistema de análisis avanzado con IA", {"Data": 2, "Backend": 1})
    ],
    "¿Cómo prefieres trabajar?": [
        ("Me gusta el backend y la lógica del servidor", {"Backend": 2, "Data": 1}),
        ("Disfruto el diseño y la interacción con usuarios", {"Frontend": 2, "Mobile": 1}),
        ("Me interesa el desarrollo móvil y su optimización", {"Mobile": 2, "Frontend": 1}),
        ("Prefiero analizar datos y buscar patrones", {"Data": 2, "Backend": 1})
    ],
    "Si tuvieras que elegir un rol, ¿cuál sería?": [
        ("Backend Developer", {"Backend": 2, "Data": 1}),
        ("Frontend Developer", {"Frontend": 2, "Mobile": 1}),
        ("Mobile Developer", {"Mobile": 2, "Frontend": 1}),
        ("Data Scientist", {"Data": 2, "Backend": 1})
    ]
}
    
    for pregunta, opciones in preguntas.items():
        print(f"{pregunta}")

        for i,(opcion, puntuacion) in enumerate(opciones, 1):
            print(f"{i} - {opcion}")

        while True:
            try:
                eleccion = abs(int(input("Selecciona una opción: ")))
                if 1 <= eleccion <= 4:
                    break
                print("Error: Opción invalida")
            except ValueError:
                print("Error: Ingresa una opción valida")

        puntos = opciones[eleccion - 1][1]

        for casa, valor in puntos.items():
            casas[casa] += valor
    

    casa_eleccion = sorted(casas.items(), key=lambda item: item[1], reverse=True)[0][0]
    print(f"La casa que más te conviene es: {casa_eleccion}")


howarts_dev()