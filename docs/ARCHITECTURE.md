# Project Architecture

Current Architecture

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
├── analyzer.py
└── report.py
~~~

Goal:

- Modular architecture
- Better maintainability
- Easier testing
- Separation of concerns