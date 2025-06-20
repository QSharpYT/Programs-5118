const int minNumber = 1;
const int maxNumber = 100;
int targetNumber;

void setup() {
    Serial.begin(115200);
    randomSeed(analogRead(0));  // Seed randomness
    targetNumber = random(minNumber, maxNumber + 1);

    Serial.println("Guess the Number Game!");
    Serial.print("I'm thinking of a number between ");
    Serial.print(minNumber);
    Serial.print(" and ");
    Serial.print(maxNumber);
    Serial.println(". Try to guess it!");
}

void loop() {
    if (Serial.available()) {
        int guess = Serial.parseInt();
        if (guess > 0) {  // Valid input
            if (guess < targetNumber) {
                Serial.println("Too low! Try again.");
            } else if (guess > targetNumber) {
                Serial.println("Too high! Try again.");
            } else {
                Serial.println("Congratulations! You guessed it!");
                delay(2000);
                targetNumber = random(minNumber, maxNumber + 1);
                Serial.println("New number chosen. Try again!");
            }
        }
    }
}
