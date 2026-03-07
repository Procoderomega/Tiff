import tomllib


#* Here we load the config.toml File 🤔 ig...
with open("config.toml","rb") as f:
    config = tomllib.load(f)