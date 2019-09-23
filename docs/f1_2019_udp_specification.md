F1 2019 UDP SPECIFICATION
=========================

Based on the CodeMasters Forum post documenting the format:

    https://forums.codemasters.com/topic/38920-f1-2019-udp-specification/

 Editorial notes:

* Tables were included as images, we turned them into proper MarkDown tables, here.
* We changed driver name 'Wilheim Kaufmann' into 'Wilhelm Kaufmann'.
* Fixed PacketSessionData's field 'm_networkGame'. It should have type 'uint8', not 'unint8'.
* The FAQ entries that follow the UDP specification were omitted.
  They state two important facts that are needed to correctly interpret the packet structs:
  - The structs are packed (i.e, no padding).
  - The numeric fields are transferred in little-endian format.

OVERVIEW
--------

The F1 series of games support the outputting of key game data via a UDP data stream. This data can be interpreted by external apps or connected peripherals for a range of different uses, including providing additional telemetry information, customised HUD displays, motion platform hardware support or providing force feedback data for custom steering wheels. The following information is a summary of the data that is outputted so that developers of supporting hardware or software are able to configure these to work with the F1 game correctly. If the information you require is not contained here, or if you have any issues with the UDP data itself, then please let us know and a member of the dev team will respond to your query as soon as possible.

PACKET TYPES
------------

The main change for 2018 is the introduction of multiple packet types: each packet can now carry different types of data rather than having one packet which contains everything. A header has been added to each packet as well so that versioning can be tracked and it will be easier for applications to check they are interpreting the incoming data in the correct way.

Each packet has the following header:

```
struct PacketHeader
{
    uint16    m_packetFormat;         // 2019
    uint8     m_gameMajorVersion;     // Game major version - "X.00"
    uint8     m_gameMinorVersion;     // Game minor version - "1.XX"
    uint8     m_packetVersion;        // Version of this packet type, all start from 1
    uint8     m_packetId;             // Identifier for the packet type, see below
    uint64    m_sessionUID;           // Unique identifier for the session
    float     m_sessionTime;          // Session timestamp
    uint      m_frameIdentifier;      // Identifier for the frame the data was retrieved on
    uint8     m_playerCarIndex;       // Index of player's car in the array
};
```

| Packet Name   | ID | Description                               | Frequency       | Size
| ------------- | -- | ----------------------------------------- | --------------- | ----------
| Motion        |  0 | Contains motion data for player's car – only sent while player is in control | Menu setting    | 1343 bytes
| Session       |  1 | Data about the session – track, time left                                    | 2 per second    |  149 bytes
| Lap Data      |  2 | Data about all the lap times of cars in the session                          | Menu setting    |  843 bytes
| Event         |  3 | Various notable events that happen during a session                          | On event        |   32 bytes
| Participants  |  4 | List of participants in the session, mostly relevant for multiplayer         | Every 5 seconds | 1104 bytes
| Car Setups    |  5 | Packet detailing car setups for cars in the race                             | 2 per second    |  843 bytes
| Car Telemetry |  6 | Telemetry data for all cars                                                  | Menu settings   | 1347 bytes
| Car Status    |  7 | Status data for all cars such as damage                                      | Menu settings   | 1143 bytes

MOTION PACKET
-------------

The motion packet gives physics data for all the cars being driven. There is additional data for the car being driven with the goal of being able to drive a motion platform setup.

N.B. For the normalised vectors below, to convert to float values divide by 32767.0f. 16-bit signed values are used to pack the data and on the assumption that direction values are always between -1.0f and 1.0f.

Frequency: Rate as specified in menus
Size: 1343 bytes
Version: 1

