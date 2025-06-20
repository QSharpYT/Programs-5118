
#include <Arduino.h>

// Morse code dictionary (compact storage)
const char* morseTable[] = {
  ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", // A-Z
  "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."  // 0-9
};

#define CHAR_OFFSET 48 // ASCII offset for digits
#define ALPHA_OFFSET 65 // ASCII offset for letters

void setup() {
  Serial.begin(9600);
  Serial.println("Morse Code Translator Ready!");
  Serial.println("Enter 'T:<text>' for text-to-Morse or 'M:<morse>' for Morse-to-text.");
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    if (input.startsWith("T:")) {
      String text = input.substring(2);
      text.toUpperCase();
      Serial.println("Morse Code: " + textToMorse(text));
    } else if (input.startsWith("M:")) {
      String morse = input.substring(2);
      Serial.println("Translated Text: " + morseToText(morse));
    } else {
      Serial.println("Invalid input format. Use 'T:<text>' or 'M:<morse>'.");
    }
  }
}

// Converts text to Morse code
String textToMorse(const String& text) {
  String morse = "";

  for (char c : text) {
    if (c >= 'A' && c <= 'Z') {
      morse += morseTable[c - ALPHA_OFFSET];
    } else if (c >= '0' && c <= '9') {
      morse += morseTable[c - CHAR_OFFSET + 26];
    } else if (c == ' ') {
      morse += "/"; // Word separator
    } else {
      continue; // Ignore unsupported characters
    }

    morse += " "; // Space between characters
  }

  morse.trim(); // Remove trailing space
  return morse;
}

// Converts Morse code to text
String morseToText(const String& morse) {
  String text = "";
  String currentSymbol = "";

  for (char c : morse) {
    if (c == '.' || c == '-') {
      currentSymbol += c;
    } else if (c == ' ' || c == '/') {
      if (!currentSymbol.isEmpty()) {
        text += decodeMorseSymbol(currentSymbol);
        currentSymbol = "";
      }
      if (c == '/') {
        text += ' '; // Add space for word separation
      }
    }
  }

  if (!currentSymbol.isEmpty()) {
    text += decodeMorseSymbol(currentSymbol);
  }

  return text;
}

// Decodes a single Morse code symbol
char decodeMorseSymbol(const String& symbol) {
  for (int i = 0; i < 36; i++) {
    if (symbol == morseTable[i]) {
      return (i < 26) ? ('A' + i) : ('0' + i - 26);
    }
  }
  return '?'; // Unknown symbol
}
