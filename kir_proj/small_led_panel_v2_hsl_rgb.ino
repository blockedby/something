#include <GyverButton.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define BTN_menu 5
#define BTN_inc 3
#define BTN_dec 4

#define R 10
#define G 9
#define B 6


#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define LOGO_HEIGHT  64
#define LOGO_WIDTH    128
GButton Menu(BTN_menu);
GButton Inc(BTN_inc);
GButton Dec(BTN_dec);




int menu = 0;
int row = 0;
int r = 255;
int g = 255;
int b = 255;

int h = 0;
int s = 100;
int l = 50;

int r_hsl = 0;
int g_hsl = 0;
int b_hsl = 0;


void setup() {
  /*Menu.setDebounce(2);
    Inc.setDebounce(2);
    Dec.setDebounce(2);
  */
  Menu.setType(LOW_PULL);
  Inc.setType(LOW_PULL);
  Dec.setType(LOW_PULL);
  Menu.setTickMode(AUTO);
  Inc.setTickMode(AUTO);
  Dec.setTickMode(AUTO);
  // put your setup code here, to run once:
  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3D for 128x64
    Serial.println(F("SSD1306 allocation failed"));
    for (;;); // Don't proceed, loop forever
  }
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);



  display.setRotation(2);
  disp_menu(menu, row, r, g, b); //this function shows info on display
  disp_values();
  light(r, g, b);

  Serial.begin(9600);
}

void loop() {


  //Menu.tick(); //
  //Inc.tick();
  //Dec.tick();

  if (Menu.isClick())  //checks is menu button is clicked
  {
    //Serial.println("menu");
    if (row == 3)
    {
      row = 0;
    }
    else
    {
      row = row + 1;
    }
    disp_menu(menu, row, r, g, b); //this function shows info on display
    disp_values();
  }
  if (Inc.isClick())  //checks is Inc button is clicked
  {
    //Serial.println("inc");
    single_click(0, menu, row);
    if (row != 0)
    {
      switch (menu)
      {
        case 0:
          light(r, g, b);
          break;
        case 1:
          hsl_to_rgb();
          light_hsl(r_hsl, g_hsl, b_hsl);
          break;
      }
    }
    disp_values();  //displays current values
  }
  if (Dec.isClick())  //checks is Dec button is clicked
  {
    //Serial.println("dec");
    single_click(1, menu, row);
    if (row != 0)
    {
      switch (menu)
      {
        case 0:
          light(r, g, b);
          break;
        case 1:
          hsl_to_rgb();
          light_hsl(r_hsl, g_hsl, b_hsl);
          break;
      }
    }
    disp_values();  //displays current values
  }
  if (Inc.isHold())   //checks is Inc button is hold
  {
    button_hold(0, menu, row, Inc.getClicks());
    disp_values();  //displays current values
  }
  if (Dec.isHold())   //checks is Dec button is hols
  {
    button_hold(1, menu, row, Dec.getClicks());
    disp_values();  //displays current values
  }
  //light_time(r,g,b,2);     //lights the leds for some time
}

void light(int r, int g, int b)  //main function to power leds
{
  analogWrite(R, r);
  analogWrite(G, g);
  analogWrite(B, b);
}

void light_time(int r, int g, int b, int duration)  ////lights the leds for some time
{
  int counter = 0;
  while (counter < duration)
  {
    light(r, g, b);
    delay(1);
    counter++;
  }
}


void light_hsl(int r_hsl, int g_hsl, int b_hsl)  //main function to power leds
{
  analogWrite(R, r_hsl);
  analogWrite(G, g_hsl);
  analogWrite(B, b_hsl);
}

void light_time_hsl(int r_hsl, int g_hsl, int b_hsl, int duration)  ////lights the leds for some time
{
  int counter = 0;
  while (counter < duration)
  {
    light(r_hsl, g_hsl, b_hsl);
    delay(1);
    counter++;
  }
}

void single_click(int but, int cur_menu, int cur_row) //action on cur_but click
{
  switch (but)
  {
    case 0:
      switch (cur_row)
      {
        case 0:
          switch (cur_menu)
          {
            case 0:
              menu = 1;
              disp_menu(menu, row, r, g, b); //this function shows info on display
              break;
            case 1:
              menu = 0;
              disp_menu(menu, row, r, g, b); //this function shows info on display
              break;
          }
          break;
        case 1:
          switch (cur_menu)
          {
            case 0:
              if (r < 255) r = r + 1;
              break;
            case 1:
              if (h < 360) h = h + 1;
              break;
          }
          break;
        case 2:
          switch (cur_menu)
          {
            case 0:
              if (g < 255) g = g + 1;
              break;
            case 1:
              if (s < 100) s = s + 1;
              break;
          }
          break;
        case 3:
          switch (cur_menu)
          {
            case 0:
              if (b < 255) b = b + 1;
              break;
            case 1:
              if (l < 100) l = l + 1;
              break;
          }
          break;
      }
      break;
    case 1:
      switch (cur_row)
      {
        case 0:
          switch (cur_menu)
          {
            case 0:
              menu = 1;
              disp_menu(menu, row, r, g, b); //this function shows info on display
              break;
            case 1:
              menu = 0;
              disp_menu(menu, row, r, g, b); //this function shows info on display
              break;
          }
          break;
        case 1:
          switch (cur_menu)
          {
            case 0:
              if (r > 0) r = r - 1;
              break;
            case 1:
              if (h > 0) h = h - 1;
              break;
          }
          break;
        case 2:
          switch (cur_menu)
          {
            case 0:
              if (g > 0) g = g - 1;
              break;
            case 1:
              if (s > 0) s = s - 1;
              break;
          }
          break;
        case 3:
          switch (cur_menu)
          {
            case 0:
              if (b > 0) b = b - 1;
              break;
            case 1:
              if (l > 0) l = l - 1;
              break;
          }
          break;
      }
      break;
  }
}

