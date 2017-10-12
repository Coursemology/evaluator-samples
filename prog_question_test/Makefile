prepare:

compile:	tests/autograde.py submission/template.py tests/prepend.py tests/append.py
	cat tests/prepend.py submission/template.py tests/append.py tests/autograde.py > answer.py

public:
	PYTHONPATH="$(shell pwd)/submission":"$(shell pwd)/tests" python3 answer.py ProgQuestionPublic

private:
	PYTHONPATH="$(shell pwd)/submission":"$(shell pwd)/tests" python3 answer.py ProgQuestionPrivate

evaluation:
	PYTHONPATH="$(shell pwd)/submission":"$(shell pwd)/tests" python3 answer.py ProgQuestionEvaluation

clean:
	-rm answer.py
	-rm report.xml
