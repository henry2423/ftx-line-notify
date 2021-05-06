# ftx funding payments collection bot

## Description
Get your ftx funding payments information and send you through Line Notify bot. You will have your funding payment info hourly and daily summary.

![image](https://github.com/henry2423/ftx-line-notify/blob/docker/.img/line.jpg)

### All you have to prepare:
1. [Line Notify API Key](https://notify-bot.line.me/zh_TW/)：到網站申請一組API_KEY，並連結到你要接收通知的聊天室 (在[這裡](https://notify-bot.line.me/my/)產生你的API Token)
2. [FTX API Key](https://ftx.com/profile)：需要一組能夠讀取到套利子帳戶的API KEY，唯獨權限即可。
3. [Heroku Account](https://signup.heroku.com/login)：創建一個 Heroku 帳號來 host自己的 bot

### One Click Deployment with Heroku
<a href="https://www.heroku.com/deploy/?template=https://github.com/henry2423/ftx-line-notify/tree/heroku">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

1. Click the `Deploy to Heroku` button.
2. You will see a Create New App page.
![image](https://github.com/henry2423/ftx-line-notify/blob/docker/.img/start-deploy.png)
3. Decide your App name, can be anything, just to be unique.
4. Type in FYX api key, secret and the subaccount you want to monitor.
5. Type in Line api key.
![image](https://github.com/henry2423/ftx-line-notify/blob/docker/.img/parameter-setup.png)
7. Hit the `Deploy app` button, should see the green check if deploy succeed.
![image](https://github.com/henry2423/ftx-line-notify/blob/docker/.img/deploy-finish.png)
8. Go to `Manage App` -> `Resource` -> Enable the Free Dynos manually.
![image](https://github.com/henry2423/ftx-line-notify/blob/docker/.img/enable-cron.png)

--- 
### Run the Docker image manually
1. Install [Docker](https://docs.docker.com/engine/install/).
2. Pull the docker image from [Docker Hub](https://hub.docker.com/repository/docker/henry2423/ftx-line-notify).
```
$ docker pull henry2423/ftx-line-notify:latest
```
3. Run the image with the following command
```
$ docker run \
-e line_api_key='your_line_api_key' \
-e ftx_api_key='your_ftx_api_key' \
-e ftx_api_secret='your_ftx_api_secret' \
-e ftx_sub_account='your_ftx_sub_account' \
-d henry2423/ftx-line-notify:latest
```
4. The bot will be triggered automatically based on the `cronjobs` file settings.

### Contribution
- [maya142857/ftx-line-notify](https://github.com/maya142857/ftx-line-notify)
