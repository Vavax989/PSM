# A structured library of Emergency Response: Liberty County (ERLC) Private Server Admin Commands
ERLC_PRIVATE_SERVER_COMMANDS = {
    # Server Owner Commands
    "Server Owner Commands": {
        ":admin": {
            "description": "Grants admin privileges to a player.",
            "example": ":admin PlayerName",
            "arguments": "[Player/UserId]",
        },
        ":unadmin": {
            "description": "Removes admin privileges from a player.",
            "example": ":unadmin PlayerName",
            "arguments": "[Player/UserId]",
        },
    },

    # Server Admin Commands
    "Server Admin Commands": {
        ":helper": {
            "description": "Grants helper privileges to a player.",
            "example": ":helper PlayerName",
            "arguments": "[Player/UserId]",
        },
        ":unhelper": {
            "description": "Removes helper privileges from a player.",
            "example": ":unhelper PlayerName",
            "arguments": "[Player/UserId]",
        },
        ":mod": {
            "description": "Grants moderator privileges to a player.",
            "example": ":mod PlayerName",
            "arguments": "[Player/UserId]",
        },
        ":unmod": {
            "description": "Removes moderator privileges from a player.",
            "example": ":unmod PlayerName",
            "arguments": "[Player/UserId]",
        },
        ":ban": {
            "description": "Bans a player from the server.",
            "example": ":ban PlayerName",
            "arguments": "[Player/UserId]",
        },
        ":unban": {
            "description": "Unbans a player.",
            "example": ":unban PlayerName",
            "arguments": "[String: Player/UserId]",
        },
        ":weather": {
            "description": "Changes the server weather.",
            "example": ":weather clear",
            "arguments": "[String: clear/rain/fog/snow]",
        },
        ":kick": {
            "description": "Kicks a player from the server.",
            "example": ":kick PlayerName",
            "arguments": "[Player]",
        },
        ":logs": {
            "description": "Displays the server logs.",
            "example": ":logs",
            "arguments": "None",
        },
    },

    # Server Moderator Commands
    "Server Moderator Commands": {
        ":toatv": {
            "description": "Teleports to the ATV location.",
            "example": ":toatv",
            "arguments": "None",
        },
        ":log": {
            "description": "Logs a specific string in the server.",
            "example": ":log Server restarted",
            "arguments": "[String]",
        },
    },

    # Gameplay Commands
    "Gameplay Commands": {
        ":killlogs": {
            "description": "Kills a player (Alias: :down).",
            "example": ":killlogs PlayerName",
            "arguments": "[Player]",
        },
        ":h": {
            "description": "Sends a server-wide message.",
            "example": ":h Hello everyone!",
            "arguments": "[String]",
        },
        ":m": {
            "description": "Sends a private message to a player.",
            "example": ":m PlayerName Hello!",
            "arguments": "[String]",
        },
        ":tp": {
            "description": "Teleports one player to another.",
            "example": ":tp Player1 Player2",
            "arguments": "[Player] [Player]",
        },
        ":bring": {
            "description": "Brings a player to your location.",
            "example": ":bring PlayerName",
            "arguments": "[Player]",
        },
        ":refresh": {
            "description": "Refreshes a player (respawns them).",
            "example": ":refresh PlayerName",
            "arguments": "[Player]",
        },
        ":heal": {
            "description": "Heals a player to full health.",
            "example": ":heal PlayerName",
            "arguments": "[Player]",
        },
        ":view": {
            "description": "Views a player's screen.",
            "example": ":view PlayerName",
            "arguments": "[Player]",
        },
        ":wanted": {
            "description": "Adds a wanted level to a player.",
            "example": ":wanted PlayerName",
            "arguments": "[Player]",
        },
        ":unwanted": {
            "description": "Removes a player's wanted level.",
            "example": ":unwanted PlayerName",
            "arguments": "[Player]",
        },
        ":jail": {
            "description": "Jails a player.",
            "example": ":jail PlayerName",
            "arguments": "[Player]",
        },
    },

    # Utility Commands
    "Utility Commands": {
        ":time": {
            "description": "Sets the server time.",
            "example": ":time 12",
            "arguments": "[Number]",
        },
        ":stopfire": {
            "description": "Stops all fires in the server.",
            "example": ":stopfire",
            "arguments": "None",
        },
        ":startfire": {
            "description": "Starts a fire at a specified location.",
            "example": ":startfire LocationName",
            "arguments": "[String]",
        },
        ":startnearfire": {
            "description": "Starts a fire near a specified location.",
            "example": ":startnearfire LocationName",
            "arguments": "[String]",
        },
        ":to": {
            "description": "Teleports to a specific player.",
            "example": ":to PlayerName",
            "arguments": "[Player]",
        },
        ":tocar": {
            "description": "Teleports to a car.",
            "example": ":tocar",
            "arguments": "None",
        },
        ":pt": {
            "description": "Performs an action with a specific party size.",
            "example": ":pt 5",
            "arguments": "[Number]",
        },
    },

    # Informational Commands
    "Informational Commands": {
        ":commands": {
            "description": "Displays the list of available commands.",
            "example": ":commands",
            "arguments": "None",
        },
        ":bans": {
            "description": "Displays the list of banned players.",
            "example": ":bans",
            "arguments": "None",
        },
        ":helpers": {
            "description": "Displays the list of current helpers.",
            "example": ":helpers",
            "arguments": "None",
        },
        ":admins": {
            "description": "Displays the list of current admins.",
            "example": ":admins",
            "arguments": "None",
        },
        ":mods": {
            "description": "Displays the list of current moderators.",
            "example": ":mods",
            "arguments": "None",
        },
    },
}
