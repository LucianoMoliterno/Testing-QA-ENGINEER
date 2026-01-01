#!/bin/bash
# Script de Verificación Local antes de Push a GitHub
# Autor: Luciano Moliterno
# Simula lo que hará el pipeline de CI/CD

echo "========================================================================"
echo "🔍 VERIFICACIÓN LOCAL DEL FRAMEWORK"
echo "Simulando pipeline CI/CD antes de push a GitHub"
echo "========================================================================"
echo ""

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Contador de errores
ERRORS=0

# 1. Verificar que Python está instalado
echo "📍 [1/7] Verificando Python..."
if command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version)
    echo -e "${GREEN}✓${NC} Python encontrado: $PYTHON_VERSION"
else
    echo -e "${RED}✗${NC} Python no encontrado"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 2. Verificar dependencias
echo "📍 [2/7] Verificando dependencias..."
if pip show pytest > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} pytest instalado"
else
    echo -e "${RED}✗${NC} pytest no instalado - ejecuta: pip install -r requirements.txt"
    ERRORS=$((ERRORS + 1))
fi

if pip show behave > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} behave instalado"
else
    echo -e "${RED}✗${NC} behave no instalado - ejecuta: pip install -r requirements.txt"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 3. Verificar estructura de archivos
echo "📍 [3/7] Verificando estructura de archivos..."
REQUIRED_FILES=(
    ".github/workflows/ci.yml"
    "conftest.py"
    "pytest.ini"
    "requirements.txt"
    "features/login.feature"
    "features/cart.feature"
    "features/environment.py"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file existe"
    else
        echo -e "${RED}✗${NC} $file NO encontrado"
        ERRORS=$((ERRORS + 1))
    fi
done
echo ""

# 4. Ejecutar Tests Smoke (CRÍTICO)
echo "📍 [4/7] Ejecutando Tests @smoke (CRÍTICOS)..."
echo "========================================================================"
pytest -m smoke -v --tb=short
SMOKE_EXIT=$?
if [ $SMOKE_EXIT -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Tests smoke pasaron exitosamente"
else
    echo -e "${RED}✗${NC} Tests smoke FALLARON - El pipeline CI/CD fallará"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 5. Verificar sintaxis BDD
echo "📍 [5/7] Verificando features BDD..."
behave --dry-run > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Features BDD tienen sintaxis correcta"
else
    echo -e "${YELLOW}⚠${NC} Advertencia en features BDD"
fi
echo ""

# 6. Ejecutar Tests API (opcional pero recomendado)
echo "📍 [6/7] Ejecutando Tests API..."
pytest test_api/test_post_lifecycle.py::test_post_lifecycle -v --tb=short
API_EXIT=$?
if [ $API_EXIT -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Test E2E de API pasó exitosamente"
else
    echo -e "${YELLOW}⚠${NC} Test E2E de API falló (no crítico para CI)"
fi
echo ""

# 7. Resumen final
echo "========================================================================"
echo "📊 RESUMEN DE VERIFICACIÓN"
echo "========================================================================"
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✓ Todas las verificaciones pasaron${NC}"
    echo ""
    echo "✅ Tu código está listo para push a GitHub"
    echo "✅ El pipeline CI/CD debería pasar exitosamente"
    echo ""
    echo "Próximos pasos:"
    echo "  1. git add ."
    echo "  2. git commit -m 'Update: CI/CD pipeline configured'"
    echo "  3. git push origin main"
    echo ""
    exit 0
else
    echo -e "${RED}✗ Se encontraron $ERRORS error(es)${NC}"
    echo ""
    echo "❌ Corrige los errores antes de hacer push"
    echo "❌ El pipeline CI/CD fallará con estos errores"
    echo ""
    exit 1
fi

