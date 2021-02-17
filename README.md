# Description
URL Decoder is the simple tool for decoding URLs. Get started by typing or pasting a URL encoded string in the input CLI, the tool will decode your input string in real time.  
# Usage
$ git clone https://github.com/mer1-97/urldecoder.git

$ cd urldecoder

$ python urldecoder.py [-h] or [-c] "string"

ex)
python urldecoder.py "https://www.google.com/search?q=%ED%85%8C%EC%8A%A4%ED%8A%B8&oq=%ED%85%8C%EC%8A%A4%ED%8A%B8&aqs=chrome..69i57j69i61l2.1117j0j7&sourceid=chrome&ie=UTF-8"

Result =>
https://www.google.com/search?q=테스트&oq=테스트&aqs=chrome..69i57j69i61l2.1117j0j7&sourceid=chrome&ie=UTF-8

# Options
    -h      Print this help
    -c      Decode the string, copy to clipboard
