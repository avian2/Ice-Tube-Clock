/* MSB -> 7 6 5 4   3 2 1 0 <- LSB

      7
     ___

 2 |     | 6
   |  1  |
     ___

 3 |     | 5
   |  4  |
     ___    O 0
*/
const uint8_t alphatable[] PROGMEM = {
	0xFA, /* a */
	0x3E, /* b */
	0x1A, /* c */
	0x7A, /* d */
	0xDE, /* e */
	0x8E, /* f */
	0xF6, /* g */
	0x2E, /* h */
	0x60, /* i */
	0x78, /* j */
	0xAE, //k
	0x1C, // l
	0xAA, // m
	0x2A, // n
	0x3A, // o
	0xCE, //p
	0xF3, // q
	0x0A, //r
	0xB6, //s
	0x1E, //t
	0x38, //u
	0x38, //v // fix?
	0xB8, //w
	0x6E, //x
	0x76, // y
	0xDA, //z
	/* more */
};
PGM_P alphatable_p PROGMEM = alphatable;

const uint8_t numbertable[] PROGMEM = { 
  0xFC /* 0 */, 
  0x60 /* 1 */,
  0xDA /* 2 */,
  0xF2 /* 3 */,
  0x66 /* 4 */,
  0xB6 /* 5 */,
  0xBE, /* 6 */
  0xE0, /* 7 */
  0xFE, /* 8 */
  0xF6, /* 9 */
};
PGM_P numbertable_p PROGMEM = numbertable;
