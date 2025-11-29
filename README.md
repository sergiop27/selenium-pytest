## 🧪 Curso Introductorio de Testing con Selenium + Python

¡Bienvenido al repositorio oficial del **Curso Introductorio de Testing Automatizado con Python**!  

Aquí vas a aprender paso a paso cómo construir un **framework de pruebas desde cero** usando **Selenium WebDriver + Pytest**, 
comenzando con un **primer test funcional de Front** y luego evolucionando el proyecto con **buenas prácticas**, 
**patrones simples** y, más adelante, **pruebas de API**.

En esta **primera etapa** vas a encontrar un **script sencillo de prueba** que nos servirá como base inicial.  
En los **próximos commits**, iremos haciendo crecer el proyecto y también este **README**, incorporando más explicaciones y 
funcionalidades.

---

### 🚀 ¿Qué contiene este proyecto?

- **Lenguaje:** Python 3.x  
- **Framework de pruebas:** Pytest  
- **Automatización UI:** Selenium WebDriver  
- **Primer caso:** Login básico sobre una página pública de ejemplo (definida en el primer test)

Más adelante sumaremos:

- Pruebas de **API** usando `requests` + Pytest  
- Mejores prácticas para organizar UI + API en el mismo repo

---

### 📂 Estructura inicial del proyecto

```text
selenium-pytest/
├── tests/
│   └── test_login.py     # Primer test básico de interfaz
├── requirements.txt         # Dependencias del proyecto (pytest, selenium, etc.)
├── .gitignore               # Ignora archivos innecesarios (venv, __pycache__, etc.)
└── README.md                # Bienvenida y guía del curso
```

---

### ▶️ ¿Cómo ejecutar?
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/selenium-pytest.git
   ```

2. Navegar al proyecto:
   ```bash
   cd selenium-pytest
   ```

3. Instalar dependencias:
   ```bash
   py -m pip install -r requirements.txt
   ```

4. Ejecutar los tests con Pytest:
   ```bash
   py -m pytest -v
   ```

---

### ✨ Autor
Ing. Sergio Pace
QA Automation Technical Lead & Instructor

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sígueme-blue)](https://www.linkedin.com/in/pace-sergio/)

---

Nota: Este repositorio está diseñado para fines educativos como parte del Curso Introductorio de Testing Automatizado. Cada commit documenta la evolución del proyecto para que puedas seguir su crecimiento desde un simple script hasta un framework profesional.
