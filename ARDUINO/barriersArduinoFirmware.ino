#include <WiegandMulti.h>

// ---- DIGITAL PINS -----
// Пины считывателя на вход
#define D0Enter 2
#define D1Enter 3
// Пины считывателя на выход
#define D0Exit 4
#define D1Exit 5
// Турникет
#define f2 7
#define f1 6
#define f2Common 8
#define f1Common 9

// ---- ANALOG PINS -----
// Звук считывателя
#define soundReaderExit A4
#define soundReaderEnter A5
// Лампочки считывателей
#define ledReaderExit A2
#define ledReaderEnter A3
// Реле
#define relayExit A0
#define relayEnter A1

 // Считыватель на вход
WIEGANDMULTI wgEnter;
// Cчитыватель на выход
WIEGANDMULTI wgExit; 

void Reader1D0Interrupt(void) {
  wgEnter.ReadD0();
}

void Reader1D1Interrupt(void) {
  wgEnter.ReadD1();
}

void Reader2D0Interrupt(void) {
  wgExit.ReadD0();
}

void Reader2D1Interrupt(void) {
  wgExit.ReadD1();
}


void setup() {
	Serial.begin(9600);  
	wgEnter.begin(D0Enter ,D1Enter, Reader1D0Interrupt, Reader1D1Interrupt);
	wgExit.begin(D0Exit, D1Exit, Reader2D0Interrupt ,Reader2D1Interrupt);

  pinMode(soundReaderEnter, OUTPUT);
  pinMode(soundReaderExit, OUTPUT);
  pinMode(ledReaderEnter, OUTPUT);
  pinMode(ledReaderExit, OUTPUT);
  pinMode(relayEnter, OUTPUT);
  pinMode(relayExit, OUTPUT);
  pinMode(f2, INPUT); // F2 НЗ
  pinMode(f1, INPUT); // F1 НЗ
  pinMode(f2Common, OUTPUT); // F2 общий
  pinMode(f1Common, OUTPUT); // F1 общий

  digitalWrite(soundReaderEnter, HIGH);
  digitalWrite(soundReaderExit, HIGH);
  digitalWrite(ledReaderEnter, HIGH);
  digitalWrite(ledReaderExit, HIGH);
  digitalWrite(relayEnter, LOW);
  digitalWrite(relayExit, LOW);

   // -- Для прокрутки турникета
  digitalWrite(f2, HIGH);
  digitalWrite(f1, HIGH);
}

void loop() {
  delay(50);
  // Выдать данные с карты в сериал порт
	if(wgEnter.available()) printCardCode(wgEnter.getCode(), "enter");
	if(wgExit.available()) printCardCode(wgExit.getCode(), "exit");

  // Получить комманды для турникета с сериал порта
  if(Serial.available()) {
    String serialData = Serial.readString();
    String command = getSerialCommand(serialData);
    String commandSide = getCommandSide(serialData);
    
    if (command == "user-not-found") alertSignal(commandSide);
    if (command == "user-success") controlDoor(commandSide);
  }
}

// Выдать данные карты в сериал порт
void printCardCode(long unsigned code, String direction) {
  Serial.print("@Code=");
  Serial.print(code);
  Serial.print(";");
  Serial.print("@Direction="); 
  Serial.print(direction);
  Serial.println("");
}

// Воспроизвести сигнал и включить
// светодиод на считывателе при неудаче
void alertSignal(String direction) {
  if (direction == "exit") {
    digitalWrite(soundReaderExit, LOW);
    delay(1500);
    digitalWrite(soundReaderExit, HIGH);
  } else {
    digitalWrite(soundReaderEnter, LOW);
    delay(1500);
    digitalWrite(soundReaderEnter, HIGH);
  }
}

// Управление проходом
void controlDoor(String direction) {
  if (direction == "exit") {
    bool exited = false;
    digitalWrite(ledReaderExit, LOW); // Делаем лампочку на считывателе зелёной
    digitalWrite(relayExit, HIGH); // Открываем реле

    for (int i=0; i < 350; i++ ) {
      if (digitalRead(f2) == HIGH) {
        digitalWrite(ledReaderExit, HIGH); // Возвращшаем лампочку на считывателе в крастный 
        digitalWrite(relayExit, LOW); // Закрываем реле
        Serial.println("exit-success");
        exited = true;
        break;
      } 
      delay(10);
    }

    digitalWrite(ledReaderExit, HIGH);
    digitalWrite(relayExit, LOW);

    if (!exited) Serial.println("exit-fail");
    
    // Если это сторона входа
  } else if (direction == "enter") {
    bool entered = false;
    digitalWrite(ledReaderEnter, LOW); // Делаем лампочку на считывателе зелёной
    digitalWrite(relayEnter, HIGH); // Открываем реле

    for (int i=0; i < 350; i++ ) {
      if (digitalRead(f1) == HIGH) {
        digitalWrite(ledReaderEnter, HIGH); // Возвращшаем лампочку на считывателе в крастный 
        digitalWrite(relayEnter, LOW); // Закрываем реле
        Serial.println("enter-success");
        entered = true;
        break;
      }
      delay(10);
    }

    digitalWrite(ledReaderEnter, HIGH);
    digitalWrite(relayEnter, LOW);

    if (!entered) Serial.println("enter-fail");
  }
}

// Получить строку из сериал порта
String getValue(String data, char separator, int index) {
  int found = 0;
  int strIndex[] = { 0, -1 };
  int maxIndex = data.length() - 1;

  for (int i = 0; i <= maxIndex && found <= index; i++) {
    if (data.charAt(i) == separator || i == maxIndex) {
        found++;
        strIndex[0] = strIndex[1] + 1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }
  
  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

// Получить код из комманды пришедшей в сериал порт
String getSerialCommand(String str) {
  str.trim();
  String code = getValue(str, ';', 0);
  return getValue(code, '=', 1);
}

// Получить направление из комманды пришедшей в сериал порт
String getCommandSide(String str) {
  str.trim();
  String reader = getValue(str, ';', 1);
  return getValue(reader, '=', 1);
}
