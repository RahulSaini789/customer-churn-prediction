"""
customer_churn_prediction.config
--------------------------------

Centralized configuration file for directory paths, constants, and project-level settings.

This module defines standardized paths (for data, models, reports, etc.)
so every script and notebook in the repository can import from a single place
without hardcoding file locations.

Example:
    from customer_churn_prediction.config import PROCESSED_DIR, RANDOM_STATE

Usage:
    - Store all directory constants here.
    - Avoid using absolute paths in scripts.
    - Keep this file lightweight and environment-agnostic.
"""

from pathlib import Path

# Project root (auto-detects one level above this file)
ROOT = Path(__file__).resolve().parents[1]

# ========================
# Directory Configuration
# ========================
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

REPORTS_DIR = ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

MODELS_DIR = ROOT / "models"

# ========================
# File Paths
# ========================
RAW_FILE = RAW_DIR / "telco_churn.csv"
PROCESSED_FILE = PROCESSED_DIR / "telco_churn_cleaned.csv"

# ========================
# Global Constants
# ========================
RANDOM_STATE = 42
TEST_SIZE = 0.2

# ========================
# Utility: Path Validation
# ========================
if __name__ == "__main__":
    print(f"ROOT: {ROOT}")
    print(f"RAW FILE EXISTS: {RAW_FILE.exists()}")
    print(f"PROCESSED DIR: {PROCESSED_DIR}")
