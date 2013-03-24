#include <Wire.h> // Used for I2C

#define ADNS2080_ADDRESS 0x00
#define WHO_AM_I 0x00


#define Delta_Y				0x04
#define Delta_X				0x03
#define Motion_Status	        	0x02

#define Mask_Motion			0x80
#define Mask_DYOVF			0x10
#define Mask_DXOVF			0x08


void setup()
{
  Serial.begin(38400);
  Serial.println("ADNS-2080 Basic Example");

  Serial.println("here 1");
  Wire.begin(); //Join the bus as a master
  Serial.println("here 2");
  
  initADNS2080(); //Test and intialize the MMA8452
}

void loop()
{  
  int delta[2];  // Stores the 12-bit signed value
  readOFSData(delta);  // Read the x/y/z adc values

  // Print out values
  for (int i = 0 ; i < 2 ; i++)
  {
    Serial.print(delta[i]);  // Print g values
    Serial.print("\t\t");  // tabs in between axes
  }
  Serial.println();

  delay(10);  // Delay here for visibility
}

void readOFSData(int *destination)
{
  byte rawData[2];

  rawData[0] = readRegister(Delta_X);
  rawData[1] = readRegister(Delta_Y);

}

// Initialize the MMA8452 registers 
// See the many application notes for more info on setting all of these registers:
// http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=MMA8452Q
void initADNS2080()
{
  Serial.println("here");
  byte c = readRegister(WHO_AM_I);  // Read WHO_AM_I register
  Serial.println("now here");
  if (c == 0x2A) // WHO_AM_I should always be 0x2A
  {  
    Serial.println("ADNS2080 is online...");
  }
  else
  {
    Serial.print("Could not connect to ADNS2080: 0x");
    Serial.println(c, HEX);
    while(1) ; // Loop forever if communication doesn't happen
  }
}

// Read bytesToRead sequentially, starting at addressToRead into the dest byte array
void readRegisters(byte addressToRead, int bytesToRead, byte * dest)
{
  Wire.beginTransmission(ADNS2080_ADDRESS);
  Wire.write(addressToRead);
  Wire.endTransmission(false); //endTransmission but keep the connection active

  Wire.requestFrom(ADNS2080_ADDRESS, bytesToRead); //Ask for bytes, once done, bus is released by default

  while(Wire.available() < bytesToRead); //Hang out until we get the # of bytes we expect

  for(int x = 0 ; x < bytesToRead ; x++)
    dest[x] = Wire.read();    
}

// Read a single byte from addressToRead and return it as a byte
byte readRegister(byte addressToRead)
{
  Wire.beginTransmission(ADNS2080_ADDRESS);
  Wire.write(addressToRead);
  Wire.endTransmission(false); //endTransmission but keep the connection active

  Wire.requestFrom(ADNS2080_ADDRESS, 1); //Ask for 1 byte, once done, bus is released by default

  while(!Wire.available()) ; //Wait for the data to come back
  return Wire.read(); //Return this one byte
}

// Writes a single byte (dataToWrite) into addressToWrite
void writeRegister(byte addressToWrite, byte dataToWrite)
{
  Wire.beginTransmission(ADNS2080_ADDRESS);
  Wire.write(addressToWrite);
  Wire.write(dataToWrite);
  Wire.endTransmission(); //Stop transmitting
}
