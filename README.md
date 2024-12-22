# AI Desktop Assistant - Lyro

Lyro is an AI-based desktop assistant that helps automate day-to-day tasks like searching on Google, playing YouTube videos, fetching news, opening applications, and more. This assistant uses speech recognition and text-to-speech to interact with users, providing a hands-free experience.

## Features

- **Voice Interaction**: Communicate with the assistant using voice commands.
- **Wikipedia Search**: Retrieve brief summaries from Wikipedia.
- **Google Search**: Perform Google searches directly through voice commands.
- **YouTube Playback**: Play videos on YouTube based on your input.
- **News Headlines**: Fetch the latest news headlines.
- **Calendar**: Display the current month's calendar.
- **Movie Information**: Get detailed information about movies, including IMDb ratings, cast, and plot.
- **Date & Time**: Ask for the current date and time.
- **Music Playback**: Play music from your local directory.
- **Open Applications**: Open commonly used applications like Notepad, Calculator, WhatsApp, and Telegram.
- **YouTube Recommendations**: Open the trending YouTube page for recommendations.

## Installation

1. Clone this repository or download the project files.
2. Install the required Python dependencies:
   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia webbrowser requests pywhatkit imdbpy
   ```
3. Ensure you have the following tools installed and configured:
   - Python 3.7 or higher
   - Microphone for voice commands

## Usage

1. Run the program:
   ```bash
   python lyro.py
   ```
2. Speak your commands into the microphone. For example:
   - "Search on Google for AI and machine learning"
   - "Play music"
   - "Tell me the news"
   - "What is the time?"
   - "Open Calculator"
3. Say "Goodbye" to terminate the assistant.

## Project Structure

- `lyro.py`: Main script for the desktop assistant.

## Dependencies

- `pyttsx3`: Text-to-speech conversion
- `SpeechRecognition`: For recognizing voice input
- `wikipedia`: To fetch summaries from Wikipedia
- `webbrowser`: For opening URLs in the browser
- `os`: For interacting with the operating system
- `requests`: To fetch data from APIs (e.g., news headlines)
- `pywhatkit`: For YouTube playback and Google searches
- `imdbpy`: To fetch movie details from IMDb
- `calendar`: For displaying the calendar

## Known Issues

- The `NEWS_FETCH_API_KEY` and `NEWS_FETCH_API_URL` are missing in the script. Add your API key and URL to fetch news.
- Ensure proper internet connectivity for online features like Wikipedia search, YouTube, and news.

## Future Improvements

- Add GUI support for enhanced user interaction.
- Include error handling for missing API keys or internet connectivity issues.
- Expand functionality to support more applications and commands.

## License

This project is open-source and available under the MIT License.

---

Feel free to modify and enhance the project as needed. If you encounter any issues or have suggestions, please raise them in the issue tracker. Happy coding!
