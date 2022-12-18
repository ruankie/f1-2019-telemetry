
# F1 2019 UDP Telemetry

> Forked form [this GitLab repo](https://gitlab.com/reddish/f1-2019-telemetry) <br>
> Original development by [Sidney Cadot](https://gitlab.com/reddish)

The f1-2019-telemetry package provides support for interpreting telemetry information as sent out over the network by [the F1 2019 game by CodeMasters](http://www.codemasters.com/game/f1-2019/).
It also provides command-line tools to record, playback, and monitor F1 2019 session data.

## Usage
### Setup
1. Clone this repo
2. Set up a separate conda environment and activate it by running:
    ```bash
    conda env create -f conda.yml
    conda activate f1-2019
    ```

### Recording UDP packets and saving to SQL database
> This section uses the f1-2019-telemetry CLI as describe in the [documentation](https://f1-2019-telemetry.readthedocs.io/en/latest/package-documentation.html#f1-2019-telemetry-recorder-script)
1. Launch the F1 2019 game
2. Run the following command from the `f1` conda environment (created in the setup above)
    > `-p` is the UDP port to listen to (default: 20777) <br>
    > `-i` is the interval for writing incoming data to SQLite3 file, in seconds (default: 1.0)
    ```bash
    f1-2019-telemetry-recorder -p 20777 -i 1.0
    ```


## References

- The original project was developed by [Sidney Cadot](https://gitlab.com/reddish) and is hosted in [this GitLab repo](https://gitlab.com/reddish/f1-2019-telemetry)

- The original `f1-2019-telemetry` is hosted on [PyPI](https://pypi.org/project/f1-2019-telemetry/)

- The original package documentation is hosted on [Read the Docs](https://f1-2019-telemetry.readthedocs.io/en/latest/)
