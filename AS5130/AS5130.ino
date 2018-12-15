/*
  Example Sketch for AMS AS1130 LED DRIVER. 
  Refer to Datasheet Revision 1.07

  Written by Hexadec 16-09-2012
  Feel free to do what you like with it :-)
  
/***********************************************************/
/*****                                                 *****/
/***** It's not always nescessary but it's a good idea *****/
/***** to power-down reset the AS1130 whenever a new   *****/
/***** upload of data is made as the frame memory and  *****/
/***** control registers are not always cleared.       *****/
/***** Adding a reset button and pull-up resistor to   *****/
/***** pin 13 of the AS1130 would make this easy.      *****/
/*****                                                 *****/
/***********************************************************/

/*

  *****************************
  Connections:
     
        AS1130 | connected to
  =============================
      [GND]  1 | GND  ---------
      (CS6)  2 |  (CS6)        | 10uF electrolytic
      [VDD]  3 | VDD  ---------
      (CS7)  4 |  (CS7)
      (CS8)  5 |  (CS8)
      (CS9)  6 |  (CS9)
      [GND]  7 | GND
     (CS11)  8 |  (CS11)
     (CS10)  9 |  (CS10)
      [VDD] 10 | VDD
      (IRQ) 11 |  4K7 Pull-up Resistor
     (SYNC) 12 |  4K7 Pull-up Resistor
     (RSTN) 13 | VDD
      [GND] 14 | GND
      (SCL) 15 |  4K7 Pull-up Resistor & Arduino:A5 SCL
      (SDA) 16 |  4K7 Pull-up Resistor & Arduino:A4 SDA
     (ADDR) 17 |  <open> (see Table 6 page 12 for other options)
      [VDD] 18 | VDD
      [VDD] 19 | VDD
      (CS5) 20 |  (CS5)
      (CS4) 21 |  (CS4)
      [GND] 22 | GND
      (CS2) 23 |  (CS2)
      (CS3) 24 |  (CS3)
      (CS0) 25 |  (CS0)
      [VDD] 26 | VDD
      (CS1) 27 |  (CS1)
      [GND] 28 | GND
  =============================
*/

//Use Wire Library to do I2C communication  
#include <Wire.h>         
#include <avr/interrupt.h>

/***** Register definitions for AS1130 ******************************/
//Refer to AS1130 Datasheet Revision 1.07
//
// AS1130 I2C Address - see table 6 page 12
#define AS1130ADDRESS     0x30
// 0x30 = default if PIN 17 floating

// RAM Section Selection - see table 7 page 14
#define REGISTERSELECTION 0xFD
#define NOP               0x00
#define FRAME0            0x01
#define FRAME1            0x02
#define FRAME2            0x03
#define FRAME3            0x04
#define FRAME4            0x05
#define FRAME5            0x06
#define FRAME6            0x07
#define FRAME7            0x08
#define FRAME8            0x09
#define FRAME9            0x0A
#define FRAME10           0x0B
#define FRAME11           0x0C
#define FRAME12           0x0D
#define FRAME13           0x0E
#define FRAME14           0x0F
#define FRAME15           0x10
#define FRAME16           0x11
#define FRAME17           0x12
#define FRAME18           0x13
#define FRAME19           0x14
#define FRAME20           0x15
#define FRAME21           0x16
#define FRAME22           0x17
#define FRAME23           0x18
#define FRAME24           0x19
#define FRAME25           0x1A
#define FRAME26           0x1B
#define FRAME27           0x1C
#define FRAME28           0x1D
#define FRAME29           0x1E
#define FRAME30           0x1F
#define FRAME31           0x20
#define FRAME32           0x21
#define FRAME33           0x22
#define FRAME34           0x23
#define FRAME35           0x24

#define BLINK_PWM0        0x40
#define BLINK_PWM1        0x41
#define BLINK_PWM2        0x42
#define BLINK_PWM3        0x43
#define BLINK_PWM4        0x44
#define BLINK_PWM5        0x45

#define DOTCORRECTION     0x80
#define CONTROLREGISTER   0xC0

