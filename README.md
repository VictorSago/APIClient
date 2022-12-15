# API Client

This is an API client application for SEK Svensk Elstandard. It retrieves information from standardization 
organisations. At this stage it only retrieves from CENELEC, but with the right permissions it can also retrieve from CEN, IEC and ISO.

## Running

The application is a Python script. It requires Python being installed on the machine where it is run. The command to run it is:

```{bash}
python run.py
```

## Auth.ini

The auth.ini file contains all the keys and IDs needed to obtain access to the API. The auth.example.ini shows the 
form of the file. By feeling in the correct values in the example file one can create the necessary ini-file.

## Endpoints

The api_endpoints.py contains a dict with the endpoints and URLs that are used for retrieving information from the 
APIs. When all the right permissions are obtained from CEN, IEC and ISO, one can replace the endpoints dict with the 
future_endpoints and the script will retrieve all the available data from those organisations.
