

int count=0;

void setup(){
    Serial.begin(9600);//bits per second 
}

void loop(){
    Serial.print(‘The current count is:’);
    Serial.println(count);
    count +=1;
    delay(1000);
}