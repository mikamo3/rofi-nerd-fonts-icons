from cssutils import parseString
import requests
import re

url = 'https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/css/nerd-fonts-generated.css'
res = requests.get(url)
style = parseString(res.text)
i = 0
for rule in style.cssRules:
    i += 1
    if i == 10:
        break
    if (rule.__class__.__name__ == "CSSStyleRule"):
        match_fc_name = re.match(r'^(\.nf-.*?):before', rule.selectorText)
        if match_fc_name:
            match_fc_content = re.match(
                r'"(.*)"', rule.style.getProperty('content').value)
            if match_fc_content:
                name = match_fc_name.group(1)
                content = match_fc_content.group(1)
                print('<span face=\'Symbols Nerd Font\'>&#x' +
                      repr(content)[3:-1]+'</span> ' + name)
