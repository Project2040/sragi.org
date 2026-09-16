# ===========================================================
#  SRAGI Makefile - SSOT Utilities
#  Author: Rune Solberg / Neptunia Media AS
#  License: CC-BY-4.0
# ===========================================================

PYTHON := python3
SSOT_SCRIPT := tools/enforce_version_refs.py

.PHONY: all check-ssot check-license build-license clean-versions

# Default target
all: check-ssot check-license

## 🧭 Run SSOT compliance check
check-ssot:
	@echo "🔍 Running SRAGI SSOT enforcement..."
	@$(PYTHON) $(SSOT_SCRIPT)

check-license:
	@$(PYTHON) automation/license_builder/build_licenses.py --check
	@$(PYTHON) -m unittest discover -s tests

build-license:
	@$(PYTHON) automation/license_builder/build_licenses.py

## Compatibility alias: validation never silently rewrites artifact rights.
clean-versions:
	@$(PYTHON) $(SSOT_SCRIPT)
