MAINFILE = mcp2210_test
APIFILE = mcp2210_api
EXEC_NAME = sample_code_demo

Rule:
		gcc $(MAINFILE).c $(APIFILE).c -o $(EXEC_NAME) -Wall
		./getDev.sh
		# $(EXEC_NAME)
		
.PHONY: clean
clean:
	rm $(EXEC_NAME) 
