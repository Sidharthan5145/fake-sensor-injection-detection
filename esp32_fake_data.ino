#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";
const char* serverURL = "http://YOUR_PC_IP:5000/predict";

void setup() {
  Serial.begin(115200);
  dht.begin();
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
}

void loop() {
  float temp;
  float hum = dht.readHumidity();

  // Fake data injection
  if (random(0, 10) > 7) {
    temp = random(80, 120); // FAKE DATA
  } else {
    temp = dht.readTemperature(); // REAL DATA
  }

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverURL);
    http.addHeader("Content-Type", "application/json");

    String json = "{\"temp\":" + String(temp) + ",\"hum\":" + String(hum) + "}";

    http.POST(json);
    http.end();
  }

  delay(3000);
}