void button_hold(int but, int cur_menu, int cur_row, int clicks)
{
  switch (but)
  {
    case 0:
      switch (cur_row)
      {
        case 1:
          switch (cur_menu)
          {
            case 0:
              while (Inc.isHold())
              {
                if (r < 250) r = r + 5;
                if (r > 249) r = 255;
                light_time(r, g, b, 50);
                disp_values();
              }
              break;
            case 1:
              while (Inc.isHold())
              {
                if (h < 355) h = h + 5;
                if (h > 354) h = 360;
                hsl_to_rgb();
                light_time_hsl(r_hsl, g_hsl, b_hsl, 50);
                disp_values();
              }
              break;
          }
          break;
        case 2:
          switch (cur_menu)
          {
            case 0:
              while (Inc.isHold())
              {
                if (g < 250) g = g + 5;
                if (g > 249) g = 255;
                light_time(r, g, b, 50);
                disp_values();
              }
              break;
            case 1:
              while (Inc.isHold())
              {
                if (s < 95) s = s + 5;
                if (s > 94) s = 100;
                hsl_to_rgb();
                light_time_hsl(r_hsl, g_hsl, b_hsl, 50);
                disp_values();
              }
              break;
          }
          break;
        case 3:
          switch (cur_menu)
          {
            case 0:
              while (Inc.isHold())
              {
                if (b < 250) b = b + 5;
                if (b > 249) b = 255;
                light_time(r, g, b, 50);
                disp_values();
              }
              break;
            case 1:
              while (Inc.isHold())
              {
                if (l < 95) l = l + 5;
                if (l > 94) l = 100;
                hsl_to_rgb();
                light_time_hsl(r_hsl, g_hsl, b_hsl, 50);
                disp_values();
              }
              break;
          }
          break;
      }
      break;
    case 1:
      switch (cur_row)
      {
        case 1:
          switch (cur_menu)
          {
            case 0:
              while (Dec.isHold())
              {
                if (r > 5) r = r - 5;
                if (r < 6) r = 0;
                light_time(r, g, b, 50);
                disp_values();
              }
              break;
            case 1:

              while (Dec.isHold())
              {
                if (h > 5) h = h - 5;
                if (h < 6) h = 0;
                hsl_to_rgb();
                light_time_hsl(r_hsl, g_hsl, b_hsl, 50);
                disp_values();
              }
              break;
          }
          break;
        case 2:
          switch (cur_menu)
          {
            case 0:
              while (Dec.isHold())
              {
                if (g > 5) g = g - 5;
                if (g < 6) g = 0;
                light_time(r, g, b, 50);
                disp_values();
              }
              break;
            case 1:
              while (Dec.isHold())
              {
                if (s > 5) s = s - 5;
                if (s < 6) s = 0;
                hsl_to_rgb();
                light_time_hsl(r_hsl, g_hsl, b_hsl, 50);
                disp_values();
              }
              break;
          }
          break;
        case 3:
          switch (cur_menu)
          {
            case 0:
              while (Dec.isHold())
              {
                if (b > 5) b = b - 5;
                if (b < 6) b = 0;
                light_time(r, g, b, 50);
                disp_values();
              }
              break;
            case 1:
              while (Dec.isHold())
              {
                if (l > 5) l = l - 5;
                if (l < 6) l = 0;
                hsl_to_rgb();
                light_time_hsl(r_hsl, g_hsl, b_hsl, 50);
                disp_values();
              }
              break;
          }
          break;
      }
      break;
  }
}

void disp_menu(int cur_menu, int cur_row, int rr, int gg, int bb) //this function shows info on display
{
  display.clearDisplay();
  display.setTextSize(2);             //2:1 pixel scale
  display.setTextColor(SSD1306_WHITE);        // Draw white text

  display.setCursor(0, 0);            // Start at top-left corner
  switch (cur_menu)
  {
    case 0:
      display.print(F("Mode:"));
      display.println(F(" RGB "));
      switch (cur_row)
      {
        case 0:
          display.setCursor(0, 0);
          display.print(F("Mode:"));
          display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
          display.println(F(" RGB "));
          display.setTextColor(SSD1306_WHITE);        // Draw white text

          break;
      }
      display.setCursor(0, 18);
      display.println(F("R:"));
      display.println(F("G:"));
      display.println(F("B:"));
      break;
    case 1:
      display.print(F("Mode:"));
      display.println(F(" HSL "));
      switch (cur_row)
      {
        case 0:
          display.setCursor(0, 0);
          display.print(F("Mode:"));
          display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
          display.println(F(" HSL "));
          display.setTextColor(SSD1306_WHITE);        // Draw white text

          break;
      }
      display.setCursor(0, 18);
      display.println(F("H:"));
      display.println(F("S:"));
      display.println(F("L:"));
      break;
  }

  display.drawLine(0, 16, 128, 16, SSD1306_WHITE);
  display.display();
}

