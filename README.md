[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# instagram-comment-scrapper

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/GA-U-u2bsAApmn9.jpeg)
Get all comments from instagram post url or id

## Requirements

- **Python >= 3.11.4**
- **Requests >= 2.31.0**

## Installation

```sh
# Clonig Repository
git clone https://github.com/romysaputrasihananda/instagram-comment-scrapper

# Change Directory
cd instagram-comment-scrapper

# Install Requirement
pip install -r requirements.txt
```

## Example Usages

```sh
python main.py --url=7170139292767882522 --output=data
```

### Flags

| Flag     | Alias |            Description            | Example         |       Default       |
| :------- | :---: | :-------------------------------: | :-------------- | :-----------------: |
| --url    |  -u   | Url or post id of instagram video | --url=id or url | 7170139292767882522 |
| --cookie |  -c   |     yout cookie of instagram      | --cookie=cookie |        None         |
| --output |  -o   |       json file output path       | --output=data   |        data         |

## Sample Output

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/Screenshot_20231211_001804.png)

```json
{
  "username": "_____mfr.py",
  "full_name": "-- ..- .... ..-. .- .-.. .. .... .-.",
  "caption": "🗿",
  "date_now": "2024-01-01T01:14:47",
  "create_at": "2023-01-01T06:23:25",
  "post_url": "https://instagram.com/p/Cm2cJmABD1p",
  "comments": [
    {
      "username": "wq_ddisaaa",
      "full_name": "disa",
      "comment": "Hengker😮😮",
      "create_time": "2023-10-04T07:58:57",
      "avatar": "https://scontent-cgk1-1.cdninstagram.com/v/t51.2885-19/394723348_859645495542180_5183735561136891809_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-cgk1-1.cdninstagram.com&_nc_cat=100&_nc_ohc=DPwcwLcPlpoAX8KY_65&edm=AId3EpQBAAAA&ccb=7-5&oh=00_AfBs7rlnJfRuModR3l0VN1740TEqo9C5rAAbnG96EHh2HQ&oe=6595D8CB&_nc_sid=f5838a",
      "total_like": 0,
      "total_reply": 0,
      "replies": []
    },
    {
      "username": "ariiiyogaaa.p",
      "full_name": "Ariii",
      "comment": "Ngeriii",
      "create_time": "2023-01-04T18:16:46",
      "avatar": "https://scontent-cgk1-1.cdninstagram.com/v/t51.2885-19/397920871_788933773000237_982373528353592889_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-cgk1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=RN-d5uNobBQAX_qYk5o&edm=AId3EpQBAAAA&ccb=7-5&oh=00_AfAkXsVm97JhEfnbIKqI3EARWyZ2Y4EzeoYa3pNS0It_og&oe=65969964&_nc_sid=f5838a",
      "total_like": 0,
      "total_reply": 1,
      "replies": [
        {
          "username": "_____mfr.py",
          "full_name": "-- ..- .... ..-. .- .-.. .. .... .-.",
          "comment": "@yogxzyy_ folbek Ra awokawok",
          "create_time": "2023-01-04T19:29:51",
          "avatar": "https://scontent-cgk1-1.cdninstagram.com/v/t51.2885-19/382939904_1057120308617315_8576025359738875373_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-cgk1-1.cdninstagram.com&_nc_cat=111&_nc_ohc=Wg2QEvb_M_cAX8g3kpJ&edm=AFDWGO4BAAAA&ccb=7-5&oh=00_AfCgcfYNq5GQO_pW2uJtZLzl1MMW3klwI4zJoUblyQ98vw&oe=6596FC3D&_nc_sid=7b9ede",
          "total_like": 0
        }
      ]
    },
    {
      "username": "romys.12",
      "full_name": "",
      "comment": "Sheesshhhh 🥶🥶",
      "create_time": "2023-01-01T14:25:26",
      "avatar": "https://scontent-cgk1-1.cdninstagram.com/v/t51.2885-19/175528500_943726476461534_7522721559249567006_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-cgk1-1.cdninstagram.com&_nc_cat=102&_nc_ohc=P7LarmY630YAX-6KJ9D&edm=AId3EpQBAAAA&ccb=7-5&oh=00_AfDqj5SFEuj7f6iCwR_vPMqFh997_YnK2PWdRxyp219_yw&oe=65972FB3&_nc_sid=f5838a",
      "total_like": 2,
      "total_reply": 0,
      "replies": []
    }
  ]
}
```

## License

This project is licensed under the [MIT License](LICENSE).
