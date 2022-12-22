# API Client

This is beginning of a simple API client application. It retrieves information from APIs that use Bearer Tokens for authorization.

## Running

The application is a Python script. It requires Python being installed on the machine where it is run. The command to run it is:

```{bash}
python run.py
```

## Auth.ini

The auth.ini file contains all the keys and IDs needed to obtain access to the API. The auth.example.ini shows the form of the file. By filling in the correct values in the example file one can create the necessary ini-file.

## Endpoints

The api_endpoints.py contains a dict with the endpoints and URLs that are used for retrieving information from the APIs. When all the right permissions are obtained from all the relevant organisations, one can replace the `endpoints` dict with the `future_endpoints` and the script will retrieve all the available data from those organisations.
