init:
	python setup.py develop
	pip install -r requirements.txt

test:
	nosetests tests/test_bitcoins.py

bitpy:
	rm -fr bitcoins/packages/bitcoinrpc
	git clone https://github.com/laanwj/bitcoin-python.git
	cd bitcoin-python && git checkout master && cd ..
	mv bitcoin-python/src/bitcoinrpc bitcoins/packages/
	rm -fr bitcoin-python
