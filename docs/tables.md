# F1 F1 2019 UDP Telemetry support package

This package is based on the CodeMasters Forum post documenting the F1 2019 packet format:

    https://forums.codemasters.com/topic/38920-f1-2019-udp-specification/

The specification as given there has a few minor issues; these have been fixed here:

(1) In the 'Type / Description' table, the type 'uint', (or preferably, 'uint32', ; see also remark (2) below),
    should be listed as it is used for the field 'm_frameIdentifier' of the 'PacketHeader' structure.
(2) In the 'PacketHeader' structure, the type of the 'm_frameIdentifier' field is given as 'uint'.
    For consistency with the other type names, this should be 'uint32'.
(3) In the 'PacketMotionData' structure, the comments for the three m_angularAcceleration{X,Y,Z} fields erroneously
    refer to 'velocity' rather than 'acceleration'.
(4) In the Driver IDs table, driver 34 has name "Wilheim Kaufmann".
    This is a typo; whenever this driver is encountered in the game, his name is given as "Wilhelm Kaufmann".


## Packet Field Types

| Type   | Description             |
| ------ | ----------------------- |
| uint8  | Unsigned 8-bit integer  |
| int8   | Signed 8-bit integer    |
| uint16 | Unsigned 16-bit integer |
| int16  | Signed 16-bit integer   |
| uint32 | Unsigned 32-bit integer |
| float  | Floating point (32-bit) |
| uint64 | Unsigned 64-bit integer |

## Packet IDs

| Packet Name   | Value | Description                                                                      |
| ------------- | ----- | -------------------------------------------------------------------------------- |
| Motion        | 0     | Contains all motion data for player's car – only sent while player is in control |
| Session       | 1     | Data about the session – track, time left                                        |
| Lap Data      | 2     | Data about all the lap times of cars in the session                              |
| Event         | 3     | Various notable events that happen during a session                              |
| Participants  | 4     | List of participants in the session, mostly relevant for multiplayer             |
| Car Setups    | 5     | Packet detailing car setups for cars in the race                                 |
| Car Telemetry | 6     | Telemetry data for all cars                                                      |
| Car Status    | 7     | Status data for all cars such as damage                                          |

## Event Types

| Event             | Code | Description                            |
| ----------------- | ---- | -------------------------------------- |
| Session Started   | SSTA | Sent when the session starts           |
| Session Ended     | SEND | Sent when the session ends             |
| Fastest Lap       | FTLP | When a driver achieves the fastest lap |
| Retirement        | RTMT | When a driver retires                  |
| DRS enabled       | DRSE | Race control have enabled DRS          |
| DRS disabled      | DRSD | Race control have disabled DRS         |
| Team mate in pits | TMPT | Your team mate has entered the pits    |
| Chequered flag    | CHQF | The chequered flag has been waved      |
| Race Winner       | RCWN | The race winner is announced           |

## Team IDs

| ID | Team            | ID | Team                  | ID | Team         |
|----|-----------------|----|-----------------------|----|--------------|
| 0  | Mercedes        | 21 | Red Bull 2010         | 63 | Ferrari 1990 |
| 1  | Ferrari         | 22 | Ferrari 1976          | 64 | McLaren 2010 |
| 2  | Red Bull Racing | 23 | ART Grand Prix        | 65 | Ferrari 2010 |
| 3  | Williams        | 24 | Campos Vexatec Racing |    |              |
| 4  | Racing Point    | 25 | Carlin                |    |              |
| 5  | Renault         | 26 | Charouz Racing System |    |              |
| 6  | Toro Rosso      | 27 | DAMS                  |    |              |
| 7  | Haas            | 28 | Russian Time          |    |              |
| 8  | McLaren         | 29 | MP Motorsport         |    |              |
| 9  | Alfa Romeo      | 30 | Pertamina             |    |              |
| 10 | McLaren 1988    | 31 | McLaren 1990          |    |              |
| 11 | McLaren 1991    | 32 | Trident               |    |              |
| 12 | Williams 1992   | 33 | BWT Arden             |    |              |
| 13 | Ferrari 1995    | 34 | McLaren 1976          |    |              |
| 14 | Williams 1996   | 35 | Lotus 1972            |    |              |
| 15 | McLaren 1998    | 36 | Ferrari 1979          |    |              |
| 16 | Ferrari 2002    | 37 | McLaren 1982          |    |              |
| 17 | Ferrari 2004    | 38 | Williams 2003         |    |              |
| 18 | Renault 2006    | 39 | Brawn 2009            |    |              |
| 19 | Ferrari 2007    | 40 | Lotus 1978            |    |              |

