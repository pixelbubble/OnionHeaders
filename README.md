# OnionHeaders
Simple script to catch the headers of .onion websites.

## Prerequisite

```bash
pip3 install -r requirements.txt
```

## Input
A list of .onion websites (here an example):
```bash
http://hxuzjtocnzvv5g2rtg2bhwkcbupmk7rclb6lly3fo4tvqkk5oyrv3nid.onion/
https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion/
https://www.nytimesn7cgmftshazwhfgzm37qxb44r64ytbb2dj3x62d2lljsciiyd.onion/
```

## Usage
```bash
python3 script.py list_onion.txt
```
![image](https://user-images.githubusercontent.com/75697623/218340100-3e3fafa4-8165-4285-85ba-674407424a78.png)

## Output
```bash
Domain,Title,Statut,Date
http://hxuzjtocnzvv5g2rtg2bhwkcbupmk7rclb6lly3fo4tvqkk5oyrv3nid.onion/,DNMX - Anonymous Email Provider,ONLINE,12/02/2023 23:01:34
https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion/,Facebook - log in or sign up,ONLINE,12/02/2023 23:01:40
https://www.nytimesn7cgmftshazwhfgzm37qxb44r64ytbb2dj3x62d2lljsciiyd.onion/,The New York Times - Breaking News- US News- World News and Videos,ONLINE,12/02/2023 23:01:50
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
