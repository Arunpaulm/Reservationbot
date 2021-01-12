payload = {
    "type": "object",
    "properties": {
        "invalid_trigger": {"type": "string", "maxLength": 20},
        "key": {"type": "string", "maxLength": 11},
        "name": {"type": "number", "minimum": 60, "maximum": 2592000},
        "reuse": {"type": "number", "minimum": 60, "maximum": 2592000},
        "support_multiple": {"type": "string", "format": "cron", "maxLength": 100},
        "pick_first": {"type": "string", "format": "timezone", "maxLength": 36},
        "channels": {"type": "string"},
        "unique": {
            "type": "array",
            "items": {"enum": ["name", "tags", "timeout", "grace"]}
        }
    }
}