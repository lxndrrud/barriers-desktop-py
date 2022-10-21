#include <WiegandMega2560.h>

#define FALSE 0
#define TRUE  1


WIEGAND wg;

// Readers sound ports (Звук считывателя)
int soundReaderExit = 5;
int soundReaderEnter = 6;

// Readers led ports (Лампочки считывателей)
int ledReaderExit = 4;
int ledReaderEnter = 7;

// Relay ports (Реле)
int relayExit = 8;
int relayEnter = 9;

// Barriers ports (Порты для турникета)
int f2 = 50;
int f1 = 48;
int f2Common = 51;
int f1Common = 49;

void setup() {
  /* 
    f2 nz pin mode 44
    f1 nz pin mode 41
  */

  Serial.begin(9600);
  // Включить считыватели
	wg.begin(TRUE, TRUE, FALSE);

  pinMode(soundReaderEnter, OUTPUT);
  pinMode(soundReaderExit, OUTPUT);
  pinMode(ledReaderEnter, OUTPUT);
  pinMode(ledReaderExit, OUTPUT);

  pinMode(relayEnter, OUTPUT);
  pinMode(relayExit, OUTPUT);

  digitalWrite(soundReaderEnter, HIGH);
  digitalWrite(soundReaderExit, HIGH);
  digitalWrite(ledReaderEnter, HIGH);
  digitalWrite(ledReaderExit, HIGH);

  // РЕЛЕ ДЛЯ ТОГО ЧТОБЫ РАБОТАЛА ПРОКРУТКА ОНИ ДОЛЖНЫ БЫТЬ В HIGH
  digitalWrite(relayEnter, LOW);
  digitalWrite(relayExit, LOW);

  // -- Для прокрутки турникета
  pinMode(f2, INPUT); // F2 NZ
  pinMode(f1, INPUT); // F1 NZ
  pinMode(f2Common, OUTPUT); // F2 comman
  pinMode(f1Common, OUTPUT); // F1 comman
  digitalWrite(f2, HIGH);
  digitalWrite(f1, HIGH);
  
}

