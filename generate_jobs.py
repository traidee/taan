import os

template_file = "template.html"
with open(template_file, "r") as f:
    template = f.read()

import random

jobs = [
    {
        "filename": "job-ux-designer.html",
        "JOB_TITLE": "Senior UX/UI Designer",
        "COMPANY": "TechNova Solutions",
        "JOB_IMAGE": "https://images.unsplash.com/photo-1573164713988-8665fc963095?auto=format&fit=crop&w=1000&q=80",
        "ICON_BG": "bg-gray-100",
        "ICON_BORDER": "border-gray-200",
        "ICON_CLASS": "fab fa-google",
        "ICON_COLOR": "text-gray-600",
        "LOCATION": "Remoto 100%",
        "TYPE": "Tiempo Completo",
        "SALARY": "$45,000 - $60,000 MXN/mes",
        "DESCRIPTION": "En TechNova Solutions, creemos que la diversidad impulsa la innovación. Estamos buscando a una Senior UX/UI Designer apasionada por crear experiencias digitales excepcionales. Liderarás el rediseño completo de nuestra aplicación principal, trabajando codo a codo con nuestro equipo de ingeniería y producto.",
        "RESPONSIBILITIES": "<li>Liderar el diseño end-to-end de nuevas características de producto.</li><li>Realizar investigación de usuarios y pruebas de usabilidad.</li><li>Crear wireframes, prototipos interactivos y diseños de alta fidelidad.</li><li>Colaborar activamente en la creación y mantenimiento de nuestro Design System.</li>",
        "REQUIREMENTS": "<li>Mínimo 4 años de experiencia en diseño UX/UI.</li><li>Dominio avanzado de Figma y herramientas de prototipado.</li><li>Portafolio sólido demostrando resolución de problemas complejos.</li><li>Excelentes habilidades de comunicación y capacidad de defender decisiones de diseño.</li>",
        "BENEFITS": "<li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Horario 100% flexible</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Brecha salarial cero garantizada</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Apoyo económico por maternidad</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Seguro de gastos médicos mayores</li>"
    },
    {
        "filename": "job-cfo.html",
        "JOB_TITLE": "Directora de Finanzas (CFO)",
        "COMPANY": "Grupo Financiero Inclusivo",
        "JOB_IMAGE": "https://images.unsplash.com/photo-1556761175-5973dc0f32d7?auto=format&fit=crop&w=1000&q=80",
        "ICON_BG": "bg-blue-50",
        "ICON_BORDER": "border-blue-100",
        "ICON_CLASS": "fas fa-building",
        "ICON_COLOR": "text-blue-500",
        "LOCATION": "CDMX (Esquema Híbrido)",
        "TYPE": "Ejecutivo / Full-time",
        "SALARY": "Confidencial / Atractivo",
        "DESCRIPTION": "Estamos en la búsqueda de una Directora de Finanzas (CFO) visionaria para liderar nuestra estrategia financiera. Como organización certificada en equidad de género, estamos comprometidos con impulsar el liderazgo femenino en los puestos directivos más altos.",
        "RESPONSIBILITIES": "<li>Diseñar y ejecutar la estrategia financiera global de la compañía.</li><li>Liderar procesos de levantamiento de capital y relación con inversionistas.</li><li>Supervisar la planificación financiera, tesorería y contabilidad corporativa.</li><li>Participar activamente en el comité directivo y toma de decisiones clave.</li>",
        "REQUIREMENTS": "<li>Más de 8 años de experiencia en finanzas corporativas.</li><li>Experiencia previa comprobable en roles directivos (VP o C-Level).</li><li>Conocimiento profundo del sector financiero en México y LATAM.</li><li>Liderazgo empático y comprobado manejo de equipos multidisciplinarios.</li>",
        "BENEFITS": "<li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Bono ejecutivo anual por desempeño</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Esquema de trabajo híbrido flexible</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Permiso extendido por maternidad</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Presupuesto anual para formación ejecutiva</li>"
    },
    {
        "filename": "job-backend.html",
        "JOB_TITLE": "Ingeniera de Software Backend",
        "COMPANY": "EcoTech Startup",
        "JOB_IMAGE": "https://images.unsplash.com/photo-1573164574572-cb89e39749b4?auto=format&fit=crop&w=1000&q=80",
        "ICON_BG": "bg-green-50",
        "ICON_BORDER": "border-green-100",
        "ICON_CLASS": "fab fa-envira",
        "ICON_COLOR": "text-green-500",
        "LOCATION": "Remoto LatAm",
        "TYPE": "Tiempo Completo",
        "SALARY": "$3,000 - $4,500 USD/mes",
        "DESCRIPTION": "Únete a EcoTech, donde nuestro equipo de ingeniería está conformado en un 60% por mujeres increíbles. Estamos construyendo tecnología sustentable y buscamos una Ingeniera Backend sólida para optimizar nuestra infraestructura y desarrollar nuevas APIs.",
        "RESPONSIBILITIES": "<li>Arquitectar y desarrollar APIs RESTful escalables.</li><li>Optimizar el rendimiento de las bases de datos y consultas complejas.</li><li>Participar en revisiones de código y promover buenas prácticas.</li><li>Colaborar con el equipo frontend para integración de servicios.</li>",
        "REQUIREMENTS": "<li>Experiencia sólida (3+ años) con Python y frameworks como Django o FastAPI.</li><li>Conocimiento intermedio/avanzado de Node.js.</li><li>Experiencia manejando bases de datos relacionales (PostgreSQL).</li><li>Familiaridad con despliegues en AWS y contenedores Docker.</li>",
        "BENEFITS": "<li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Trabajo remoto permanente (LatAm)</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Días libres ilimitados (PTO)</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Mentoría 1:1 con líderes tech</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Apoyo para setup de home office</li>"
    },
    {
        "filename": "job-marketing.html",
        "JOB_TITLE": "Especialista en Marketing Digital",
        "COMPANY": "Agencia Creativa Violeta",
        "JOB_IMAGE": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1000&q=80",
        "ICON_BG": "bg-brand-50",
        "ICON_BORDER": "border-purple-100",
        "ICON_CLASS": "fas fa-bullhorn",
        "ICON_COLOR": "text-purple-500",
        "LOCATION": "Guadalajara, Jal.",
        "TYPE": "Medio Tiempo",
        "SALARY": "$15,000 - $20,000 MXN/mes",
        "DESCRIPTION": "Esta posición es ideal para madres profesionales que buscan reincorporarse al mundo laboral con horarios reducidos. En Agencia Violeta impulsamos marcas con propósito y necesitamos a alguien que gestione nuestras estrategias digitales B2B.",
        "RESPONSIBILITIES": "<li>Creación y ejecución de campañas en LinkedIn Ads y Google Ads.</li><li>Gestión de calendarios de contenido y redes sociales.</li><li>Análisis de métricas y elaboración de reportes mensuales de KPIs.</li><li>Optimización de embudos de conversión.</li>",
        "REQUIREMENTS": "<li>2+ años de experiencia en marketing digital B2B.</li><li>Certificaciones en Google Analytics o herramientas similares.</li><li>Excelente ortografía y redacción persuasiva (Copywriting).</li><li>Capacidad de organización y gestión del tiempo.</li>",
        "BENEFITS": "<li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Jornada reducida (4 horas al día)</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Posibilidad de esquema híbrido</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Guardería pagada</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Oportunidad de crecimiento interno</li>"
    },
    {
        "filename": "job-hr.html",
        "JOB_TITLE": "Gerente de Recursos Humanos",
        "COMPANY": "PeopleFirst Corporativo",
        "JOB_IMAGE": "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=1000&q=80",
        "ICON_BG": "bg-red-50",
        "ICON_BORDER": "border-red-100",
        "ICON_CLASS": "fas fa-users",
        "ICON_COLOR": "text-red-500",
        "LOCATION": "Monterrey, N.L.",
        "TYPE": "Tiempo Completo",
        "SALARY": "$50,000 - $70,000 MXN/mes",
        "DESCRIPTION": "Buscamos a una líder apasionada por la diversidad y la inclusión para tomar las riendas de nuestro departamento de HR. Tu misión principal será transformar nuestra cultura organizacional y asegurar que tengamos los mejores procesos de retención de talento femenino.",
        "RESPONSIBILITIES": "<li>Liderar el equipo de reclutamiento y selección con perspectiva de género.</li><li>Desarrollar políticas corporativas inclusivas y protocolos contra el acoso.</li><li>Gestionar programas de bienestar físico y mental para los empleados.</li><li>Medir e implementar estrategias para asegurar brecha salarial cero.</li>",
        "REQUIREMENTS": "<li>Licenciatura en Psicología, Administración o afín.</li><li>Experiencia de 5+ años en puestos gerenciales de Recursos Humanos.</li><li>Diplomados o certificaciones comprobables en Diversidad, Equidad e Inclusión (DEI).</li><li>Excelentes habilidades de negociación y resolución de conflictos.</li>",
        "BENEFITS": "<li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Vales de despensa y fondo de ahorro</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Bonos por cumplimiento de métricas de diversidad</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Seguro de vida y SGMM</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> 20 días de vacaciones desde el primer año</li>"
    },
    {
        "filename": "job-product.html",
        "JOB_TITLE": "Product Manager B2B",
        "COMPANY": "SaaS Innovators",
        "JOB_IMAGE": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1000&q=80",
        "ICON_BG": "bg-yellow-50",
        "ICON_BORDER": "border-yellow-100",
        "ICON_CLASS": "fas fa-box-open",
        "ICON_COLOR": "text-yellow-500",
        "LOCATION": "Remoto (Cualquier lugar)",
        "TYPE": "Tiempo Completo",
        "SALARY": "$4,000 - $6,000 USD/mes",
        "DESCRIPTION": "En SaaS Innovators nos enorgullece contar con un equipo de liderazgo donde el 50% son mujeres. Buscamos a una Product Manager brillante para tomar la propiedad (ownership) de nuestro producto estrella B2B y llevarlo al siguiente nivel de crecimiento.",
        "RESPONSIBILITIES": "<li>Definir la visión, estrategia y el roadmap del producto B2B.</li><li>Trabajar con ingeniería y diseño para el lanzamiento oportuno de features.</li><li>Realizar entrevistas con clientes clave para entender sus dolores y necesidades.</li><li>Analizar datos de uso para iterar y mejorar la adopción del producto.</li>",
        "REQUIREMENTS": "<li>Experiencia mínima de 3 años como Product Manager en SaaS B2B.</li><li>Habilidad fuerte en toma de decisiones basadas en datos (Data-driven).</li><li>Experiencia trabajando con metodologías ágiles (Scrum, Kanban).</li><li>Inglés avanzado fluido (C1/C2).</li>",
        "BENEFITS": "<li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Trabajo remoto desde cualquier parte del mundo</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Acciones de la empresa (Stock Options)</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Presupuesto para conferencias y cursos</li><li><i class='fas fa-check-circle text-brand-500 mr-2'></i> Retiros anuales de la empresa todo pagado</li>"
    }
]