```
struct CarMotionData
{
    float         m_worldPositionX;           // World space X position
    float         m_worldPositionY;           // World space Y position
    float         m_worldPositionZ;           // World space Z position
    float         m_worldVelocityX;           // Velocity in world space X
    float         m_worldVelocityY;           // Velocity in world space Y
    float         m_worldVelocityZ;           // Velocity in world space Z
    int16         m_worldForwardDirX;         // World space forward X direction (normalised)
    int16         m_worldForwardDirY;         // World space forward Y direction (normalised)
    int16         m_worldForwardDirZ;         // World space forward Z direction (normalised)
    int16         m_worldRightDirX;           // World space right X direction (normalised)
    int16         m_worldRightDirY;           // World space right Y direction (normalised)
    int16         m_worldRightDirZ;           // World space right Z direction (normalised)
    float         m_gForceLateral;            // Lateral G-Force component
    float         m_gForceLongitudinal;       // Longitudinal G-Force component
    float         m_gForceVertical;           // Vertical G-Force component
    float         m_yaw;                      // Yaw angle in radians
    float         m_pitch;                    // Pitch angle in radians
    float         m_roll;                     // Roll angle in radians
};

struct PacketMotionData
{
    PacketHeader    m_header;               // Header

    CarMotionData   m_carMotionData[20];    // Data for all cars on track

    // Extra player car ONLY data
    float         m_suspensionPosition[4];       // Note: All wheel arrays have the following order:
    float         m_suspensionVelocity[4];       // RL, RR, FL, FR
    float         m_suspensionAcceleration[4];   // RL, RR, FL, FR
    float         m_wheelSpeed[4];               // Speed of each wheel
    float         m_wheelSlip[4];                // Slip ratio for each wheel
    float         m_localVelocityX;              // Velocity in local space
    float         m_localVelocityY;              // Velocity in local space
    float         m_localVelocityZ;              // Velocity in local space
    float         m_angularVelocityX;            // Angular velocity x-component
    float         m_angularVelocityY;            // Angular velocity y-component
    float         m_angularVelocityZ;            // Angular velocity z-component
    float         m_angularAccelerationX;        // Angular velocity x-component
    float         m_angularAccelerationY;        // Angular velocity y-component
    float         m_angularAccelerationZ;        // Angular velocity z-component
    float         m_frontWheelsAngle;            // Current front wheels angle in radians
};
```

SESSION PACKET
--------------

The session packet includes details about the current session in progress.

Frequency: 2 per second
Size: 149 bytes
Version: 1

```
struct MarshalZone
{
    float  m_zoneStart;   // Fraction (0..1) of way through the lap the marshal zone starts
    int8   m_zoneFlag;    // -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
};

struct PacketSessionData
{
    PacketHeader    m_header;                   // Header

    uint8           m_weather;                  // Weather - 0 = clear, 1 = light cloud, 2 = overcast
                                                // 3 = light rain, 4 = heavy rain, 5 = storm
    int8            m_trackTemperature;         // Track temp. in degrees celsius
    int8            m_airTemperature;           // Air temp. in degrees celsius
    uint8           m_totalLaps;                // Total number of laps in this race
    uint16          m_trackLength;              // Track length in metres
    uint8           m_sessionType;              // 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P
                                                // 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ
                                                // 10 = R, 11 = R2, 12 = Time Trial
    int8            m_trackId;                  // -1 for unknown, 0-21 for tracks, see appendix
    uint8           m_formula;                  // Formula, 0 = F1 Modern, 1 = F1 Classic, 2 = F2,
                                                // 3 = F1 Generic
    uint16          m_sessionTimeLeft;          // Time left in session in seconds
    uint16          m_sessionDuration;          // Session duration in seconds
    uint8           m_pitSpeedLimit;            // Pit speed limit in kilometres per hour
    uint8           m_gamePaused;               // Whether the game is paused
    uint8           m_isSpectating;             // Whether the player is spectating
    uint8           m_spectatorCarIndex;        // Index of the car being spectated
    uint8           m_sliProNativeSupport;      // SLI Pro support, 0 = inactive, 1 = active
    uint8           m_numMarshalZones;          // Number of marshal zones to follow
    MarshalZone     m_marshalZones[21];         // List of marshal zones – max 21
    uint8           m_safetyCarStatus;          // 0 = no safety car, 1 = full safety car
                                                // 2 = virtual safety car
    unint8          m_networkGame;              // 0 = offline, 1 = online
};
```

LAP DATA PACKET
---------------

The lap data packet gives details of all the cars in the session.

Frequency: Rate as specified in menus
Size: 843 bytes
Version: 1