// AS1130 Control Register - see table 13 page 20
#define PICTURE           0x00
#define MOVIE             0x01
#define MOVIEMODE         0x02
#define FRAMETIME         0x03
#define DISPLAYOPTION     0x04
#define CURRENTSOURCE     0x05
#define AS1130CONFIG      0x06
#define INTERRUPTMASK     0x07
#define INTERRUPTFRAME    0x08
#define SHUTDOWNOPENSHORT 0x09
#define I2CINTERFACE      0x0A
#define CLKSYNC           0x0B
#define INTERRUPTSTATUS   0x0E
#define AS1130STATUS      0x0F

// uncomment the following lines for debug mode
//#define DEBUG 1
//#define DEBUG_DATA_UPLOAD 1
//#define DEBUG_INTERRUPT 1
//#define DEBUG_STATUS 1
/*****************************************************/
/**** There are much better ways of handling the  ****/
/**** datasets etc. but this is NOT a programming ****/ 
/**** tutorial; it is an attempt to demonstrate   ****/
/**** the use of the AS1130 chip and to simplify  ****/
/**** and explain the Datasheet which can be a    ****/
/**** bit confusing!                              ****/
/**** I've done things this way to (hopefully)    ****/
/**** make the set-up procedure clearer and to    ****/
/**** provide a start point for coders who are    ****/
/**** having trouble translating the Datasheet.   ****/
/**** The graphics are crappy and the programming ****/
/**** is long-winded and over commented - which   ****/
/**** is just what you want when you are trying   ****/
/**** out a new process.                          ****/
/**** So....                                      ****/
/**** All you experts out there, please use your  ****/
/**** skills to add to the knowledge - not to     ****/
/**** criticise my lack of it :-)                 ****/
/****                                             ****/
/*****************************************************/
int flip = 0b01010011;
//change this to suit debugging requirements
int debug_delay = 50;   //change this to suit debugging requirements
// Counter for the number of Interrupts generated
uint8_t int_Count = 0;
// General delay time variable
uint16_t delay_ms = 300;
//6 frames * 12 segments * 2 bytes
uint8_t Frames_Data[0X90] =  {

  //All on
  0b00000111, 0b11111111,    //CS0   Frame 0 PWM set 0
  0b00000111, 0b11111111,    //CS1
  0b00000111, 0b11111111,    //CS2
  0b00000111, 0b11111111,    //CS3
  0b00000111, 0b11111111,    //CS4
  0b00000111, 0b11111111,    //CS5
  0b00000111, 0b11111111,    //CS6
  0b00000111, 0b11111111,    //CS7
  0b00000111, 0b11111111,    //CS8
  0b00000111, 0b11111111,    //CS9
  0b00000111, 0b11111111,    //CS10
  0b00000111, 0b11111111,    //CS11
  
  //All on
  0b00100111, 0b11111111,    //CS0   Frame 1 PWM set 1
  0b00000111, 0b11111111,    //CS1
  0b00000111, 0b11111111,    //CS2
  0b00000111, 0b11111111,    //CS3
  0b00000111, 0b11111111,    //CS4
  0b00000111, 0b11111111,    //CS5
  0b00000111, 0b11111111,    //CS6
  0b00000111, 0b11111111,    //CS7
  0b00000111, 0b11111111,    //CS8
  0b00000111, 0b11111111,    //CS9
  0b00000111, 0b11111111,    //CS10
  0b00000111, 0b11111111,    //CS11

  //All on
  0b10000111, 0b11111111,    //CS0   Frame 2 PWM set 4
  0b00000111, 0b11111111,    //CS1
  0b00000111, 0b11111111,    //CS2
  0b00000111, 0b11111111,    //CS3
  0b00000111, 0b11111111,    //CS4
  0b00000111, 0b11111111,    //CS5
  0b00000111, 0b11111111,    //CS6
  0b00000111, 0b11111111,    //CS7
  0b00000111, 0b11111111,    //CS8
  0b00000111, 0b11111111,    //CS9
  0b00000111, 0b11111111,    //CS10
  0b00000111, 0b11111111,    //CS11

  //heart
  0b01100000, 0b00111000,    //CS0   Frame 3 PWM set 3
  0b00000000, 0b01111100,    //CS1
  0b00000000, 0b11111110,    //CS2
  0b00000001, 0b11111110,    //CS3
  0b00000011, 0b11111100,    //CS4
  0b00000111, 0b11111000,    //CS5
  0b00000011, 0b11111100,    //CS6
  0b00000001, 0b11111110,    //CS7
  0b00000000, 0b11111110,    //CS8
  0b00000000, 0b01111100,    //CS9
  0b00000000, 0b00111000,    //CS10
  0b00000000, 0b00000000,    //CS11
  
  //circle
  0b01000000, 0b01110000,    //CS0   Frame 4 PWM set 2
  0b00000001, 0b00000100,    //CS1
  0b00000010, 0b00000010,    //CS2
  0b00000000, 0b00000000,    //CS3
  0b00000100, 0b00000001,    //CS4
  0b00000100, 0b00100001,    //CS5
  0b00000100, 0b00000001,    //CS6
  0b00000000, 0b00000000,    //CS7
  0b00000010, 0b00000010,    //CS8
  0b00000001, 0b00000100,    //CS9
  0b00000000, 0b01110000,    //CS10
  0b00000000, 0b00000000,    //CS11

  //face negative
  0b00100111, 0b10001111,    //CS0   Frame 5 PWM set 1
  0b00000110, 0b11111011,    //CS1
  0b00000101, 0b11111101,    //CS2
  0b00000111, 0b01100111,    //CS3
  0b00000010, 0b11100110,    //CS4
  0b00000010, 0b10011110,    //CS5
  0b00000010, 0b11100110,    //CS6
  0b00000111, 0b01100111,    //CS7
  0b00000101, 0b11111101,    //CS8
  0b00000110, 0b11111011,    //CS9
  0b00000111, 0b10001111,    //CS10
  0b00000111, 0b11111111,    //CS11
};

