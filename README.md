# Correctly

**Correctly** is an intelligent typing tool that understands your typing intent, even if you're using the wrong keyboard layout. Forget about switching languages manually—Correctly detects and corrects mistyped input, ensuring your message comes out just as you intended.

## Features

- **Automatic Keyboard Layout Detection**: Detects if you're using the wrong layout and automatically corrects it.
- **AI-Powered Correction**: Uses AI to understand the intended text and corrects typing mistakes caused by using the wrong layout.
- **Supports Multiple Languages**: Correctly works with multiple language layouts, including English and Arabic (or others with customization).

## How It Works

Correctly listens to your keyboard input, and after a brief delay, analyzes what you typed. Using AI, it detects if the input doesn't match the intended language and corrects it accordingly.

For example, if you forget that your keyboard layout is set to Arabic and you start typing in English, Correctly will automatically convert “اثممخ صخقمي” to “hello world”.

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/mohamedch7/correctly.git
   cd correctly
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Run the Python script to start listening to your keyboard input:

```sh
python script.py
```

Correctly will start running in the background and automatically correct your typing if you use the wrong keyboard layout.

## Configuration

- **Keyboard Layouts**: You can customize the English and Arabic keyboard layouts in the `script.py` file by editing the `ENGLISH_LAYOUT` and `ARABIC_LAYOUT` constants.

## Requirements

- Python 3.7+
- `pynput` for capturing keyboard input.
- `openai` for AI-powered correction.
- `python-dotenv` for loading environment variables.

## Example

If you mistakenly type `اثممخ صخقمي` while intending to write `hello world`, Correctly will detect the wrong layout and convert it automatically to `hello world`.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve Correctly.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- Thanks to OpenAI for providing the powerful language model used to correct mistyped input.
- Inspired by the challenge of switching between language layouts seamlessly while typing.

## Contact

If you have any questions or feedback, please reach out at [mohamedakremch@protom.me].

