# ==========================================
# Institutional Trade Engine
# File : health_check.py
# ==========================================

import importlib

REQUIRED_MODULES = [
    "streamlit",
    "pandas",
    "numpy",
    "yfinance",
    "plotly",
    "requests"
]

PROJECT_FILES = [
    "scanner",
    "engine",
    "dashboard",
    "live_data",
    "indicators",
    "validator",
    "paper_trading",
    "risk_manager",
    "portfolio_manager",
    "ai_score_engine"
]


def check_modules():

    missing = []

    for module in REQUIRED_MODULES:

        try:

            importlib.import_module(module)

        except Exception:

            missing.append(module)

    return missing


def check_project():

    failed = []

    for module in PROJECT_FILES:

        try:

            importlib.import_module(module)

        except Exception as e:

            failed.append(
                f"{module} -> {e}"
            )

    return failed


def run_health_check():

    result = {

        "python_packages": check_modules(),

        "project_errors": check_project()

    }

    return result
