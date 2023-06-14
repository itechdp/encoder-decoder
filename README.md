# Encoder/Decoder for Text

This is a simple Python program that allows you to encode and decode text using ASCII values.

## Description

The program takes a text input from the user and performs the following steps:

1. Splits the input into individual words.
2. Converts each word into a list of characters.
3. Converts each character into its corresponding ASCII value.
4. Increments the ASCII values by 5 to encode the text.
5. Converts the encoded ASCII values back into characters.
6. Outputs the encoded text.

For decoding, the program reverses the process:

1. Converts the encoded text into ASCII values.
2. Decrements the ASCII values by 5 to decode the text.
3. Converts the decoded ASCII values back into characters.
4. Outputs the decoded text.

## Usage

To encode or decode text, follow these steps:

1. Run the program.
2. Choose the encoding or decoding option.
3. If you choose encoding, you can choose to store the encoded data in a file.
4. Enter the text you want to encode or decode.

## File Storage

If you choose to store the encoded data, you will be prompted to provide a file name and specify what you want to store (e.g., username, password, or any kind of text). The program will save the data in a file named `<file_name>.txt` in the `E:\Login data\` directory.

## Dependencies

The code does not have any external dependencies.

## Contribution

Feel free to contribute to the code by submitting pull requests or suggesting improvements. If you encounter any issues, please open an issue in the GitHub repository.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).

