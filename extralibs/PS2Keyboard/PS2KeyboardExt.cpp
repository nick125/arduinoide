/*
  PS2KeyboardExt.cpp - PS2Keyboard library extension
  Copyright (c) 2008 Free Software Foundation.  All right reserved.
  Written by Nir Jacobson <nirj@pacbell.net>
  Original PS2Keyboard library written by Christian Weichel <info@32leaves.net>

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/

#include <ctype.h>

byte val = 0;
byte capslk = 0;

// set the number of characters in each type (functions, numbers, letters, punctuations)
#define numFuncts 6
#define numNums 10
#define numLetts 26
#define numPuncs 14


PROGMEM prog_uchar functs_byte[numFuncts] = {0x5a, 0x29, 0x0D, 0x66, 0x58, 0x76};			// functions' byte array
													// in order: return, space, tab, backspace, capslock, escape

PROGMEM prog_uchar nums_upper[numNums] = {')', '!', '@', '#', '$', '%', '^', '&', '*', '('};		// numbers' corresponding alternate character array
PROGMEM prog_uchar nums[numNums] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};			// numbers array
PROGMEM prog_uchar nums_byte[numNums] = {0x45, 0x16, 0x1e, 0x26, 0x25, 0x2e, 0x36, 0x3d, 0x3e, 0x46};	// numbers' corresponding bytes array


PROGMEM prog_uchar letts[numLetts] = {'a', 'b', 'c', 'd', 'e', 'f',					// letters array
				      'g', 'h', 'i', 'j', 'k', 'l',
				      'm', 'n', 'o', 'p', 'q', 'r',
                                      's', 't', 'u', 'v', 'w', 'x',
				      'y', 'z'};
PROGMEM prog_uchar letts_byte[numLetts] = {0x1c, 0x32, 0x21, 0x23, 0x24, 0x2b,				// letters' corresponding bytes array
					   0x34, 0x33, 0x43, 0x3b, 0x42, 0x4b,
                                           0x3a, 0x31, 0x44, 0x4d, 0x15, 0x2d,
                                           0x1b, 0x2c, 0x3c, 0x2a, 0x1d, 0x22,
                                           0x35, 0x1a};

PROGMEM prog_uchar puncs_upper[numPuncs] = {'~', '_', '+', '{', '}', '|', ':',				// punctuations' corresponding alternate character array
					    '"', '<', '>', '?', '*', '-', '+'};
PROGMEM prog_uchar puncs[numPuncs] = {'`', '-', '=', '[', ']', '\\', ';',				// punctuations array					
				      '\'', ',', '.', '/', '*', '-', '+'};
PROGMEM prog_uchar puncs_byte[numPuncs] = {0x0e, 0x4e, 0x55, 0x54, 0x5b, 0x5d, 0x4c,			// punctuations' corresponding bytes array
					   0x52, 0x41, 0x49, 0x4a, 0x7c, 0x7b, 0x79};

byte getKeyType(byte keyByte) {                    // checks which array (functions, numbers, letters or punctuations)
                                                   // the received byte belongs to and returns a corresponding
                                                   // digit (1, 2, 3 or 4)

  int i = 0;
                                                   
  for (i = 0; i < numFuncts; i++)                  // for each value of the functions' byte array
  {
    val = pgm_read_byte_near(functs_byte + i);     
    if (keyByte == val)                            //   check if keyByte matches it
    {
      return 1;                                    //     if so, return 1 for 'function'
    }
  }                                                // if none match, check the remaining types' bytes array
  
  for (i = 0; i < numNums; i++)                    // for each value of the numbers' byte array
  {
    val = pgm_read_byte_near(nums_byte + i);
    if (keyByte == val)                            //   check if keyByte matches it
    {
      return 2;                                    //     if so, return 2 for 'number'
    }
  }                                                // if none match, check the remaining types' bytes array
  for (i = 0; i < numLetts; i++)
  {
    val = pgm_read_byte_near(letts_byte + i);
    if (keyByte == val)
    {
      return 3;                                    // return 3 for 'letter'
    }
  }
  for (i = 0; i < numPuncs; i++)
  {
    val = pgm_read_byte_near(puncs_byte + i);
    if (keyByte == val)
    {
      return 4;                                    // return 4 for 'punctuation'
    }
  }
  return 0;
}

char getKeyChar(byte keyByte, byte keyType)        // checks the array of character type keyType
                                                   // for the byte keyByte, and returns its corresponding character
{
  if (keyType == 2) {                              // if keyType is 2 for 'number'
    for (int i = 0; i < numNums; i++)              //   then for each value of the numbers' bytes array
    {
      val = pgm_read_byte_near(nums_byte + i);
      if (keyByte == val)                          //     check if keyByte matches it
      {
        if (capslk == 0)                           //       if so, check for capslock and retrieve the appropriate corresponding character
        {
          val = pgm_read_byte_near(nums + i);
        } else {
          val = pgm_read_byte_near(nums_upper + i);
        }
        return val;                                //       and return it
      }
    }
  } else if (keyType == 3) {                       // if keyType is 3 for 'letter'
    for (int i = 0; i < numLetts; i++)             //   then for each value of the letters' bytes array
    {
      val = pgm_read_byte_near(letts_byte + i);
      if (keyByte == val)                          //     check if keyByte matches it
      {
        val = pgm_read_byte_near(letts + i);       //       if so, get the corresponding character
        if (capslk == 1)                           //       and capitalize it if capslock is on
        {
          val = toupper(val);
        }
        return val;                                //       and return it
      }
    } 
  } else if (keyType == 4) {
    for (int i = 0; i < numPuncs; i++)
    {
      val = pgm_read_byte_near(puncs_byte + i);
      if (keyByte == val)			   //     check if keyByte matches it
      {
        if (capslk == 0)                           //       if so, check for capslock and retrieve the appropriate corresponding character
        {
          val = pgm_read_byte_near(puncs + i);
        } else {
          val = pgm_read_byte_near(puncs_upper + i);
        }
        return val;				   //       and return it
      }
    }
  } else {
    return 0;
  }
}

byte getKeyFunct(byte keyByte)                     // checks the functions array for byte keyByte
                                                   // and returns the position of the byte in the array
                                                   // starting from 1.
{
  for (int i = 0; i < numFuncts; i++)
  {
    val = pgm_read_byte_near(functs_byte + i);
    if (val == keyByte)
    {
      return i+1;
    }
  }
  return 0;
}
