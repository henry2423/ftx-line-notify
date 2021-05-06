# ftx-api

## Description
透過 Line Notify 獲得每日期現套利收益報告，每小時提供當一小時獲利，每天UTC 00:00提供前一天獲利，效果如下圖。

![image](https://github.com/maya142857/ftx-line-notify/blob/main/.img/per-day.png)

## 使用說明

### All you have to prepare:
1. [Line Notify API Key](https://notify-bot.line.me/zh_TW/)：到網站申請一組API_KEY，並連結到你要接收通知的聊天室
2. [FTX API Key](https://ftx.com/profile)：需要一組能夠讀取到套利子帳戶的API KEY，唯獨權限即可。

### One Click Deployment with Heroku
1. Click the `Deploy to Heroku` button.
<a href="https://www.heroku.com/deploy/?template=https://github.com/henry2423/ftx-line-notify/tree/docker">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
2. You will see a Create New App page
2. Decide your App name, can be anything, just to be unique.
3. Type in FYX api key, secret and the subaccount you want to monitor.
4. Type in Line api key.
5. Hit the `Deploy app` button and wait for few minutes.

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

### Contribution
- [maya142857/ftx-line-notify](https://github.com/maya142857/ftx-line-notify)