// LED 00 in the set above is the LSB of
// the second byte in the set.
// LED 00's PWM byte is the 1st byte of the datasets below.

//6 PWM datasets
uint8_t PWM_Data[0x318] =  {
 // Set 0
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS0
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS1
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS2
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS3
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS4
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0x05, 0x05,    //CS5
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0x05, 0x05,    //CS6
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS7
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS8
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS9
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS10
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS11
  
  // Set 1
  0X05, 0X05, 0X05, 0X05, 0X05, 0x7F, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS0
  0X05, 0X05, 0X05, 0X05, 0x7F, 0x7F, 0x7F, 0X05, 0X05, 0X05, 0X05,    //CS1
  0X05, 0X05, 0X05, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0X05, 0X05, 0X05,    //CS2
  0X05, 0X05, 0x7F, 0x7F, 0x7F, 0x05, 0x7F, 0x7F, 0x7F, 0X05, 0X05,    //CS3
  0X05, 0x7F, 0x7F, 0x7F, 0x05, 0x05, 0x05, 0x7F, 0x7F, 0x7F, 0X05,    //CS4
  0x7F, 0x7F, 0x7F, 0x05, 0x05, 0x05, 0x05, 0x05, 0x7F, 0x7F, 0x7F,    //CS5
  0X05, 0x7F, 0x7F, 0x7F, 0x05, 0x05, 0x05, 0x7F, 0x7F, 0x7F, 0X05,    //CS6
  0X05, 0X05, 0x7F, 0x7F, 0x7F, 0x05, 0x7F, 0x7F, 0x7F, 0X05, 0X05,    //CS7
  0X05, 0X05, 0X05, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0X05, 0X05, 0X05,    //CS8
  0X05, 0X05, 0X05, 0X05, 0x7F, 0x7F, 0x7F, 0X05, 0X05, 0X05, 0X05,    //CS9
  0X05, 0X05, 0X05, 0X05, 0X05, 0x7F, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS10
  0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05, 0X05,    //CS11

  // Set 2 50% Duty
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS0
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS1
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS2
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS3
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS4
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS5
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS6
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS7
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS8
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS9
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS10
  0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,    //CS11
  
  // Set 3 20% Duty
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS0
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS1
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS2
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS3
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS4
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS5
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS6
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS7
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS8
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS9
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS10
  0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33,    //CS11

  // Set 4 Mixed Duty
  0x3F, 0x3F, 0x3F, 0x3F, 0x3F, 0x7F, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF,    //CS0
  0x1F, 0x3F, 0x3F, 0x3F, 0x3F, 0x3F, 0x7F, 0x7F, 0xFF, 0xFF, 0xFF,    //CS1
  0x1F, 0x1F, 0x3F, 0x3F, 0x3F, 0x3F, 0x3F, 0x7F, 0x7F, 0xFF, 0xFF,    //CS2
  0x0F, 0x1F, 0x1F, 0x3F, 0x3F, 0x3F, 0x3F, 0x3F, 0x7F, 0x7F, 0xFF,    //CS3
  0x0F, 0x0F, 0x1F, 0x1F, 0x3F, 0x3F, 0x3F, 0x3F, 0x3F, 0x7F, 0x7F,    //CS4
  0x07, 0x0F, 0x0F, 0x1F, 0x1F, 0x3F, 0x3F, 0x3F, 0x3F, 0x3F, 0x7F,    //CS5
  0x07, 0x07, 0x0F, 0x0F, 0x1F, 0x1F, 0x3F, 0x3F, 0x3F, 0x3F, 0x3F,    //CS6
  0x05, 0x07, 0x07, 0x0F, 0x0F, 0x1F, 0x1F, 0x3F, 0x3F, 0x3F, 0x3F,    //CS7
  0x05, 0x05, 0x07, 0x07, 0x0F, 0x0F, 0x1F, 0x1F, 0x3F, 0x3F, 0x3F,    //CS8
  0x03, 0x05, 0x05, 0x07, 0x07, 0x0F, 0x0F, 0x1F, 0x1F, 0x3F, 0x3F,    //CS9
  0x03, 0x03, 0x05, 0x05, 0x07, 0x07, 0x0F, 0x0F, 0x1F, 0x1F, 0x3F,    //CS10
  0x01, 0x03, 0x03, 0x05, 0x05, 0x07, 0x07, 0x0F, 0x0F, 0x1F, 0x1F,    //CS11

  // Set 5 1% Duty
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS0
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS1
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS2
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS03
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS4
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS5
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS6
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS7
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS8
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS9
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS10
  0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,    //CS11
};

