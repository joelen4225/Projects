#include <FastLED.h>

#define NUM_LEDS 60
#define DATA_PIN 2
#define CLOCK_PIN 13

int gHue = 0;
int state = 0;

CRGB leds[NUM_LEDS];

void setup() 
{ 
    FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);
    pinMode(DATA_PIN, OUTPUT);
    digitalWrite(DATA_PIN, LOW);
    Serial.begin(38400);
}

void loop() 
{ 
  if (Serial.available() > 0)
  {
    state = Serial.read();
  }

  if (state == '0')
  {
    FastLED.setBrightness(25);
    BlackLED();
    FastLED.show();
  }

  if (state == '1')
  {
    FastLED.setBrightness(150);
    OceanWave();
    FastLED.show();
  }

  if (state == '2')
  {
    FastLED.setBrightness(150);
    CloudWave();
    FastLED.show();
  }

  if (state == '3')
  {
    FastLED.setBrightness(150);
    RainbowWave();
    FastLED.show();
  }

  if (state == '4')
  {
    FastLED.setBrightness(150);
    ForestwWave();
    FastLED.show();
  }

  if (state == '5')
  {
    FastLED.setBrightness(150);
    LavaWave();
    FastLED.show();
  }

  if (state == '6')
  {
    FastLED.setBrightness(150);
    RedLED();
    FastLED.show();
  }

  if (state == '7')
  {
    FastLED.setBrightness(150);
    OrangeLED();
    FastLED.show();
  }

  if (state == '8')
  {
    FastLED.setBrightness(150);
    YellowLED();
    FastLED.show();
  }

  if (state == '9')
  {
    FastLED.setBrightness(150);
    GreenLED();
    FastLED.show();
  }

  if (state == 'a')
  {
    FastLED.setBrightness(150);
    BlueLED();
    FastLED.show();
  }

  if (state == 'b')
  {
    FastLED.setBrightness(150);
    PurpleLED();
    FastLED.show();
  }

  if (state == 'c')
  {
    FastLED.setBrightness(150);
    PinkLED();
    FastLED.show();
  }

  if (state == 'd')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      OceanWave();
      FastLED.show();
    }
  }

  if (state == 'e')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      CloudWave();
      FastLED.show();
    }
  }

  if (state == 'f')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      RainbowWave();
      FastLED.show();
    }
  }

  if (state == 'g')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      ForestWave();
      FastLED.show();
    }
  }

  if (state == 'h')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      LavaWave();
      FastLED.show();
    }
  }

  if (state == 'i')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      RedLED();
      FastLED.show();
    }
  }

  if (state == 'j')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      OrangeLED();
      FastLED.show();
    }
  }

  if (state == 'k')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      YellowLED();
      FastLED.show();
    }
  }

  if (state == 'l')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      Green();
      FastLED.show();
    }
  }

  if (state == 'm')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      BlueLED();
      FastLED.show();
    }
  }

  if (state == 'n')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      PurpleLED();
      FastLED.show();
    }
  }

  if (state == 'o')
  {
    if (digitalRead(7) == 0)
    {
      FastLED.setBrightness(25);
      BlackLED();
      FastLED.show();
    }
    if (digitalRead(7) == 1)
    {
      FastLED.setBrightness(150);
      PinkLED();
      FastLED.show();
    }
  }
}


void BlackLED()
{
  for( int i = 0; i < NUM_LEDS; i++) 
  { 
    leds[i] = CHSV(0, 0, 0);
  }
}

void RedLED()
{
  for (int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = CRGB(255, 0, 0);
  }
}

void OrangeLED()
{
  for (int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = CRGB(255, 128, 0);
  }
}

void YellowLED()
{
  for (int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = CRGB(255, 255, 0);
  }
}

void GreenLED()
{
  for (int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = CRGB(0, 255, 0);
  }
}

void BlueLED()
{
  for (int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = CRGB(0, 0, 255);
  }
}

void PurpleLED()
{
  for (int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = CRGB(255, 0, 255);
  }
}

void PinkLED()
{
  for (int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = CRGB(255, 0, 128);
  }
}

void OceanWave()
{
  int BeatsPerMinute = 62;
  CRGBPalette16 palette = OceanColors_p;
  int beat = beatsin8(BeatsPerMinute, 64, 255);
  
  for( int i = 0; i < NUM_LEDS; i++) 
  { 
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void CloudWave()
{
  int BeatsPerMinute = 62;
  CRGBPalette16 palette = CloudColors_p;
  int beat = beatsin8(BeatsPerMinute, 64, 255);
  
  for( int i = 0; i < NUM_LEDS; i++) 
  { 
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void RainbowWave()
{
  int BeatsPerMinute = 62;
  CRGBPalette16 palette = RainbowColors_p;
  int beat = beatsin8(BeatsPerMinute, 64, 255);
  
  for( int i = 0; i < NUM_LEDS; i++) 
  { 
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void ForestWave()
{
  int BeatsPerMinute = 62;
  CRGBPalette16 palette = ForestColors_p;
  int beat = beatsin8(BeatsPerMinute, 64, 255);
  
  for( int i = 0; i < NUM_LEDS; i++) 
  { 
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void LavaWave()
{
  int BeatsPerMinute = 62;
  CRGBPalette16 palette = LavaColors_p;
  int beat = beatsin8(BeatsPerMinute, 64, 255);
  
  for( int i = 0; i < NUM_LEDS; i++) 
  { 
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}
