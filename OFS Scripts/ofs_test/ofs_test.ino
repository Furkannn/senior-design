// inspired by Martijn The's sketch, adding all functionality of the 2610 chip, skipping
// the whole library-thing
#define SCLK 52  // Serial clock pin on the Arduino
#define SDIO 50  // Serial data (I/O) pin on the Arduino
#define sensorConfig 0x40 //CHANGE LATER
#define sensorStatus 0x00
#define Delta_Y	0x04
#define Delta_X	0x03
#define SQUAL   0x05
#define Maximum_pixel 0x08
#define Minimum_pixel 0x0A
#define Pixel_Sum 0x09
#define picture 0x0B
#define Shutter_MSB 0x09
#define Shutter_LSB 0x0A
 
unsigned char pixels[484];
 
void setup(){
  Serial.begin(38400);
  pinMode (SCLK, OUTPUT);
  pinMode (SDIO, INPUT);
  reSync();
    //forceAwake(1); // LED on
}
 
void loop(){
//    getPicture();  // take snapshot
//    sendPicture(); // send the picture
//    delay(100);
  //Serial.println(readRegister(sensorStatus),DEC);
  //delay(0);
  uint8_t delta_x = readRegister(Delta_X);
  //if (delta_x != 0 && delta_x != 255) {
    Serial.println(delta_x,DEC);
  //}
  delay(50);
  //Serial.println();
}
void reSync(){
  // ReSync (startup) mouse
  digitalWrite(SCLK, HIGH);                     
  delayMicroseconds(100);
  digitalWrite(SCLK, LOW);
  delayMicroseconds(100);
  digitalWrite(SCLK, HIGH);	
  // wait for OptiMouse serial transaction timer to time out:
  delay(1000);
  Serial.println("reSync done");
}
void getPicture(void){
  writeRegister(picture,0); // default write: initiate picture transfer
  for (int x=0;x<21;x++){   // MAYBE 22??
    for (int y=21;y>=0;y--){// 18 collumns (reverse order)
      unsigned char pix = readRegister(picture); // SPI read operation
      int timeout = 12;                          // Try 12 times max to
      while (!(pix & 0x40) && timeout>0){        // check for valid data
        pix = readRegister(picture);             // read the picture data
        timeout--;
      }
      pixels[x*22+y]=pix&0x3F; // store the data (might still be invalid after 12 tries) // was pix&0x2F
    }
  }
}
void sendPicture(void){
  for(int z=0;z<484;z++)  {
    Serial.print((unsigned char)(pixels[z]&0x3F)); // send block of 324 bytes //was pixels[z]&0x2F
  }
  Serial.println();
}
void forceAwake(char value){
  if (value>0) writeRegister(sensorConfig,0x01); 
  else writeRegister(sensorConfig,0x00);
}
signed char getDx(void){
  return (signed char) readRegister(Delta_X);
}
signed char getDy(void){
  return (signed char) readRegister(Delta_Y);
}
signed int getShutter(void){
  signed int shutter = readRegister(Shutter_MSB) <<8;
  shutter += readRegister(Shutter_LSB); // + LSB
  return shutter;
}
uint8_t readRegister(uint8_t address){ // Bitbang SPI read operation
  int i = 7;
  uint8_t r = 0;
  pinMode (SDIO, OUTPUT);   // Write the address of the register we want to read:
  for (; i>=0; i--)  {
    digitalWrite (SCLK, LOW);
    digitalWrite (SDIO, address & (1 << i));
    digitalWrite (SCLK, HIGH);
  }
  pinMode (SDIO, INPUT);    // Switch data line from OUTPUT to INPUT
  delayMicroseconds(200);   // Wait according to datasheet
  for (i=7; i>=0; i--)	{     // Fetch the data!                          
    digitalWrite (SCLK, LOW);
    digitalWrite (SCLK, HIGH);
    r |= (digitalRead (SDIO) << i);
  }
  delayMicroseconds(200);
  return r;
}
void writeRegister(uint8_t address, uint8_t data){
   int i = 7;	
   // Set MSB high, to indicate write operation:
  address |= 0x80;	
  // Write the address:
  pinMode (SDIO, OUTPUT);
  for (; i>=0; i--){
    digitalWrite (SCLK, LOW);
    digitalWrite (SDIO, address & (1 << i));
    digitalWrite (SCLK, HIGH);
  }	
  // Write the data:
  for (i=7; i>=0; i--){
    digitalWrite (SCLK, LOW);
    digitalWrite (SDIO, data & (1 << i));
    digitalWrite (SCLK, HIGH);
  }
}