```
struct LapData
{
    float       m_lastLapTime;           // Last lap time in seconds
    float       m_currentLapTime;        // Current time around the lap in seconds
    float       m_bestLapTime;           // Best lap time of the session in seconds
    float       m_sector1Time;           // Sector 1 time in seconds
    float       m_sector2Time;           // Sector 2 time in seconds
    float       m_lapDistance;           // Distance vehicle is around current lap in metres – could
                                         // be negative if line hasn’t been crossed yet
    float       m_totalDistance;         // Total distance travelled in session in metres – could
                                         // be negative if line hasn’t been crossed yet
    float       m_safetyCarDelta;        // Delta in seconds for safety car
    uint8       m_carPosition;           // Car race position
    uint8       m_currentLapNum;         // Current lap number
    uint8       m_pitStatus;             // 0 = none, 1 = pitting, 2 = in pit area
    uint8       m_sector;                // 0 = sector1, 1 = sector2, 2 = sector3
    uint8       m_currentLapInvalid;     // Current lap invalid - 0 = valid, 1 = invalid
    uint8       m_penalties;             // Accumulated time penalties in seconds to be added
    uint8       m_gridPosition;          // Grid position the vehicle started the race in
    uint8       m_driverStatus;          // Status of driver - 0 = in garage, 1 = flying lap
                                         // 2 = in lap, 3 = out lap, 4 = on track
    uint8       m_resultStatus;          // Result status - 0 = invalid, 1 = inactive, 2 = active
                                         // 3 = finished, 4 = disqualified, 5 = not classified
                                         // 6 = retired
};

struct PacketLapData
{
    PacketHeader    m_header;              // Header

    LapData         m_lapData[20];         // Lap data for all cars on track
};
```

EVENT PACKET
------------

This packet gives details of events that happen during the course of the race.

Frequency: When the event occurs
Size: 32 bytes
Version: 1

```
struct PacketEventData
{
    PacketHeader    m_header;               // Header
    
    uint8           m_eventStringCode[4];   // Event string code, see above
};
```

| Event           | Code   | Description                  |
| --------------- | ------ | ---------------------------- |
| Session Started | "SSTA" | Sent when the session starts |
| Session Ended   | "SEND" | Sent when the session ends   |

PARTICIPANTS PACKET
-------------------

This is a list of participants in the race. If the vehicle is controlled by AI, then the name will be the driver name. If this is a multiplayer game, the names will be the Steam Id on PC, or the LAN name if appropriate.

N.B. on Xbox One, the names will always be the driver name, on PS4 the name will be the LAN name if playing a LAN game, otherwise it will be the driver name.

The array should be indexed by vehicle index. 

Frequency: Every 5 seconds
Size: 1104 bytes
Version: 1

```
struct ParticipantData
{
    uint8      m_aiControlled;           // Whether the vehicle is AI (1) or Human (0) controlled
    uint8      m_driverId;               // Driver id - see appendix
    uint8      m_teamId;                 // Team id - see appendix
    uint8      m_raceNumber;             // Race number of the car
    uint8      m_nationality;            // Nationality of the driver
    char       m_name[48];               // Name of participant in UTF-8 format – null terminated
                                         // Will be truncated with … (U+2026) if too long
    uint8      m_yourTelemetry;          // The player's UDP setting, 0 = restricted, 1 = public
};

struct PacketParticipantsData
{
    PacketHeader    m_header;            // Header

    uint8           m_numActiveCars;           // Number of active cars in the data – should match number of
                                               // cars on HUD
    ParticipantData m_participants[20];
};
```

CAR SETUPS PACKET
-----------------

This packet details the car setups for each vehicle in the session. Note that in multiplayer games, other player cars will appear as blank, you will only be able to see your car setup and AI cars.

Frequency: 2 per second
Size: 843 bytes
Version: 1

```
struct CarSetupData
{
    uint8     m_frontWing;                // Front wing aero
    uint8     m_rearWing;                 // Rear wing aero
    uint8     m_onThrottle;               // Differential adjustment on throttle (percentage)
    uint8     m_offThrottle;              // Differential adjustment off throttle (percentage)
    float     m_frontCamber;              // Front camber angle (suspension geometry)
    float     m_rearCamber;               // Rear camber angle (suspension geometry)
    float     m_frontToe;                 // Front toe angle (suspension geometry)
    float     m_rearToe;                  // Rear toe angle (suspension geometry)
    uint8     m_frontSuspension;          // Front suspension
    uint8     m_rearSuspension;           // Rear suspension
    uint8     m_frontAntiRollBar;         // Front anti-roll bar
    uint8     m_rearAntiRollBar;          // Rear anti-roll bar
    uint8     m_frontSuspensionHeight;    // Front ride height
    uint8     m_rearSuspensionHeight;     // Rear ride height
    uint8     m_brakePressure;            // Brake pressure (percentage)
    uint8     m_brakeBias;                // Brake bias (percentage)
    float     m_frontTyrePressure;        // Front tyre pressure (PSI)
    float     m_rearTyrePressure;         // Rear tyre pressure (PSI)
    uint8     m_ballast;                  // Ballast
    float     m_fuelLoad;                 // Fuel load
};

struct PacketCarSetupData
{
    PacketHeader    m_header;            // Header

    CarSetupData    m_carSetups[20];
};
```

