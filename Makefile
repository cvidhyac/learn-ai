# Makefile for learn-ai project
# ================================
# Common tasks for development, testing, and code quality
#
# Usage:
#   make help          Show this help message
#   make setup         Initial project setup (venv + install + pre-commit)
#   make install       Install project dependencies
#   make format        Auto-format code with black and ruff
#   make lint          Run linters (ruff)
#   make type-check    Run type checking (mypy)
#   make check         Run all checks (format + lint + type-check)
#   make test          Run tests with pytest
#   make clean         Remove temporary files and caches
#   make pre-commit    Run pre-commit on all files

# ================================
# Configuration
# ================================
PYTHON := python3
PIP := pip
VENV := .venv
ACTIVATE := . $(VENV)/bin/activate

# Directories
SRC_DIR := practice
TEST_DIR := tests

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m  # No Color

# ================================
# Phony Targets (not actual files)
# ================================
.PHONY: help setup install install-dev clean format lint type-check check test pre-commit all

# ================================
# Default target (runs when you type 'make')
# ================================
.DEFAULT_GOAL := help

# ================================
# Help - Show available commands
# ================================
help:
	@echo "$(BLUE)========================================$(NC)"
	@echo "$(BLUE)  learn-ai Project - Available Commands$(NC)"
	@echo "$(BLUE)========================================$(NC)"
	@echo ""
	@echo "$(GREEN)Setup & Installation:$(NC)"
	@echo "  $(YELLOW)make setup$(NC)         - Complete project setup (first time)"
	@echo "  $(YELLOW)make install$(NC)       - Install runtime dependencies"
	@echo "  $(YELLOW)make install-dev$(NC)   - Install development dependencies"
	@echo ""
	@echo "$(GREEN)Code Quality:$(NC)"
	@echo "  $(YELLOW)make format$(NC)        - Auto-format code (black + ruff)"
	@echo "  $(YELLOW)make lint$(NC)          - Run linters (ruff)"
	@echo "  $(YELLOW)make type-check$(NC)    - Run type checker (mypy)"
	@echo "  $(YELLOW)make check$(NC)         - Run all quality checks"
	@echo "  $(YELLOW)make pre-commit$(NC)    - Run pre-commit hooks on all files"
	@echo ""
	@echo "$(GREEN)Testing:$(NC)"
	@echo "  $(YELLOW)make test$(NC)          - Run tests with coverage"
	@echo ""
	@echo "$(GREEN)Cleanup:$(NC)"
	@echo "  $(YELLOW)make clean$(NC)         - Remove temporary files and caches"
	@echo ""
	@echo "$(GREEN)Shortcuts:$(NC)"
	@echo "  $(YELLOW)make all$(NC)           - Format, lint, type-check, and test"
	@echo ""

# ================================
# Setup - Initial project setup
# ================================
setup:
	@echo "$(BLUE)Setting up project...$(NC)"
	@if [ ! -d "$(VENV)" ]; then \
		echo "$(YELLOW)Creating virtual environment...$(NC)"; \
		$(PYTHON) -m venv $(VENV); \
	else \
		echo "$(GREEN)Virtual environment already exists.$(NC)"; \
	fi
	@echo "$(YELLOW)Installing dependencies...$(NC)"
	@$(ACTIVATE) && $(PIP) install --upgrade pip
	@$(ACTIVATE) && $(PIP) install -e ".[dev]"
	@echo "$(YELLOW)Installing pre-commit hooks...$(NC)"
	@$(ACTIVATE) && pre-commit install
	@echo "$(GREEN)✓ Setup complete!$(NC)"
	@echo "$(BLUE)Activate venv with: source $(VENV)/bin/activate$(NC)"

# ================================
# Install - Install dependencies
# ================================
install:
	@echo "$(YELLOW)Installing runtime dependencies...$(NC)"
	@$(ACTIVATE) && $(PIP) install -e .
	@echo "$(GREEN)✓ Runtime dependencies installed$(NC)"

install-dev:
	@echo "$(YELLOW)Installing development dependencies...$(NC)"
	@$(ACTIVATE) && $(PIP) install -e ".[dev]"
	@echo "$(GREEN)✓ Development dependencies installed$(NC)"

# ================================
# Code Quality - Formatting
# ================================
format:
	@echo "$(BLUE)Formatting code...$(NC)"
	@echo "$(YELLOW)Running black...$(NC)"
	@$(ACTIVATE) && black $(SRC_DIR)
	@echo "$(YELLOW)Running ruff (import sorting and fixes)...$(NC)"
	@$(ACTIVATE) && ruff check $(SRC_DIR) --fix
	@echo "$(GREEN)✓ Code formatted$(NC)"

# ================================
# Code Quality - Linting
# ================================
lint:
	@echo "$(BLUE)Linting code...$(NC)"
	@$(ACTIVATE) && ruff check $(SRC_DIR)
	@echo "$(GREEN)✓ Linting complete$(NC)"

# ================================
# Code Quality - Type Checking
# ================================
type-check:
	@echo "$(BLUE)Type checking...$(NC)"
	@$(ACTIVATE) && mypy $(SRC_DIR)
	@echo "$(GREEN)✓ Type checking complete$(NC)"

# ================================
# Code Quality - Run all checks
# ================================
check: format lint type-check
	@echo "$(GREEN)✓ All checks passed!$(NC)"

# ================================
# Testing - Run pytest with coverage
# ================================
test:
	@echo "$(BLUE)Running tests...$(NC)"
	@if [ -d "$(TEST_DIR)" ]; then \
		$(ACTIVATE) && pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=term-missing --verbose; \
	else \
		echo "$(YELLOW)No tests directory found. Skipping tests.$(NC)"; \
	fi

# ================================
# Pre-commit - Run hooks on all files
# ================================
pre-commit:
	@echo "$(BLUE)Running pre-commit on all files...$(NC)"
	@$(ACTIVATE) && pre-commit run --all-files
	@echo "$(GREEN)✓ Pre-commit complete$(NC)"

# ================================
# Clean - Remove temporary files
# ================================
clean:
	@echo "$(BLUE)Cleaning temporary files...$(NC)"
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name ".coverage" -delete 2>/dev/null || true
	@find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN)✓ Cleanup complete$(NC)"

# ================================
# All - Run format, lint, type-check, test
# ================================
all: format lint type-check test
	@echo "$(GREEN)✓ All tasks complete!$(NC)"
