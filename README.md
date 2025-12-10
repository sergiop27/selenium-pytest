## 🧪 Curso Introductorio de Testing con Selenium + Python

¡Bienvenido al repositorio oficial del **Curso Introductorio de Testing Automatizado con Python**!  

En este proyecto vas a aprender a construir un framework de pruebas combinando:
* Selenium WebDriver + Pytest para pruebas de Front/UI
* Requests + Pytest para pruebas de API/Backend
* Page Object Model (POM)
* Datos parametrizados en JSON
* Reportes HTML
* Evidencias automáticas (screenshots)

---

### 🚀 ¿Qué contiene este proyecto?

✔ Pruebas automatizadas de Frontend con Selenium
✔ Pruebas de Backend / API con Requests
✔ Uso de fixtures, POM, marcadores y parametrización
✔ Generación automática de screenshots en cada test
✔ Generación de reporte HTML con detalles de ejecución
✔ Buenas prácticas de estructura, claridad y escalabilidad

---

### 📂 Estructura inicial del proyecto

```text
selenium-pytest/
├── api/
│   └── api_client.py
│
├── data/
│   └── data_login.json            # Datos parametrizados
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── front/
│   │   ├── login_test.py
│   │   ├── products_test.py
│   │   ├── checkout_test.py
│   │   └── conftest.py            # driver_setup + screenshots
│   │
│   └── back/
│       └── getApi_test.py
│
├── screenshots/                   # Evidencias automáticas (ignorada en .gitignore)
├── reports/                       # Reportes HTML (ignorados)
│
├── requirements.txt
├── .gitignore
└── README.md
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

## 🎯 Ejecutar por separado: Frontend vs Backend

Gracias a los markers (@pytest.mark.front y @pytest.mark.back) podés ejecutar por tipo de test.

5. Ejecutar solo pruebas Front/UI:
   ```bash
   py -m pytest -m front -v
   ```

6. Ejecutar solo pruebas Back/API
   ```bash
   py -m pytest -m back -v
   ```

---

### ✨ Autor
Ing. Sergio Pace
QA Automation Technical Lead & Instructor

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sígueme-blue)](https://www.linkedin.com/in/pace-sergio/)

---

Nota: Este repositorio está diseñado para fines educativos como parte del Curso Introductorio de Testing Automatizado. Cada commit documenta la evolución del proyecto para que puedas seguir su crecimiento desde un simple script hasta un framework profesional.