/***** Interrupt Service Routine ************************************************/
void ISR_Handler() 
{
    #ifdef DEBUG_INTERRUPT
       Serial.println("Interrupt Generated\r\n");
       Serial.print("Interrupt No.: ");
       Serial.print(int_Count);
       Serial.print("\r\n");
    #endif 
    
  if(int_Count == 0)        //Change scroll direction
    {
     if(flip == 0b01010011)
         flip = 0b00010011;
     else flip = 0b01010011;
     as_config(CONTROLREGISTER, MOVIEMODE, 0b00000101);
     as_config(CONTROLREGISTER, DISPLAYOPTION, flip);
     as_config(CONTROLREGISTER, MOVIE, 0b01000000);
    }
   int_Count++;
}

/***** Function to write commands and data to I2C bus ***************************/
uint8_t I2C_write(uint8_t command, uint8_t data)
{
  Wire.beginTransmission(AS1130ADDRESS); 
  Wire.write(command); 
  Wire.write(data); 
  int ack = Wire.endTransmission(); 
    #ifdef DEBUG
      if (ack != 0) 
      {
        Serial.print("Error: ");
        Serial.print(ack);
        Serial.print("\r\n");
      }
    #endif
  return ack;
}

/***** Function to write configuration settings to I2C bus ***************************/
void as_config(uint8_t ram, uint8_t command, uint8_t data)
{
  I2C_write(REGISTERSELECTION, ram);
  I2C_write(command, data);
}

