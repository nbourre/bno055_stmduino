#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#define BNO055_SAMPLERATE_DELAY_MS (100)
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);
unsigned long myTime;
void displaySensorDetails(void)
{
  sensor_t sensor;
  bno.getSensor(&sensor);
  Serial.println("------------------------------------");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" xxx");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" xxx");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" xxx");
  Serial.println("------------------------------------");
  Serial.println("");
  delay(500);
}
void setup(void)
{
  Serial.begin(115200);
  Serial.println("Orientation Sensor Test"); Serial.println("");
  Wire.setSDA(A4);
  Wire.setSCL(A5);
  if(!bno.begin())
  {
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
   
  delay(1000);
  bno.setExtCrystalUse(true);
  displaySensorDetails();
}
void loop(void)
{
  imu::Vector<3> accel = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  imu::Vector<3> gyro = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
  imu::Vector<3> magn = bno.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER );
  myTime = millis();
 // timestamp;ax;ay;az;gx;gy;gz;mx;my;mz
  Serial.print(myTime);
  Serial.print(";");
  Serial.print(accel.x());
  Serial.print(";");
  Serial.print(accel.y());
  Serial.print(";");
  Serial.print(accel.z());
  Serial.print(";");
  Serial.print(gyro.x());
  Serial.print(";");
  Serial.print(gyro.y());
  Serial.print(";");
  Serial.print(gyro.z());
  Serial.print(";");
  Serial.print(magn.x());
  Serial.print(";");
  Serial.print(magn.y());
  Serial.print(";");
  Serial.print(magn.z());
  Serial.println(";");

  delay(BNO055_SAMPLERATE_DELAY_MS);
}
