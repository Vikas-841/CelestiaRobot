from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "CelestiaXBot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6881733978:AAG0vJjwxCsyKsRzW7-MIPpOprCwGCpQNM8")
OWNER_ID = int(getenv("OWNER_ID", "6280048819"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280048819 6691393517 737932898 6610172048 2072367717").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Celestia:Celestia@celestia.08chke4.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGZtJEArHzih-YBNJUezZo7QVwMpcIOqvmBBxbt7-Wvs8Xog0wBYx1EHoymyBzsq1iolIxvPgONdkCz6DxcpIgaLzUBr1KnlmBWTt4zUq8GG8cDyf9-eLV3u2vgPfOmvXhoKvUVLgAkyU1hVirNYafEKK2gD-GEvbFiFo0Owh3t8mXIXtg5tSdhoBRiLzC5leHtflDGajrImvcwGeD6qEjxGDDA6ALD_sEXVbin6O6DAP80ND2nFVqubjRNZlqWEBu9RzGpgv36UwCWw9k1M33IdwWCPHDwEpGzdlssCS74vBKFW8c6R0OYXIYkx4T7OhR9Dg-fb_4OJi5OL59Eaj2MA5lnbQAAAAFsCkpbAA")

