# rpi-gpio-video
Play a video on the Raspberry Pi based on its GPIO inputs

## Dependencies

```
sudo apt-get install python-rpi.gpio python3-rpi.gpio
```

## Install

Exampmle systemd service unit assumes the default user `pi` is used and the repo is located at `/home/pi`.

```
git clone https://github.com/scsole/rpi-gpio-video.git
cd rpi-gpio-video
sudo cp gpio-video.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable --now gpio-video.service
```