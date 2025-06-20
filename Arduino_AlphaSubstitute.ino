void setup() {
  Serial.begin(115200);
  Serial.println("Enter text:");
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    for (int i = 0; i < input.length(); i++) {
      if (isAlpha(input[i])) input[i] = 'Z' - (input[i] - (isLowerCase(input[i]) ? 'a' : 'A'));
    }

    Serial.println("Reversed Alphabetical input: " + input);
    Serial.println("Enter more text:");
  }
}
