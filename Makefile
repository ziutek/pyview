gae:
	python examples/web/template.py --compile templates

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	rm -f examples/templates/__init__.py


.PHONY : clean