void disp_values()  //displays current values
{
  display.fillRect(25, 18, 127, 63, SSD1306_BLACK);
  //display.display(); // Update screen with each newly-drawn rectangle
  switch (menu)
  {
    case 0:
      display.setCursor(25, 18);
      display.print(r);

      display.setCursor(25, 34);
      display.print(g);

      display.setCursor(25, 50);
      display.print(b);
      switch (row)
      {
        case 1:
          display.setCursor(25, 18);
          display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
          display.print(r);
          display.setTextColor(SSD1306_WHITE);        // Draw white text

          break;
        case 2:
          display.setCursor(25, 34);
          display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
          display.print(g);
          display.setTextColor(SSD1306_WHITE);        // Draw white text

          break;
        case 3:
          display.setCursor(25, 50);
          display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
          display.print(b);
          display.setTextColor(SSD1306_WHITE);        // Draw white text

          break;
      }
      display.display();
      break;
    case 1:
      display.setCursor(25, 18);
      display.print(h);

      display.setCursor(25, 34);
      display.print(s);

      display.setCursor(25, 50);
      display.print(l);
      
      display.setCursor(75, 18);
      display.print(r_hsl);

      display.setCursor(75, 34);
      display.print(g_hsl);

      display.setCursor(75, 50);
      display.print(b_hsl);
      switch (row)
      {
        case 1:
          display.setCursor(25, 18);
          display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
          display.print(h);
          display.setTextColor(SSD1306_WHITE);        // Draw white text

          break;
        case 2:
          display.setCursor(25, 34);
          display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
          display.print(s);
          display.setTextColor(SSD1306_WHITE);        // Draw white text

          break;
        case 3:
          display.setCursor(25, 50);
          display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
          display.print(l);
          display.setTextColor(SSD1306_WHITE);        // Draw white text

          break;
      }
      display.display();
      break;
  }

}


void hsl_to_rgb () //МАТЕМАТИКА
{
  double rr = 0;
  double gg = 0;
  double bb = 0;
  
  double hh = (double)h;  //360 100 100
  double ll = (double)l/100;
  double ss = (double)s/100;

  double var1 = 2 * ll - 1;
  double c = (1 - abs(var1)) * ss;
  double var3 = hh/60;
  double var2 = hh/60 - (int)var3 + (int)var3%2- 1;
  double x = c * (1 - abs(var2));
  double m = ll - c / 2;
  
  
  // Serial.print("\nvar1 ");
  // Serial.print(var1);
  // Serial.print(" c ");
  // Serial.print(c);
  // Serial.print("\nvar3 ");
  // Serial.print(var3);
  // Serial.print("\nvar2 ");
  // Serial.print(var2);
  // Serial.print(" x ");
  // Serial.print(x);
  // Serial.print("\nm ");
  // Serial.print(m);
  
  
  rr = (c + m) * 255;
  gg = (m) * 255;
  bb = (x + m) * 255;

  if ((h < 300) and (h > 239))
  {
    rr = (x + m) * 255;
    gg = (m) * 255;
    bb = (c + m) * 255;
  }
  if ((h < 240) and (h > 179))
  {
    rr = (m) * 255;
    gg = (x + m) * 255;
    bb = (c + m) * 255;
  }
  if ((h < 180) and (h > 119))
  {
    rr = (m) * 255;
    gg = (c + m) * 255;
    bb = (x + m) * 255;
  }
  if ((h < 120) and (h > 59))
  {
    rr = (x + m) * 255;
    gg = (c + m) * 255;
    bb = (m) * 255;
  }
  if ((h < 60) and (h > -1))
  {
    rr = (c + m) * 255;
    gg = (x + m) * 255;
    bb = (m) * 255;
  }
  r_hsl = (int)rr;
  g_hsl = (int)gg;
  b_hsl = (int)bb;
  
  // Serial.print("\nr_hsl ");
  // Serial.print(r_hsl);
  // Serial.print(" rr ");
  // Serial.print(rr);
  // Serial.print("\ng_hsl ");
  // Serial.print(g_hsl);
  // Serial.print(" gg ");
  // Serial.print(gg);
  // Serial.print("\nb_hsl ");
  // Serial.print(b_hsl);
  // Serial.print(" bb ");
  // Serial.print(bb);
  
}
// отдавать пакеты ргб\хсл 
// принимать пакеты цветов + меню + значение
// конектиться (мультиконнекшн)
// настравиать ргб и хсл в менюшке
// сохранять пресеты
 