CAR TELEMETRY PACKET
--------------------

This packet details telemetry for all the cars in the race. It details various values that would be recorded on the car such as speed, throttle application, DRS etc.

Frequency: Rate as specified in menus
Size: 1347 bytes
Version: 1

```
struct CarTelemetryData
{
    uint16    m_speed;                      // Speed of car in kilometres per hour
    float     m_throttle;                   // Amount of throttle applied (0.0 to 1.0)
    float     m_steer;                      // Steering (-1.0 (full lock left) to 1.0 (full lock right))
    float     m_brake;                      // Amount of brake applied (0.0 to 1.0)
    uint8     m_clutch;                     // Amount of clutch applied (0 to 100)
    int8      m_gear;                       // Gear selected (1-8, N=0, R=-1)
    uint16    m_engineRPM;                  // Engine RPM
    uint8     m_drs;                        // 0 = off, 1 = on
    uint8     m_revLightsPercent;           // Rev lights indicator (percentage)
    uint16    m_brakesTemperature[4];       // Brakes temperature (celsius)
    uint16    m_tyresSurfaceTemperature[4]; // Tyres surface temperature (celsius)
    uint16    m_tyresInnerTemperature[4];   // Tyres inner temperature (celsius)
    uint16    m_engineTemperature;          // Engine temperature (celsius)
    float     m_tyresPressure[4];           // Tyres pressure (PSI)
    float     m_surfaceType[4];             // Driving surface, see appendices
};

struct PacketCarTelemetryData
{
    PacketHeader        m_header;                // Header

    CarTelemetryData    m_carTelemetryData[20];

    uint32              m_buttonStatus;         // Bit flags specifying which buttons are being pressed
                                                // currently - see appendices
};
```

CAR STATUS PACKET
-----------------

This packet details car statuses for all the cars in the race. It includes values such as the damage readings on the car.

Frequency: Rate as specified in menus
Size: 1143 bytes

```
struct CarStatusData
{
    uint8       m_tractionControl;          // 0 (off) - 2 (high)
    uint8       m_antiLockBrakes;           // 0 (off) - 1 (on)
    uint8       m_fuelMix;                  // Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
    uint8       m_frontBrakeBias;           // Front brake bias (percentage)
    uint8       m_pitLimiterStatus;         // Pit limiter status - 0 = off, 1 = on
    float       m_fuelInTank;               // Current fuel mass
    float       m_fuelCapacity;             // Fuel capacity
    float       m_fuelRemainingLaps;        // Fuel remaining in terms of laps (value on MFD)
    uint16      m_maxRPM;                   // Cars max RPM, point of rev limiter
    uint16      m_idleRPM;                  // Cars idle RPM
    uint8       m_maxGears;                 // Maximum number of gears
    uint8       m_drsAllowed;               // 0 = not allowed, 1 = allowed, -1 = unknown
    uint8       m_tyresWear[4];             // Tyre wear percentage
    uint8       m_actualTyreCompound;       // F1 Modern - 16 = C5, 17 = C4, 18 = C3, 19 = C2, 20 = C1
                                            // 7 = inter, 8 = wet
                                            // F1 Classic - 9 = dry, 10 = wet
                                            // F2 – 11 = super soft, 12 = soft, 13 = medium, 14 = hard
                                            // 15 = wet
    uint8       m_visualTyreCompound;       // F1 visual (can be different from actual compound)
                                            // 16 = soft, 17 = medium, 18 = hard, 7 = inter, 8 = wet
                                            // F1 Classic – same as above
                                            // F2 – same as above
    uint8       m_tyresDamage[4];           // Tyre damage (percentage)
    uint8       m_frontLeftWingDamage;      // Front left wing damage (percentage)
    uint8       m_frontRightWingDamage;     // Front right wing damage (percentage)
    uint8       m_rearWingDamage;           // Rear wing damage (percentage)
    uint8       m_engineDamage;             // Engine damage (percentage)
    uint8       m_gearBoxDamage;            // Gear box damage (percentage)
    int8        m_vehicleFiaFlags;          // -1 = invalid/unknown, 0 = none, 1 = green
                                            // 2 = blue, 3 = yellow, 4 = red
    float       m_ersStoreEnergy;           // ERS energy store in Joules
    uint8       m_ersDeployMode;            // ERS deployment mode, 0 = none, 1 = low, 2 = medium
                                            // 3 = high, 4 = overtake, 5 = hotlap
    float       m_ersHarvestedThisLapMGUK;  // ERS energy harvested this lap by MGU-K
    float       m_ersHarvestedThisLapMGUH;  // ERS energy harvested this lap by MGU-H
    float       m_ersDeployedThisLap;       // ERS energy deployed this lap
};

struct PacketCarStatusData
{
    PacketHeader        m_header;            // Header

    CarStatusData       m_carStatusData[20];
};
```