def generate_similar_job_html(job):
    return f'''
        <div class="bg-white rounded-xl shadow-sm p-5 border border-gray-100 hover:shadow-md transition-shadow relative">
            <div class="flex items-start gap-4">
                <div class="w-12 h-12 {job['ICON_BG']} rounded-lg flex items-center justify-center flex-shrink-0 border {job['ICON_BORDER']}">
                    <i class="{job['ICON_CLASS']} text-2xl {job['ICON_COLOR']}"></i>
                </div>
                <div class="flex-1">
                    <h3 class="font-bold text-lg text-gray-900 mb-1"><a href="{job['filename']}" class="hover:text-brand-600 transition-colors">{job['JOB_TITLE']}</a></h3>
                    <p class="text-brand-600 text-sm font-medium mb-3">{job['COMPANY']}</p>
                    <div class="flex flex-wrap gap-2 mb-3">
                        <span class="bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded-md flex items-center gap-1"><i class="fas fa-map-marker-alt"></i> {job['LOCATION'].split('(')[0].strip()}</span>
                    </div>
                    <a href="{job['filename']}" class="text-brand-600 text-sm font-semibold hover:text-brand-800 transition-colors flex items-center">
                        Ver Detalles <i class="fas fa-arrow-right ml-1 text-xs"></i>
                    </a>
                </div>
            </div>
        </div>
    '''

for i, job in enumerate(jobs):
    job_html = template

    # 1. Select 2 similar jobs (just picking the next 2 in the list, wrapping around)
    similar_jobs = []
    idx1 = (i + 1) % len(jobs)
    idx2 = (i + 2) % len(jobs)
    similar_jobs.append(jobs[idx1])
    similar_jobs.append(jobs[idx2])

    similar_html = "".join([generate_similar_job_html(sj) for sj in similar_jobs])

    # 2. Inject properties
    for key, value in job.items():
        if key != "filename":
            job_html = job_html.replace(f"{{{{{key}}}}}", value)

    # 3. Inject similar jobs html
    job_html = job_html.replace("{{SIMILAR_JOBS}}", similar_html)

    with open(job["filename"], "w") as out:
        out.write(job_html)
    print(f"Created {job['filename']}")

print("All job detail pages generated.")
