@echo off
title Sistema de Cadastro de Produtos - Alves
color 0F

echo.
echo ========================================================
echo        SISTEMA DE CADASTRO DE PRODUTOS
echo ========================================================
echo.

:: Verifica Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado.
    echo Instale o Python e adicione ao PATH.
    pause
    exit
)

:: Instala biblioteca se necessario (silencioso)
echo Verificando dependencias...
pip install mysql-connector-python --quiet >nul 2>&1

echo Dependencias a serem instaladas.
echo.

:: MySQL - apenas tenta iniciar se necessario
echo Verificando MySQL...
net start MySQL >nul 2>&1
if %errorlevel% neq 0 (
    echo Se houver algum problema avise ao Diogo. 
    echo Isso deve iniciar automaticamente se fizer o passo a passo.
   
)



python main.py

echo.
echo ========================================================
echo Programa finalizado.
pause