## Driver IDs

| ID | Driver             | ID | Driver              | ID | Driver             |
|----|--------------------|----|---------------------|----|--------------------|
| 0  | Carlos Sainz       | 37 | Peter Belousov      | 69 | Ruben Meijer       |
| 1  | Daniil Kvyat       | 38 | Klimek Michalski    | 70 | Rashid Nair        |
| 2  | Daniel Ricciardo   | 39 | Santiago Moreno     | 71 | Jack Tremblay      |
| 6  | Kimi Räikkönen     | 40 | Benjamin Coppens    | 74 | Antonio Giovinazzi |
| 7  | Lewis Hamilton     | 41 | Noah Visser         | 75 | Robert Kubica      |
| 9  | Max Verstappen     | 42 | Gert Waldmuller     |    |                    |
| 10 | Nico Hulkenberg    | 43 | Julian Quesada      |    |                    |
| 11 | Kevin Magnussen    | 44 | Daniel Jones        |    |                    |
| 12 | Romain Grosjean    | 45 | Artem Markelov      |    |                    |
| 13 | Sebastian Vettel   | 46 | Tadasuke Makino     |    |                    |
| 14 | Sergio Perez       | 47 | Sean Gelael         |    |                    |
| 15 | Valtteri Bottas    | 48 | Nyck De Vries       |    |                    |
| 19 | Lance Stroll       | 49 | Jack Aitken         |    |                    |
| 20 | Arron Barnes       | 50 | George Russell      |    |                    |
| 21 | Martin Giles       | 51 | Maximilian Günther  |    |                    |
| 22 | Alex Murray        | 52 | Nirei Fukuzumi      |    |                    |
| 23 | Lucas Roth         | 53 | Luca Ghiotto        |    |                    |
| 24 | Igor Correia       | 54 | Lando Norris        |    |                    |
| 25 | Sophie Levasseur   | 55 | Sérgio Sette Câmara |    |                    |
| 26 | Jonas Schiffer     | 56 | Louis Delétraz      |    |                    |
| 27 | Alain Forest       | 57 | Antonio Fuoco       |    |                    |
| 28 | Jay Letourneau     | 58 | Charles Leclerc     |    |                    |
| 29 | Esto Saari         | 59 | Pierre Gasly        |    |                    |
| 30 | Yasar Atiyeh       | 62 | Alexander Albon     |    |                    |
| 31 | Callisto Calabresi | 63 | Nicholas Latifi     |    |                    |
| 32 | Naota Izum         | 64 | Dorian Boccolacci   |    |                    |
| 33 | Howard Clarke      | 65 | Niko Kari           |    |                    |
| 34 | Wilhelm Kaufmann   | 66 | Roberto Merhi       |    |                    |
| 35 | Marie Laursen      | 67 | Arjun Maini         |    |                    |
| 36 | Flavio Nieves      | 68 | Alessio Lorandi     |    |                    |

## Track IDs

| ID | Track             |
|----|-------------------|
| 0  | Melbourne         |
| 1  | Paul Ricard       |
| 2  | Shanghai          |
| 3  | Sakhir (Bahrain)  |
| 4  | Catalunya         |
| 5  | Monaco            |
| 6  | Montreal          |
| 7  | Silverstone       |
| 8  | Hockenheim        |
| 9  | Hungaroring       |
| 10 | Spa               |
| 11 | Monza             |
| 12 | Singapore         |
| 13 | Suzuka            |
| 14 | Abu Dhabi         |
| 15 | Texas             |
| 16 | Brazil            |
| 17 | Austria           |
| 18 | Sochi             |
| 19 | Mexico            |
| 20 | Baku (Azerbaijan) |
| 21 | Sakhir Short      |
| 22 | Silverstone Short |
| 23 | Texas Short       |
| 24 | Suzuka Short      |