Appendices for the various IDs used in the UDP output:

2019 Team IDs
-------------

| ID | Team          | ID | Team                  | ID | Team          |
| -- | ------------- | -- | --------------------- | -- | ------------- |
|  0 | Mercedes      | 15 | McLaren 1998          | 31 | McLaren 1990  | 
|  1 | Ferrari       | 16 | Ferrari 2002          | 32 | Trident       | 
|  2 | Red Bull      | 17 | Ferrari 2004          | 33 | BWT Arden     | 
|  3 | Williams      | 18 | Renault 2006          | 34 | McLaren 1976  |
|  4 | Racing Point  | 19 | Ferrari 2007          | 35 | Lotus 1972    |
|  5 | Renault       | 21 | Red Bull 2010         | 36 | Ferrari 1979  |
|  6 | Toro Rosso    | 22 | Ferrari 1976          | 37 | McLaren 1982  |
|  7 | Haas          | 23 | ART Grand Prix        | 38 | Williams 2003 |
|  8 | McLaren       | 24 | Campos Vexatec Racing | 39 | Brawn 2009    |
|  9 | Alfa Romeo    | 25 | Carlin                | 40 | Lotus 1978    |
| 10 | McLaren 1988  | 26 | Charouz Racing System | 63 | Ferrari 1990  |
| 11 | McLaren 1991  | 27 | DAMS                  | 64 | McLaren 2010  |
| 12 | Williams 1992 | 28 | Russian Time          | 65 | Ferrari 2010  | 
| 13 | Ferrari 1995  | 29 | MP Motorsport         |    |               |
| 14 | Williams 1996 | 30 | Pertamina             |    |               |

2018 Driver IDs
---------------

| ID | Driver            | ID | Driver             |
| -- | ----------------- | -- | ------------------ |
|  0 | Carlos Sainz      | 24 | Igor Correia       |
|  1 | Daniil Kvyat
|  2 | Daniel Ricciardo  | 25 | Sophie Levasseur   |
|  3 | Fernando Alonso   | 26 | Jonas Schiffer     |
|  6 | Kimi Räikkönen    | 27 | Alain Forest       |
|  7 | Lewis Hamilton    | 28 | Jay Letourneau     |
|  8 | Marcus Ericsson   | 29 | Esto Saari         |
|  9 | Max Verstappen    | 30 | Yasar Atiyeh       |
| 10 | Nico Hulkenberg   | 31 | Callisto Calabresi |
| 11 | Kevin Magnussen   | 32 | Naota Izum         |
| 12 | Romain Grosjean   | 33 | Howard Clarke      |
| 13 | Sebastian Vettel  | 34 | Wilhelm Kaufmann   |
| 14 | Sergio Perez      | 35 | Marie Laursen      |
| 15 | Valtteri Bottas   | 36 | Flavio Nieves      |
| 17 | Esteban Ocon      | 58 | Charles Leclerc    |
| 18 | Stoffel Vandoorne | 59 | Pierre Gasly       |
| 19 | Lance Stroll      | 60 | Brendon Hartley    |
| 20 | Arron Barnes      | 61 | Sergey Sirotkin    |
| 21 | Martin Giles      |    |                    |
| 22 | Alex Murray       |    |                    |
| 23 | Lucas Roth        |    |                    |

2018 Track IDs
--------------

