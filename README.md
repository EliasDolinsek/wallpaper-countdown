# wallpaper-countdown

wallpaper-countdown is a python script to display a countdown as desktop wallpaper for windows.

<a href="https://ibb.co/pLH137Q"><img src="https://i.ibb.co/pLH137Q/wallpaper.png" alt="wallpaper" border="0"></a>

## Installation

Download all files of the repository.

To install all required dependencies run the following command.

```commandline
pip install -r requirements.txt
```

## Usage

To run the script execute the following command.

```commandline
python3 wallpaper_countdown.py
```

### Change countdown date

To change the countdown date, set the `countdown_datetime` variable to your desired datetime.

```python
countdown_datetime = datetime.datetime(2021, 12, 12, hour=12, minute=15)
```

### Change event name

To change the event name, set the `event_name` variable to your desired name.

```python
event_name = "Countdown event"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
