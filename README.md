# Steam sales scrapper 👾
Created date: 2023-11-04
Author: Michał Przyłucki

# About 😆
Small project to get list of discounted 🤑 games on Steam. 
I have to use STEAM API, instead of this (look at #TODO). This is just way to list
✍🏻 games from steam that are discounted. I try to look at it everyday, so I realized 
I can easily automate this 🤯. Whole project took about 1h, maybe 1,5h.

# TODO 🤔
- [ ] All it does right now is making a get request for `http://store.steampowered.com/api/featuredcategories/?l=polish`. I just found that in 30 secs, but I should reconsider using
STEAM API to provide much more functionality. That's just small prototype. 👨‍💻

# Example output

```
==============================================
|              NAME              |   PRICE   |
==============================================
| Red Dead Redemption 2          |  99,96 zł |
| Cyberpunk 2077                 | 119,40 zł |
| Anno 1800                      |  62,47 zł |
| Detroit: Become Human          |  55,60 zł |
| Sniper Elite 5                 |  53,99 zł |
| Mass Effect™ Edycja legendarna |  43,18 zł |
| Dying Light 2 Stay Human       |  99,99 zł |
| Deep Rock Galactic             |  35,63 zł |
| Sniper Elite 4                 |  21,49 zł |
| DayZ                           |  97,19 zł |
==============================================
```

## How to start?

1. Clone repo.
2. Create venv, for example `python -m venv venv`.
3. Activate the repo, for venv (on linux) it's `source venv/Scripts/activate`.
4. Install all requirements with pip: `pip install -r requirements.txt`
5. Run script by typing in terminal `python scraper.py`.
6. Wait until everything is done.
