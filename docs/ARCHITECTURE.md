# Project Architecture

### Current Architecture (v0.6.0)
The project now uses dataclass-based models to transfer structured data between application layers instead of dictionaries.

~~~
analyzer.py
│
├── File Loading
├── Log Parsing
├── Log Analysis
└── Report Output
~~~

---

Next Sprint(v0.5.0)

~~~
main.py
│
├── parser.py
│      │
│      ▼
│   models.py
│
└── report.py
~~~

Goal:

- Modular architecture
- Better maintainability
- Easier testing
- Separation of concerns