| ID | Track            | ID | Track             |
| -- | ---------------- | -- | ----------------- |
|  0 | Melbourne        | 13 | Suzuka            |
|  1 | Paul Ricard      | 14 | Abu Dhabi         |
|  2 | Shanghai         | 15 | Texas             |
|  3 | Sakhir (Bahrain) | 16 | Brazil            |
|  4 | Catalunya        | 17 | Austria           |
|  5 | Monaco           | 18 | Sochi             |
|  6 | Montreal         | 19 | Mexico            |
|  7 | Silverstone      | 20 | Baku (Azerbaijan) |
|  8 | Hockenheim       | 21 | Sakhir Short      |
|  9 | Hungaroring      | 22 | Silverstone Short |
| 10 | Spa              | 23 | Texas Short       |
| 11 | Monza            | 24 | Suzuka Short      |
| 12 | Singapore        |    |                   |

Nationality IDs
---------------

| ID | Nationality | ID | Nationality  | ID | Nationality    | ID | Nationality   |
| -- | ----------- | -- | ------------ | -- | -------------- | -- | ------------- |
|  1 | American    | 26 | Estonian     | 51 | Maltese        | 76 | South Korean  |
|  2 | Argentinian | 27 | Finnish      | 52 | Mexican        | 77 | South African |
|  3 | Australian  | 28 | French       | 53 | Monegasque     | 78 | Spanish       |
|  4 | Austrian    | 29 | German       | 54 | New Zealander  | 79 | Swedish       |
|  5 | Azerbaijani | 30 | Ghanaian     | 55 | Nicaraguan     | 80 | Swiss         |
|  6 | Bahraini    | 31 | Greek        | 56 | North Korean   | 81 | Taiwanese     |
|  7 | Belgian     | 32 | Guatemalan   | 57 | Northern Irish | 82 | Thai          |
|  8 | Bolivian    | 33 | Honduran     | 58 | Norwegian      | 83 | Turkish       |
|  9 | Brazilian   | 34 | Hong Konger  | 59 | Omani          | 84 | Uruguayan     |
| 10 | British     | 35 | Hungarian    | 60 | Pakistani      | 85 | Ukrainian     |
| 11 | Bulgarian   | 36 | Icelander    | 61 | Panamanian     | 86 | Venezuelan    |
| 12 | Cameroonian | 37 | Indian       | 62 | Paraguayan     | 87 | Welsh         |
| 13 | Canadian    | 38 | Indonesian   | 63 | Peruvian       |    |               |
| 14 | Chilean     | 39 | Irish        | 64 | Polish         |    |               |
| 15 | Chinese     | 40 | Israeli      | 65 | Portuguese     |    |               |
| 16 | Colombian   | 41 | Italian      | 66 | Qatari         |    |               |
| 17 | Costa Rican | 42 | Jamaican     | 67 | Romanian       |    |               |
| 18 | Croatian    | 43 | Japanese     | 68 | Russian        |    |               |
| 19 | Cypriot     | 44 | Jordanian    | 69 | Salvadoran     |    |               |
| 20 | Czech       | 45 | Kuwaiti      | 70 | Saudi          |    |               |
| 21 | Danish      | 46 | Latvian      | 71 | Scottish       |    |               |
| 22 | Dutch       | 47 | Lebanese     | 72 | Serbian        |    |               |
| 23 | Ecuadorian  | 48 | Lithuanian   | 73 | Singaporean    |    |               |
| 24 | English     | 49 | Luxembourger | 74 | Slovakian      |    |               |
| 25 | Emirian     | 50 | Malaysian    | 75 | Slovenian      |    |               |

Button flags
------------

These flags are used in the telemetry packet to determine if any buttons are being held on the controlling device. If the value below logically ANDed with the button status is set then the corresponding button is being held.

| Bit flag | Button            |
| -------- | ----------------- |
|  0x0001  | Cross or A        |
|  0x0002  | Triangle or Y     |
|  0x0004  | Circle or B       |
|  0x0008  | Square or X       |
|  0x0010  | D-pad Left        |
|  0x0020  | D-pad Right       |
|  0x0040  | D-pad Up          |
|  0x0080  | D-pad Down        |
|  0x0100  | Options or Menu   |
|  0x0200  | L1 or LB          |
|  0x0400  | R1 or RB          |
|  0x0800  | L2 or LT          |
|  0x1000  | R2 or RT          |
|  0x2000  | Left Stick Click  |
|  0x4000  | Right Stick Click |
