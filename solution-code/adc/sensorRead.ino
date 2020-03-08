

int sensor = A0; //declare pin A0 where potentiometer is connected 

void setup(){ 
    pinMode(sensor, INPUT); //set potentiometer as input 
    Serial.begin(9600); //bits per second   
} 

void loop(){ 
    Serial.println(analogRead(sensor)); 
    delay(200); 
}