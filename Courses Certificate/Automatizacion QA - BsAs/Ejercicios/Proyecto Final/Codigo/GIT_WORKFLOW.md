# Gestión de Control de Versiones - Git

## Historial de Commits

El proyecto ha sido organizado mediante commits atómicos que representan unidades lógicas de trabajo:

### Commits realizados:

```bash
# Configuración inicial
- Configuración de dependencias (requirements.txt)
- Configuración de pytest (pytest.ini)
- Definición de archivos a ignorar (.gitignore)

# Implementación de utilidades
- Sistema de logging (utils/logger.py)
- Lector de datos externos (utils/data_reader.py)

# Patrón Page Object Model
- BasePage con métodos reutilizables
- Page Objects: HomePage, ContactoPage, ServiciosPage, ClientesPage, RegisterPage

# Configuración de testing
- Fixtures de pytest (conftest.py)
- Configuración de drivers (desktop/mobile)
- Manejo automático de screenshots

# Datos de prueba
- Parametrización con CSV (test_data/contacto.csv)
- Datos estructurados en JSON (test_data/usuarios.json)

# Implementación de tests
- Tests de API REST (test_api.py)
- Tests de UI: registro, contacto, visualización
- Tests de responsividad móvil

# Documentación
- README.md con instrucciones técnicas
- Reportes HTML generados
```

## Estrategia de Branching

### Flujo de trabajo implementado:

```
main (rama principal)
├── feature/ci-cd-github-actions (integración CI/CD)
└── docs/documentacion-adicional (documentación)
```

### Comandos utilizados:

```bash
# Creación de rama feature
git checkout -b feature/ci-cd-github-actions

# Trabajo en la rama
git add .github/workflows/
git commit -m "feat: agregar GitHub Actions para CI/CD"

# Integración a main
git checkout main
git merge feature/ci-cd-github-actions

# Creación de rama de documentación
git checkout -b docs/documentacion-adicional
git add *.md
git commit -m "docs: agregar guías técnicas"
git checkout main
git merge docs/documentacion-adicional
```

## Convenciones de Mensajes de Commit

### Formato estándar:

```
<tipo>: <descripción corta>

[cuerpo opcional con más detalles]
[referencias a issues si aplica]
```

### Tipos utilizados:

- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de defectos
- `docs:` - Cambios en documentación
- `test:` - Adición o modificación de tests
- `refactor:` - Refactorización sin cambios funcionales
- `chore:` - Tareas de mantenimiento

### Ejemplos reales del proyecto:

```bash
feat: implementar BasePage con Page Object Model
feat: agregar tests de API REST con GET, POST, DELETE
docs: documentación completa del proyecto
test: implementar tests de responsividad desktop/mobile
chore: configuración inicial del proyecto
```

## Comandos Git - Referencia Técnica

### Inspección del repositorio:

```bash
# Ver log completo
git log

# Ver log condensado
git log --oneline

# Ver grafo de branches
git log --graph --oneline --all

# Ver cambios en un archivo
git log -p <archivo>

# Ver commits por autor
git log --author="nombre"
```

### Gestión de branches:

```bash
# Listar branches locales
git branch

# Listar branches remotos
git branch -r

# Crear y cambiar a nueva branch
git checkout -b <nombre-branch>

# Cambiar de branch
git checkout <nombre-branch>

# Eliminar branch local
git branch -d <nombre-branch>

# Forzar eliminación
git branch -D <nombre-branch>
```

### Sincronización con repositorio remoto:

```bash
# Agregar origen remoto
git remote add origin <url>

# Verificar remoto configurado
git remote -v

# Push de branch actual
git push origin <nombre-branch>

# Push de todos los branches
git push --all origin

# Pull desde remoto
git pull origin main

# Fetch sin merge
git fetch origin
```

### Operaciones de staging:

```bash
# Agregar archivos específicos
git add <archivo1> <archivo2>

# Agregar por extensión
git add *.py

# Agregar todo
git add .

# Ver estado
git status

# Ver diferencias
git diff
git diff --staged
```

## Estructura de Branches Profesional

### Modelo GitFlow adaptado:

```
main (producción)
  |
  ├── develop (desarrollo activo)
  |     |
  |     ├── feature/api-tests
  |     ├── feature/ui-automation
  |     └── feature/responsive-testing
  |
  ├── release/v1.0 (preparación release)
  |
  └── hotfix/critical-bug (fixes urgentes)
```

### Aplicación en este proyecto:

```
main
  ├── feature/ci-cd-github-actions (✓ merged)
  └── docs/documentacion-adicional (✓ merged)
```

## Verificación del Historial

Para auditoría del trabajo realizado:

```bash
# Ver todos los commits
git log --oneline --decorate --all

# Ver estadísticas
git log --stat

# Ver cambios por archivo
git log --follow <archivo>

# Ver branches merged
git branch --merged
```

## Buenas Prácticas Aplicadas

1. **Commits atómicos**: Cada commit representa una unidad lógica completa
2. **Mensajes descriptivos**: Siguiendo convención de conventional commits
3. **Branches por feature**: Separación de funcionalidades en desarrollo
4. **Merge controlado**: Integración verificada antes de fusionar a main
5. **Historial limpio**: Sin commits de "WIP" o "fix typo"

## Referencias

- Conventional Commits: https://www.conventionalcommits.org/
- Git Branching Model: https://nvie.com/posts/a-successful-git-branching-model/
- Git Documentation: https://git-scm.com/doc