## Nationality IDs

| ID | Nationality | ID | Nationality    | ID | Nationality   |
|----|-------------|----|----------------|----|---------------|
| 1  | American    | 31 | Greek          | 61 | Panamanian    |
| 2  | Argentinian | 32 | Guatemalan     | 62 | Paraguayan    |
| 3  | Australian  | 33 | Honduran       | 63 | Peruvian      |
| 4  | Austrian    | 34 | Hong Konger    | 64 | Polish        |
| 5  | Azerbaijani | 35 | Hungarian      | 65 | Portuguese    |
| 6  | Bahraini    | 36 | Icelander      | 66 | Qatari        |
| 7  | Belgian     | 37 | Indian         | 67 | Romanian      |
| 8  | Bolivian    | 38 | Indonesian     | 68 | Russian       |
| 9  | Brazilian   | 39 | Irish          | 69 | Salvadoran    |
| 10 | British     | 40 | Israeli        | 70 | Saudi         |
| 11 | Bulgarian   | 41 | Italian        | 71 | Scottish      |
| 12 | Cameroonian | 42 | Jamaican       | 72 | Serbian       |
| 13 | Canadian    | 43 | Japanese       | 73 | Singaporean   |
| 14 | Chilean     | 44 | Jordanian      | 74 | Slovakian     |
| 15 | Chinese     | 45 | Kuwaiti        | 75 | Slovenian     |
| 16 | Colombian   | 46 | Latvian        | 76 | South Korean  |
| 17 | Costa Rican | 47 | Lebanese       | 77 | South African |
| 18 | Croatian    | 48 | Lithuanian     | 78 | Spanish       |
| 19 | Cypriot     | 49 | Luxembourger   | 79 | Swedish       |
| 20 | Czech       | 50 | Malaysian      | 80 | Swiss         |
| 21 | Danish      | 51 | Maltese        | 81 | Thai          |
| 22 | Dutch       | 52 | Mexican        | 82 | Turkish       |
| 23 | Ecuadorian  | 53 | Monegasque     | 83 | Uruguayan     |
| 24 | English     | 54 | New Zealander  | 84 | Ukrainian     |
| 25 | Emirian     | 55 | Nicaraguan     | 85 | Venezuelan    |
| 26 | Estonian    | 56 | North Korean   | 86 | Welsh         |
| 27 | Finnish     | 57 | Northern Irish |    |               |
| 28 | French      | 58 | Norwegian      |    |               |
| 29 | German      | 59 | Omani          |    |               |
| 30 | Ghanaian    | 60 | Pakistani      |    |               |

## Surface Type IDs

| ID | Surface      |
|----|--------------|
| 0  | Tarmac       |
| 1  | Rumble strip |
| 2  | Concrete     |
| 3  | Rock         |
| 4  | Gravel       |
| 5  | Mud          |
| 6  | Sand         |
| 7  | Grass        |
| 8  | Water        |
| 9  | Cobblestone  |
| 10 | Metal        |
| 11 | Ridged       |

## Button bit-mask values

| Bit flags | Button            |
|-----------|-------------------|
| 0x0001    | Cross or A        |
| 0x0002    | Triangle or Y     |
| 0x0004    | Circle or B       |
| 0x0008    | Square or X       |
| 0x0010    | D-pad Left        |
| 0x0020    | D-pad Right       |
| 0x0040    | D-pad Up          |
| 0x0080    | D-pad Down        |
| 0x0100    | Options or Menu   |
| 0x0200    | L1 or LB          |
| 0x0400    | R1 or RB          |
| 0x0800    | L2 or LT          |
| 0x1000    | R2 or RT          |
| 0x2000    | Left Stick Click  |
| 0x4000    | Right Stick Click |
