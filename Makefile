SPHINXOPTS    ?=
PYENV         ?= ~/miniconda3/envs/thynotes
SPHINXBUILD   ?= $(PYENV)/bin/sphinx-build
SOURCEDIR     = .
BUILDDIR      = /tmp/thynotes/$(shell basename $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST)))))

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

show:
	@echo $(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

browse:
	@python -m webbrowser -t "$(BUILDDIR)/html/index.html"

livereload:
	@$(PYENV)/bin/livereload --host 0 --port 65001 $(BUILDDIR)/html/

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(args)
