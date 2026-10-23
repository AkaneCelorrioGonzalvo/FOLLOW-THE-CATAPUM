#include <Arduino.h>

// ============================================================
// CONFIGURACIÓN
// ============================================================

const uint32_t BAUDRATE_SERIAL = 115200;
const uint32_t INTERVALO_ENVIO_MS = 200;  // 5 Hz
const float GRAVEDAD = 9.80665f;

uint32_t tiempo_anterior_envio = 0;

float vel_max = 0.0f;
float altura_max = 0.0f;


// ============================================================
// INICIALIZAR SERIAL USB
// ============================================================

void inicializarSerial(uint32_t baudrate)
{
    Serial.begin(baudrate);

    uint32_t inicio = millis();

    while (!Serial && millis() - inicio < 3000UL)
    {
        delay(10);
    }

    randomSeed(micros() ^ analogRead(A0));

    // No enviar mensajes de arranque:
    // Python espera muestras con los 15 campos.
}


// ============================================================
// GENERAR VALOR ALEATORIO
// ============================================================

float aleatorioFloat(float minimo, float maximo)
{
    return minimo +
           (maximo - minimo) * random(0, 100001) / 100000.0f;
}


// ============================================================
// ENVIAR TELEMETRÍA SIMULADA EN JSON
// ============================================================

void enviarDato()
{
    // Simular aceleraciones en m/s² y convertirlas a G.
    // La interfaz Python muestra G.
    float acc_x = aleatorioFloat(-20, 20) / GRAVEDAD;
    float acc_y = aleatorioFloat(-20, 20) / GRAVEDAD;
    float acc_z = aleatorioFloat(-20, 20) / GRAVEDAD;

    // Orientación en grados
    float pitch = aleatorioFloat(-90, 90);
    float roll  = aleatorioFloat(-180, 180);
    float yaw   = aleatorioFloat(0, 360);

    // Velocidad en m/s
    float vel = aleatorioFloat(0, 300);

    if (vel > vel_max)
        vel_max = vel;

    // Coordenadas en grados.
    // Usar double para conservar precisión.
    double latitud =
        random(41640000L, 41660001L) / 1000000.0;

    double longitud =
        random(-900000L, -869999L) / 1000000.0;

    // Altura en metros
    float altura = aleatorioFloat(0, 1200);

    if (altura > altura_max)
        altura_max = altura;

    // Temperatura en °C
    float temperatura = aleatorioFloat(15, 45);

    // Códigos elegidos SOLO para esta simulación:
    // 0 = REPOSO
    // 1 = ASCENSO
    // 2 = DESCENSO
    // 3 = ATERRIZAJE
    //
    // La app no define esta equivalencia.
    int estado = random(0, 4);

    // Conservar la simulación 0/1, enviándola como entero.
    // Python también admite otros enteros para flag.
    int flag = random(0, 2);

    Serial.print("{");

    Serial.print("\"acc_x\":");
    Serial.print(acc_x, 3);

    Serial.print(",\"acc_y\":");
    Serial.print(acc_y, 3);

    Serial.print(",\"acc_z\":");
    Serial.print(acc_z, 3);

    Serial.print(",\"pitch\":");
    Serial.print(pitch, 2);

    Serial.print(",\"roll\":");
    Serial.print(roll, 2);

    Serial.print(",\"yaw\":");
    Serial.print(yaw, 2);

    Serial.print(",\"vel\":");
    Serial.print(vel, 2);

    Serial.print(",\"vel_max\":");
    Serial.print(vel_max, 2);

    Serial.print(",\"latitud\":");
    Serial.print(latitud, 6);

    Serial.print(",\"longitud\":");
    Serial.print(longitud, 6);

    Serial.print(",\"altura\":");
    Serial.print(altura, 2);

    Serial.print(",\"altura_max\":");
    Serial.print(altura_max, 2);

    Serial.print(",\"temperatura\":");
    Serial.print(temperatura, 1);

    // Enteros sin comillas y sin true/false.
    Serial.print(",\"estado\":");
    Serial.print(estado);

    Serial.print(",\"flag\":");
    Serial.print(flag);

    Serial.println("}");
}


// ============================================================
// ENVÍO PERIÓDICO
// ============================================================

void ejecutarEnvioPeriodico()
{
    if (!Serial)
        return;

    uint32_t tiempo_actual = millis();

    if (tiempo_actual - tiempo_anterior_envio >= INTERVALO_ENVIO_MS)
    {
        tiempo_anterior_envio = tiempo_actual;
        enviarDato();
    }
}


// ============================================================
// SETUP Y LOOP
// ============================================================

void setup()
{
    inicializarSerial(BAUDRATE_SERIAL);
}

void loop()
{
    ejecutarEnvioPeriodico();
}