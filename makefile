# ===========================================================
#  SRAGI Makefile - SSOT Utilities
#  Author: Rune Solberg / Neptunia Media AS
#  License: CC BY 4.0 via SRL
# ===========================================================

PYTHON := python3
SSOT_SCRIPT := tools/enforce_version_refs.py

.PHONY: all check-ssot clean-versions

# Default target
all: check-ssot

## 🧭 Run SSOT compliance check
check-ssot:
	@echo "🔍 Running SRAGI SSOT enforcement..."
	@$(PYTHON) $(SSOT_SCRIPT)

## ♻️ Clean and normalize all SRL version references
clean-versions:
	@echo "🧹 Cleaning version references..."
	@$(PYTHON) $(SSOT_SCRIPT) || true
	@echo "✅ Cleanup complete. Run 'make check-ssot' to verify."