String getValue(String data, char separator, int index)
{
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

String getCode(String data) {
  return getValue(getValue(data, ';', 0), '=', 1);
}

String getReader(String data) {
  return getValue(getValue(data, ';', 1), '=', 1);
}


void loop() {
  // Задержка для считывания данных о проходе
  // Она ломает считыватели, если её включить, то они себя будут вести не адекватно
  // Начнётся полный рандом их работы. Но она нужна для турникета, пока хз как исправить
  //delay(50); 

  // Проверка прохода.
  /*if (digitalRead(f1) == HIGH) {
    
    digitalWrite(ledReaderEnter, HIGH);
    digitalWrite(relayEnter, HIGH);
    Serial.println("enter-success");
  }
  if (digitalRead(f2) == HIGH) {
    
    digitalWrite(ledReaderExit, HIGH);
    digitalWrite(relayExit, HIGH);
    Serial.println("exit-success");
  }
  */

  // Здесь происходит само считывание данных с карты и отправка результата в сириал-порт
  if(wg.available()) {
    Serial.print("@Code=");
    Serial.print(wg.getCode());
    Serial.print(";");
    if (wg.getGateActive() == 1) {
      Serial.print("@Direction=enter"); 
    } else if (wg.getGateActive() == 2) {
      Serial.print("@Direction=exit"); 
    }
    Serial.println("");
	}


  // Это основная функция для работы с турникетом
  if(Serial.available() > 0) {
    String serialData = Serial.readString();
    serialData.trim();
    String code = getValue(serialData, ';', 0);
    String reader = getValue(serialData, ';', 1);
    code = getValue(code, '=', 1);
    reader = getValue(reader, '=', 1);
    
    // Если пользователь не найде начинаем пищать
    // @Code=user-not-found;@reader=exit or @Code=user-not-found;@reader=enter
    if (code == "user-not-found") {
      if (reader == "exit") {
        digitalWrite(soundReaderExit, LOW);
        delay(1500);
        digitalWrite(soundReaderExit, HIGH);
      }
      else if (reader == "enter") {
        digitalWrite(soundReaderEnter, LOW);
        delay(1500);
        digitalWrite(soundReaderEnter, HIGH);
      }
    }

    // Если пользователь найден, то начинаем химичить с проходом (палками турникета)
    // @Code=user-success;@reader=exit or @Code=user-success;@reader=enter
    if (code == "user-success") {
      
      // Если это сторона выхода
      if (reader == "exit") {
        bool exited = false;
        digitalWrite(ledReaderExit, LOW); // Делаем лампочку на считывателе зелёной
        digitalWrite(relayExit, LOW); // Открываем реле

        for (int i=0; i < 350; i++ ) {
          if (digitalRead(f2) == HIGH) {
            digitalWrite(ledReaderExit, HIGH); // Возвращшаем лампочку на считывателе в крастный 
            digitalWrite(relayExit, HIGH); // Закрываем реле
            Serial.println("exit-success");
            exited = true;
            break;
          } 
          delay(10);
        }
        digitalWrite(ledReaderExit, HIGH);
        digitalWrite(relayExit, HIGH);
        if (!exited) {
          Serial.println("exit-fail");
        }
        
        // Если это сторона входа
      } else if (reader == "enter") {
        bool entered = false;
        digitalWrite(ledReaderEnter, LOW); // Делаем лампочку на считывателе зелёной
        digitalWrite(relayEnter, LOW); // Открываем реле

        for (int i=0; i < 350; i++ ) {
          if (digitalRead(f1) == HIGH) {
            digitalWrite(ledReaderEnter, HIGH); // Возвращшаем лампочку на считывателе в крастный 
            digitalWrite(relayEnter, HIGH); // Закрываем реле
            Serial.println("enter-success");
            entered = true;
            break;
          }
          delay(10);
        }

        digitalWrite(ledReaderEnter, HIGH);
        digitalWrite(relayEnter, HIGH);

        if (!entered) Serial.println("enter-fail");
      }
    }

    // ЗАКРЫТЬ ТУРНИКЕТ ПО КНОПКЕ
    // @Code=lock;@reader=exit or @Code=user-success;@reader=enter
    if (code == "lock") {
      if (reader == "exit") {
        digitalWrite(ledReaderExit, HIGH);
        digitalWrite(relayExit, HIGH);
      }
      else if (reader == "enter") {
        digitalWrite(ledReaderEnter, HIGH);
        digitalWrite(relayEnter, HIGH);
      }
      else if (reader == "both") {
        digitalWrite(ledReaderExit, HIGH);
        digitalWrite(relayExit, HIGH);
        digitalWrite(ledReaderEnter, HIGH);
        digitalWrite(relayEnter, HIGH);
      }
    }

    // ОТКРЫТЬ ТУРНИКЕТ ПО КНОПКЕ
    // @Code=unlock;@reader=exit or @Code=unlock;@reader=enter
    if (code == "unlock") {

      if (reader == "exit") {
        digitalWrite(ledReaderExit, LOW);
        digitalWrite(relayExit, LOW);
        while(Serial.available() == 0)
        digitalWrite(ledReaderExit, HIGH);
        digitalWrite(relayExit, HIGH);
      } else if (reader == "enter") {
        digitalWrite(ledReaderEnter, LOW);
        digitalWrite(relayEnter, LOW);
        while(Serial.available() == 0)
        digitalWrite(ledReaderEnter, HIGH);
        digitalWrite(relayEnter, HIGH);
      } else if (reader == "both") {
        digitalWrite(ledReaderExit, LOW);
        digitalWrite(relayExit, LOW);
        digitalWrite(ledReaderEnter, LOW);
        digitalWrite(relayEnter, LOW);
        while(Serial.available() == 0)
        digitalWrite(ledReaderExit, HIGH);
        digitalWrite(relayExit, HIGH);
        digitalWrite(ledReaderEnter, HIGH);
        digitalWrite(relayEnter, HIGH);
      }

    }
    
  }

}