# InstaAPI

InstaAPI is a simple Python Wrapper for interacting with the Instagram Downloader API via RapidAPI. This Wrapper allows you to easily fetch download links and thumbnails for Instagram posts.

> [!WARNING]  
> We are not affiliated with Instagram in any way. Use this tool responsibly and adhere to Instagram’s Terms of Service. This tool is meant to work with publicly available Instagram content.

## Features

- Fetch Instagram post download links and thumbnails.
- Securely store and use your RapidAPI key.

## Prerequisites

Before you start, you'll need:

1. A **RapidAPI** account: If you don’t have one, you can create it at [RapidAPI](https://rapidapi.com/).
2. The **Instagram Downloader API** key: You can subscribe to it [here](https://rapidapi.com/officialofun-C-wpfpix418/api/test-api646).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/farhaanaliii/InstaAPI.git
   ```

2. Navigate to the project folder:

   ```bash
   cd InstaAPI
   ```

3. Install required Python packages:

   ```bash
   pip install requests
   ```

## Setup

1. **Store your RapidAPI key securely**:
   - Open the `config.py` file in the project.
   - Replace `"your_rapidapi_key_here"` with your actual RapidAPI key.

   ```python
   RAPIDAPI_KEY = "your_rapidapi_key_here"  # Replace with your actual API key
   ```

2. **Running the Test**:
   After setting up the API key in `config.py`, run the `main.py` script:

   ```bash
   python main.py
   ```

   This will fetch the Instagram post's thumbnail and download link and display them in the terminal.

## Example Usage

In `main.py`, you can change the `post_url` to any Instagram post URL you want to fetch data from. Here's the default example:

```python
post_url = "https://www.instagram.com/coding.np/p/DCyqv53Sa8R/"
```

The script will fetch and display the thumbnail and download link.

## Contributing

Feel free to fork this repository and contribute by submitting issues and pull requests.

## Author

- **Farhan Ali**
  - GitHub: [@farhaanaliii](https://github.com/farhaanaliii)

## License

This project is open source and available under the [MIT License](LICENSE).
