const int shift = 3; // Shift amount for the Caesar cipher

void setup() {
    Serial.begin(9600);
    Serial.println("Enter a message:");
}

void loop() {
    if (Serial.available()) {
        String message = Serial.readString();
        message.trim();
        Serial.println("Encrypted: " + caesarCipher(message, shift));
    }
}

String caesarCipher(String text, int shift) {
    for (int i = 0; i < text.length(); i++) {
        char c = text[i];

        if (isAlpha(c)) {
            char base = isLowerCase(c) ? 'a' : 'A';
            text[i] = (c - base + shift) % 26 + base;
        }
    }
    return text;
}

bool isAlpha(char c) {
    return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
}

bool isLowerCase(char c) {
    return (c >= 'a' && c <= 'z');
}
