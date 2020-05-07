#include <FastLED.h>

// How many leds in your strip?
#define NUM_LEDS 60

#define DATA_PIN 2
#define CLOCK_PIN 13

int gHue = 0;

// Define the array of leds
CRGB leds[NUM_LEDS];

void setup() 
{ 
    FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);  // GRB ordering is assumed
}

void loop() 
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


void BlackLED()
{
  for( int i = 0; i < NUM_LEDS; i++) 
  { 
    leds[i] = CHSV(0, 0, 0);
  }
}

void RainbowWave()
{
  // Rainbow Strip Pulsing at a Defined Beats-Per-Minute (BPM)
  int BeatsPerMinute = 62;
  CRGBPalette16 palette = OceanColors_p;  //Can Use CloudColors_p, RainbowStripeColors_p, ForestColors_p, or LavaColors_p 
  //(Lava and Forest May Be Switched)
    
  int beat = beatsin8(BeatsPerMinute, 64, 255);
  
  for( int i = 0; i < NUM_LEDS; i++) 
  { 
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}
