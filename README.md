![api1](https://github.com/ertugrulgaripardic/API-Get-Order/assets/118535200/82431851-18ce-4b19-a8fa-0db5a3e0638d)


# API  Application

This is a Python API application that interacts with an API to retrieve and display order data. The application provides a graphical user interface (GUI) using Tkinter for easy interaction.

## Features

- **Login**: Authenticate with the API using an API key.
- **Fetch Orders**: Retrieve and display orders from the API.

## Requirements

- Python 3.x
- `requests` library
- `tkinter` library (usually included with Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ertugrulgaripardic/API-Get-Order.git
    cd API-Get-Order
    ```

2. Install the required libraries:
    ```sh
    pip install requests
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Enter your API key in the provided field and click "Login".

3. After successful login, click "Get Orders" to fetch and display the orders.

## File Structure

- `api_client.py`: Contains the `APIClient` class that handles API requests.
- `app.py`: Contains the `App` class that handles the GUI.

## Example

![api2](https://github.com/ertugrulgaripardic/API-Get-Order/assets/118535200/d1a4c308-9da0-4289-a604-03ccc2570121)
![api3](https://github.com/ertugrulgaripardic/API-Get-Order/assets/118535200/bc2fa19d-bae5-4a2e-a5c9-ad8a9eb6e4f2)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
