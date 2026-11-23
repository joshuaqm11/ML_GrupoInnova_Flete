# Flujo de trabajo del equipo

## Git

1. `git pull origin main` antes de empezar.
2. Crear rama: `git checkout -b feature/<nombre>-<tarea>` (ej. `feature/fernanda-eda`).
3. Trabajar **solo en tu notebook**. Si necesitás cambiar algo de `src/`, avisá en el grupo primero.
4. Antes de commitear: *Kernel → Restart & Run All* (el notebook debe correr de inicio a fin).
5. Commits pequeños y en español: `git commit -m "EDA: tratamiento de nulos con justificación"`.
6. `git push -u origin feature/...` y abrir **Pull Request** a `main`. Joshua revisa y fusiona.
7. Mover la tarjeta en Trello: Pendiente → En progreso → En revisión (PR abierto) → Hecho (PR fusionado).

> La rúbrica de participación revisa que **todos** tengan commits. Hacé commits seguido, no uno solo al final.

## Reglas técnicas (no negociables)

- Semilla: siempre `config.RANDOM_STATE` (42). Split: siempre `dividir_train_test(df)`.
- Nada de `fit` sobre Test. Imputar/escalar/codificar solo dentro de un `Pipeline`.
- Toda métrica final se registra con `registrar_metricas(...)` para que la tabla del notebook 05 salga sola.
- Cada decisión se justifica en una celda Markdown: qué, por qué y qué alternativa se descartó.

## Defensa

La nota es **individual**: cualquier integrante puede ser preguntado sobre cualquier parte. Cada uno expone lo suyo, pero todos leen y entienden los 7 notebooks antes del ensayo.
