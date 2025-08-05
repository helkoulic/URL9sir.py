# URL9sir.py
##### A URL shortener written in python!


### Installation:

1. Clone the repository:
```
git clone https://github.com/helkoulic/URL9sir.py.git
```

2. Move to the URL9sir.py directory:
```
cd URL9sir.py
```

3. Install the requirements:
```
pip install -r requirements.txt
```

4. Run the script:
```
python3 URL9sir.py -help
```

### Usage:

- To get a short link, pass the website link as an argument
```
python3 URL9sir.py https://example.com
```

- To get short links of more than one website
```
python3 URL9sir.py example.com  google.com colixtrans.web.app
```

- In case the given website is down, URL9sir.py doesn't spawn the shorten links, to force it to do that add the --force argument before the URLs
```
python3 URL9sir.py --force example.com  google.com colixtrans.web.app
```

- You can choose the URL shortener service and save the output by following along with the given prompts.

### Use cases:

##