#ifdef DEBUG_STATUS
/***** Function to read status registers from I2C bus ***************************/
uint8_t I2C_read_Status()
{
  char* statusStrings[]={
  "Ack: ", "Picture: ", "Movie: ", "Movie Mode: ", "Frame Time/Scroll: ", "Display Option: ",
  "Current Source: ", "AS1130 Config: ", "Interrupt Mask: ", "Interrupt Frame Definition: ",
  "Shutdown & Open/Short: ", "I2C Interface Monitoring: ", "CLK Synchronization: ",
  "Interrupt Status: ", "AS1130 Status: ",
  }; 
  Serial.begin(9600);
  uint8_t status_byte = 0; 
  uint8_t strng = 0;
  Wire.beginTransmission(AS1130ADDRESS); 
  Wire.write(REGISTERSELECTION);
  Wire.write(CONTROLREGISTER); 
  Wire.write(PICTURE);
  Wire.endTransmission();
  Serial.print("Sending Read request:\r\n");
  Wire.beginTransmission(AS1130ADDRESS); 
  Wire.requestFrom(AS1130ADDRESS,15); 
  delay(10);
  while(Wire.available())
  {
    status_byte = Wire.read();
    Serial.print(statusStrings[strng]);
    Serial.print(status_byte,BIN);
    Serial.print("\r\n");
    strng++;
    delay(10);
  } 
  Serial.print("____________________________________________________________________\r\n");
  Wire.endTransmission();
}
#endif  
  
  
void setup()
{
    #ifdef DEBUG
      Serial.begin(9600);
      Serial.println("AS1130 example code\r\n");
      delay(debug_delay);
    #endif
    #ifdef DEBUG_DATA_UPLOAD
      Serial.begin(9600);
    #endif  
    #ifdef DEBUG_INTERRUPT
      Serial.begin(9600);
    #endif    
 
  Wire.begin();                     // start up I2C bus
  attachInterrupt(0, ISR_Handler, CHANGE);
  
/***** Start-up sequence as per datasheet - see Page 13 ******************************/
// (1) define ram configuration - see table 20 page 25
// (2) Fill the On/Off Frames with our data
// (3) Set-up Blink & PWM sets
// (4) Set-up Dot Correction (if required)
// (5) Define Control Registers - see table 13 page 20 
// (6) Define Current Source (0 to 30mA) - see table 19 page 24
// (7) Define Display Options
// (8) Start Display (Picture or Movie) Movie takes precedence over Picture


// (1) define ram configuration
  as_config(CONTROLREGISTER, AS1130CONFIG, 0b00000110);  // 0b00000110 = ram config 6 (Table 20, Page 25)
// (2) Fill the On/Off Frames with our data
//  this sends 2 bytes of data for each Current Segment in each frame
//  So:
//  CS0 is addressed at 0x00 and 0x01.
//  The first byte is LEDs 00 - 07 and the second byte is LEDs 08 - 0A
//  The 3 MSB of the second byte holds the Blink & PWM dataset number for the frame.
//  Likewise CS1 is addressed at 0x02 & 0x03, CS2 at 0x04 & 0x05 etc.
//  but no PWM set number is required.
int data = 0;
        #ifdef DEBUG
          Serial.print("Start of Frames Data Upload\r\n");
          delay(debug_delay);
        #endif
 for (int i=FRAME0; i<=FRAME5; i++)    
  {
    for (int j=0x00; j<=0x0B; j++)  // 0x00 to 0x0b are the Current Segments in each frame (CS0-CS11)
    {

      as_config(i, 2*j+1, Frames_Data[data]);    // i = frame address, 2*j+1 = CS register address (odd numbers) then second data byte
        #ifdef DEBUG_DATA_UPLOAD
          Serial.print("Frame number: ");
          Serial.print(i);
          Serial.print("  Current Segment: ");
          Serial.print(j);
          Serial.print("\r\nData 2nd Byte: ");
          Serial.print(Frames_Data[data]);
          Serial.print("\r\n");
        #endif
      data++;
      as_config(i, 2*j,   Frames_Data[data]);    // i = frame address, 2*j = CS register address (even numbers) then first data byte
        #ifdef DEBUG_DATA_UPLOAD
          Serial.print("Data 1st Byte: ");
          Serial.print(Frames_Data[data]);
          Serial.print("\r\n\r\n");
        #endif  
      data++;      
    }
  }
 // (3) Set-up Blink & PWM sets
/***** Clear Blink and write PWM Sets 1-5 *****************************************************/
//See Table 10 page 16
//Each LED in each Current Segment can be set to blink (the blink period is set in the Display Option Register [page 24]) 
//In this case blinking is turned off
  data = 0;   // Reset dataset counter
        #ifdef DEBUG_DATA_UPLOAD
          Serial.print("Start of Blink & PWM Data Upload\r\n");
          Serial.print("     Note: All Blink Frame data is set to 0 in this demo\r\n");
          delay(debug_delay);
        #endif
  for (int i=BLINK_PWM0; i<=BLINK_PWM5; i++)   // 0x40 to 0x45 are the addresses of the Blink & PWM Sets (0-5)
  {
    for (int j=0x00; j<=0x17; j++) // 0x00 to 0x17 are the addresses of the Blink Frame Registers for each Current Segment
    {
      as_config(i, j, 0x00);       // i= set number, j = address of Blink Frame, 0x00 = data byte
    }
    for (int k=0x18; k<=0x9b; k++) // 0x18 to 0x9B are the addresses of each individual LEDs PWM Register (132 LEDs can be set from 0 to 255 individually) 
    {
      as_config(i, k, PWM_Data[data]);       // i= set number, k = LED PWM Register for each individual LED,  data byte [0 -255]
        #ifdef DEBUG_DATA_UPLOAD
          Serial.print("Blink & PWM Set number: ");
          Serial.print(i-0x40);
          Serial.print("  LED Number: ");      
          Serial.print(k-0x18);
          Serial.print("\r\n      PWM Data Byte: ");
          Serial.print(PWM_Data[data]);
          Serial.print("\r\n");
        #endif
      data++;
    } 
  }
        #ifdef DEBUG
          Serial.print("End of Frames Data Upload\r\n");
          delay(debug_delay);
        #endif   
// (4) Set-up Dot Correction - NOT Required in this demo

// (5) Define Control Registers - see table 13 page 20 
    #ifdef DEBUG
      Serial.print("Start of Config sequence\r\n");
      delay(debug_delay);
    #endif
    

  as_config(CONTROLREGISTER, INTERRUPTMASK, 0b10100001);    // Interrupt when movie ends (Table 21, Page 26)
  as_config(CONTROLREGISTER, INTERRUPTFRAME, 0b00000101);    // generate interrupt after a frame (Table 22, Page 26)
//  as_config(CONTROLREGISTER, I2CINTERFACE, 0xFF);          // 0xff = default (Table 24, Page 27)
//  as_config(CONTROLREGISTER, CLKSYNC , 0x00);              // 0x00 = default (Table 25, Page 27)

// (6) Define Current Source
  as_config(CONTROLREGISTER, CURRENTSOURCE, 0xFF);           // brightness current set to 30mA (Table 19, Page 24)
// (7) Define Display Options
//  as_config(CONTROLREGISTER, PICTURE, 0b01000110);         // 0b01000000 = display picture (bits 0 - 5 are frame number to display (Table 14, Page 21)
  as_config(CONTROLREGISTER, MOVIEMODE, 0b00000101);         // number of frames to play (Table 16, Page 22) Note: Movie Mode overrides Picture Mode
  as_config(CONTROLREGISTER, FRAMETIME, 0b11010100);         //delay time between frames (Table 17, Page 23)
  as_config(CONTROLREGISTER, DISPLAYOPTION, 0b11101011);     // play movie endlessly and scan CS0 to CS11 in each frame (Table 18, Page 24)
  as_config(CONTROLREGISTER, MOVIE, 0b01000000);             // start movie - first frame is chosen by 6 least significant bits (Table 16, Page 22)
  as_config(CONTROLREGISTER, SHUTDOWNOPENSHORT, 0b00000011); // Enable the LEDs (ie make them visible)    
    #ifdef DEBUG
      Serial.print("End of Config sequence\r\n");
      delay(debug_delay);
    #endif  
}

