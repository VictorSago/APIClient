
endpoints = {
    "CENELEC": {
        "BaseURL": "https://api.cenelec.eu/",
        "AuthPath": "oauth/client_credential/accesstoken?grant_type=client_credentials",
        "APIPath": "harmonized",
        "APIEndpoints": ["projects", "publications"]
    }
}

future_endpoints = {
    "CENELEC": {
        "BaseURL": "https://api.cenelec.eu/",
        "AuthPath": "oauth/client_credential/accesstoken?grant_type=client_credentials",
        "APIPath": "harmonized",
        "APIEndpoints": ["projects", "publications"]
    },
    "CEN": {
        "BaseURL": "https://api.cen.eu/",
        "AuthPath": "oauth/client_credential/accesstoken?grant_type=client_credentials",
        "APIPath": "harmonized",
        "APIEndpoints": ["documents", "projects", "publications"]
    },
    "IEC": {
        "BaseURL": "https://api.iec.ch/",
        "AuthPath": "oauth/client_credential/accesstoken?grant_type=client_credentials",
        "APIPath": "harmonized",
        "APIEndpoints": ["comittees", "persons", "organizations", "memberships", "roles", "projects", "publications"]
    },
    "ISO": {
        "BaseURL": "https://api.iso.org/",
        "AuthPath": "oauth/client_credential/accesstoken?grant_type=client_credentials",
        "APIPath": "harmonized",
        "APIEndpoints": ["documents", "comittees", "persons", "organizations", "memberships", "roles", "projects", "publications"]
    }
}
