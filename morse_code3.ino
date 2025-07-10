#define LED_PIN 13

String morseCode[] = {
  ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
};

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();
    for (char c : input) {
      if (isAlpha(c)) {
        encodeMorse(toupper(c));
      } else if (c == ' ') {
        delay(700); // Space between words
      }
    }
  }
}

void encodeMorse(char c) {
  updateDelay();
  int index = c - 'A';
  if (index >= 0 && index < 26) {
    String code = morseCode[index];
    for (char dotDash : code) {
      if (dotDash == '.') {
        digitalWrite(LED_PIN, HIGH);
        delay(200); // Dot duration
      } else if (dotDash == '-') {
        digitalWrite(LED_PIN, HIGH);
        delay(600); // Dash duration
      }
      digitalWrite(LED_PIN, LOW);
      delay(200); // Pause between dots/dashes
    }
    delay(400); // Pause between letters
  }
}

void updateDelay() {
  if (Serial.available() > 0) { // Check if data is available on Serial
    int dot = Serial.parseInt(); // Parse the integer from Serial input
    if (dot > 0) { // Ensure the delay value is positive
      int delayValue = dot;
      Serial.print("Delay updated to: ");
      Serial.println(delayValue);
    } else {
      Serial.println("Invalid input. Please enter a positive number.");
    }
  }
}