void loop() 
{
// (8) Start Display  
  #ifdef DEBUG
    Serial.print("Main loop started\r\n");
    delay(debug_delay);
  #endif
  #ifdef DEBUG_STATUS
    I2C_read_Status();
    delay(5000);
  #endif
  delay(5000);
  as_config(CONTROLREGISTER, FRAMETIME, 0b11010001);
  delay(5000);
  as_config(CONTROLREGISTER, FRAMETIME, 0b01010001);
  delay(5000);
  as_config(CONTROLREGISTER, FRAMETIME, 0b01010111);
  delay(5000);
  as_config(CONTROLREGISTER, FRAMETIME, 0b11010111);
  delay(5000);
  as_config(CONTROLREGISTER, FRAMETIME, 0b10010001);
  delay(5000);
  as_config(CONTROLREGISTER, FRAMETIME, 0b00010001);
  delay(5000);
  as_config(CONTROLREGISTER, FRAMETIME, 0b00010111);
  delay(5000);
  as_config(CONTROLREGISTER, FRAMETIME, 0b10010111);  
/*
//Use this for Picture mode
  for(int frame = FRAME0; frame <= FRAME35; frame++)   // Show 36 frames
   {
    as_config(CONTROLREGISTER, PICTURE, frame);
    delay(delay_ms);
   }
*/
}

