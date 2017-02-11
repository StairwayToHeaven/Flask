
unit_conversion = {
  "Celsius": {
    "Kelvin": lambda x: x + 273.15,
    "Fahrenheit": lambda x: (x * 1.8) + 32,
    "Rankine": lambda x: (x * 1.8) + 491.67,
    "Celsius": lambda x: x
  },
  
  "Kelvin": {
    "Kelvin": lambda x: x,
    "Fahrenheit": lambda x: ((x - 273.15) * 1.8) + 32,
    "Rankine": lambda x: x * 1.8,
    "Celsius": lambda x: x - 273.15
  },
  
  "Fahrenheit": {
    "Kelvin": lambda x: ((x - 32) * (5.0 / 9.0)) + 273.15,
    "Fahrenheit": lambda x: x,
    "Rankine": lambda x: x + 459.67,
    "Celsius": lambda x: (x - 32) * (5.0 / 9.0)
  },
  
  "Rankine": {
    "Kelvin": lambda x: x * (5.0 / 9.0),
    "Fahrenheit": lambda x: x - 459.67,
    "Rankine": lambda x: x,
    "Celsius": lambda x: (x * (5.0 / 9.0)) - 273.15
  },

  "Złoty": {
    "Euro": lambda x: x * 0.23,
    "Yuan": lambda x: x * 1.68,
    "Baht": lambda x: x * 8.63,
    "Yen": lambda x: x * 28.1,
    "American dollar": lambda x: x * 0.25,
    "Forint": lambda x: x * 70.9,
    "Złoty": lambda x: x
  },

  "Euro": {
    "Złoty": lambda x: x * 4.31,
    "Yuan": lambda x: x * 7.36,
    "Baht": lambda x: x * 37.89,
    "Yen": lambda x: x * 122.37,
    "American dollar": lambda x: x * 1.07,
    "Forint": lambda x: x * 309.4,
    "Euro": lambda x: x
  },
  
  "Baht": {
    "Euro": lambda x: x * 0.03,
    "Yuan": lambda x: x * 0.2,
    "Baht": lambda x: x,
    "Yen": lambda x: x * 3.24,
    "American dollar": lambda x: x * 0.03,
    "Forint": lambda x: x * 8.17,
    "Złoty": lambda x: x * 0.16
  },
  
  "Yuan": {
    "Euro": lambda x: x * 0.14,
    "Yuan": lambda x: x,
    "Baht": lambda x: x * 5.15,
    "Yen": lambda x: x * 16.67,
    "American dollar": lambda x: x * 0.15,
    "Forint": lambda x: x * 42.04,
    "Złoty": lambda x: x * 0.59
  },
  
  "Yen": {
    "Euro": lambda x: x * 0.008,
    "Yuan": lambda x: x * 0.06,
    "Baht": lambda x: x * 0.3,
    "Yen": lambda x: x,
    "American dollar": lambda x: x * 0.009,
    "Forint": lambda x: x * 2.52,
    "Złoty": lambda x: x * 0.04
  },
  
  "American dollar": {
    "Euro": lambda x: x * 4.08,
    "Yuan": lambda x: x * 6.88,
    "Baht": lambda x: x * 35.4,
    "Yen": lambda x: x * 114.6,
    "American dollar": lambda x: x,
    "Forint": lambda x: x * 289.1,
    "Złoty": lambda x: x * 4.08
  },
  
  "Forint": {
    "Euro": lambda x: x * 0.003,
    "Yuan": lambda x: x * 0.02,
    "Baht": lambda x: x * 0.12,
    "Yen": lambda x: x * 0.4,
    "American dollar": lambda x: x * 0.004,
    "Forint": lambda x: x,
    "Złoty": lambda x: x * 0.015
  },
  
  "Prussian okseft": {
    "Log": lambda x: x * 412.0,
    "Litre": lambda x: x * 206.0,
    "Mililiter": lambda x: x * 206000.0,
    "Prussian okseft": lambda x: x
  },
  
  "Log": {
    "Log": lambda x: x,
    "Litre": lambda x: x * 0.5,
    "Mililiter": lambda x: x * 500.0,
    "Prussian okseft": lambda x: x * 0.01
  },
  
  "Litre": {
    "Log": lambda x: x * 2,
    "Litre": lambda x: x,
    "Mililiter": lambda x: x * 1000.0,
    "Prussian okseft": lambda x: x * 0.02
  },
  
  "Mililiter": {
    "Log": lambda x: x * 0.05,
    "Litre": lambda x: x * 0.001,
    "Mililiter": lambda x: x,
    "Prussian okseft": lambda x: x * 0.0002
  },
  
  "Pound": {
    "Stone": lambda x: x * 0.07,
    "Kilogram": lambda x: x * 0.45,
    "Pound": lambda x: x,
    "Cetnar": lambda x: x * 0.009
  },
  
  "Stone": {
    "Stone": lambda x: x ,
    "Kilogram": lambda x: x * 6.35,
    "Pound": lambda x: x * 14,
    "Cetnar": lambda x: x * 0.13
  },
  
  "Kilogram": {
    "Stone": lambda x: x * 0.16,
    "Kilogram": lambda x: x ,
    "Pound": lambda x: x * 2.2,
    "Cetnar": lambda x: x * 0.02
  },
  
  "Cetnar": {
    "Stone": lambda x: x * 8,
    "Kilogram": lambda x: x * 50.8,
    "Pound": lambda x: x * 112,
    "Cetnar": lambda x: x
  },
  
  "Sążen": {
    "Cracow elbow": lambda x: x * 2.7,
    "Foot": lambda x: x * 5.58,
    "Danish rod": lambda x: (x * 5.58) * 14.0,
    "Kilometre": lambda x: (x * 0.17) / 100.0,
    "Centimeter": lambda x: x * 170.0,
    "Meter": lambda x: x * 1.7,
    "Sążen": lambda x: x
  },
  
  "Meter": {
    "Cracow elbow": lambda x: x * 1.6,
    "Foot": lambda x: x * 3.5,
    "Danish rod": lambda x: (x * 0.3) * 14.0,
    "Kilometre": lambda x: x * 0.001,
    "Centimeter": lambda x: x * 100.0,
    "Meter": lambda x: x,
    "Sążen": lambda x: x * 0.6
  },
  
  "Kilometre": {
    "Cracow elbow": lambda x: x * 1600.0,
    "Foot": lambda x: x * 3278.7,
    "Danish rod": lambda x: (x * 3278.7) * 14.0,
    "Kilometre": lambda x: x,
    "Centimeter": lambda x: x * 100000.0,
    "Meter": lambda x: x * 1000.0,
    "Sążen": lambda x: x * 588.2
  },
  
  "Danish rod": {
    "Cracow elbow": lambda x: x * 14.0 * 30.5 * 2.05,
    "Foot": lambda x: x * 14.0,
    "Danish rod": lambda x: x,
    "Kilometre": lambda x: ((x * 14) * 30.5) / 100000.0,
    "Centimeter": lambda x: (x * 14) * 30.5,
    "Meter": lambda x: ((x * 14.0) * 30.5) / 100.0,
    "Sążen": lambda x: (((x * 14.0) * 30.5) / 100.0) / 1.7
  },
  
  "Foot": {
    "Cracow elbow": lambda x: x / 2.05,
    "Foot": lambda x: x,
    "Danish rod": lambda x: x / 14.0,
    "Kilometre": lambda x: (x * 30.5) / 100000.0,
    "Centimeter": lambda x: x * 30.5,
    "Meter": lambda x: (x * 30.5) / 100.0,
    "Sążen": lambda x: ((x * 30.5) / 100.0) / 1.7
  },
  
  "Cracow elbow": {
    "Cracow elbow": lambda x: x,
    "Foot": lambda x: x * 2.05,
    "Danish rod": lambda x: x * 14.0 * 2.05,
    "Kilometre": lambda x: (x * 62.5) / 100000.0,
    "Centimeter": lambda x: x * 62.5,
    "Meter": lambda x: (x * 62.5) / 100.0,
    "Sążen": lambda x: ((x * 62.5) / 100.0) / 1.7
  },
  
  "Centimeter": {
    "Cracow elbow": lambda x: x * 0.62,
    "Foot": lambda x: x * 0.3,
    "Danish rod": lambda x: (x * 0.3) * 14.0,
    "Kilometre": lambda x: x * 0.00001,
    "Centimeter": lambda x: x,
    "Meter": lambda x: x * 0.01,
    "Sążen": lambda x: x * 0.17
  }
  
  
}

unit_description = {
#jednostki temperatury
  'Celsius': {
  'Celsius': 'Celsius, also known as centigrade, is a scale and unit of measurement for temperature. As an SI derived unit, it is used by most countries in the world. It is named after the Swedish astronomer Anders Celsius.',
  'Kelvin': 'Kelvin is a unit of measure for temperature based upon an absolute scale. It is one of the seven base units in the International System of Units (SI) and is assigned the unit symbol K.',
  'Fahrenheit': 'Fahrenheit is a temperature scale based on one proposed in 1724 by the physicist Daniel Gabriel Fahrenheit (1686–1736), after whom the scale is named.',
  'Rankine': 'Rankine cycle is a model that is used to predict the performance of steam turbine systems. The Rankine cycle is an idealized thermodynamic cycle of a heat engine that converts heat into mechanical work.'
  },
  
  'Kelvin': {
  'Celsius': 'Celsius, also known as centigrade, is a scale and unit of measurement for temperature. As an SI derived unit, it is used by most countries in the world. It is named after the Swedish astronomer Anders Celsius.',
  'Kelvin': 'Kelvin is a unit of measure for temperature based upon an absolute scale. It is one of the seven base units in the International System of Units (SI) and is assigned the unit symbol K.',
  'Fahrenheit': 'Fahrenheit is a temperature scale based on one proposed in 1724 by the physicist Daniel Gabriel Fahrenheit (1686–1736), after whom the scale is named.',
  'Rankine': 'Rankine cycle is a model that is used to predict the performance of steam turbine systems. The Rankine cycle is an idealized thermodynamic cycle of a heat engine that converts heat into mechanical work.'
  },
  
  'Fahrenheit': {
  'Celsius': 'Celsius, also known as centigrade, is a scale and unit of measurement for temperature. As an SI derived unit, it is used by most countries in the world. It is named after the Swedish astronomer Anders Celsius.',
  'Kelvin': 'Kelvin is a unit of measure for temperature based upon an absolute scale. It is one of the seven base units in the International System of Units (SI) and is assigned the unit symbol K.',
  'Fahrenheit': 'Fahrenheit is a temperature scale based on one proposed in 1724 by the physicist Daniel Gabriel Fahrenheit (1686–1736), after whom the scale is named.',
  'Rankine': 'Rankine cycle is a model that is used to predict the performance of steam turbine systems. The Rankine cycle is an idealized thermodynamic cycle of a heat engine that converts heat into mechanical work.'
  },
  
  'Rankine': {
  'Celsius': 'Celsius, also known as centigrade, is a scale and unit of measurement for temperature. As an SI derived unit, it is used by most countries in the world. It is named after the Swedish astronomer Anders Celsius.',
  'Kelvin': 'Kelvin is a unit of measure for temperature based upon an absolute scale. It is one of the seven base units in the International System of Units (SI) and is assigned the unit symbol K.',
  'Fahrenheit': 'Fahrenheit is a temperature scale based on one proposed in 1724 by the physicist Daniel Gabriel Fahrenheit (1686–1736), after whom the scale is named.',
  'Rankine': 'Rankine cycle is a model that is used to predict the performance of steam turbine systems. The Rankine cycle is an idealized thermodynamic cycle of a heat engine that converts heat into mechanical work.'
  },
  
#jednostki długości
  'Sążen': {
  'Sążen': 'Unit of length. Sążeń had a length of outstretched hands arms of adult man ~ 1,7 meter.',
  'Cracow elbow': 'A unit of length, with different values depending on the State, the region and the historical epoch. Calculations are performed for the adoption of the measure of the elbow of the 14th century- 62.5 cm.',
  'Foot': 'A unit of length, originally derived from the length of the human foot. It is divided into to 30.48 centimeters.',
  'Danish rod': 'A unit of length, one of pręt duński is 14 foots. In Polish it is - pręt duński.',
  'Kilometre': 'A unit of length, the common measure of distances equal to 1000 meters.',
  'Centimeter': 'One 100th of a meter.',
  'Meter': 'The fundamental unit of length in the metric system, one meter is 100 centimeter & 0,001 kilometre.'
  },
  
  'Cracow elbow': {
  'Sążen': 'Unit of length. Sążeń had a length of outstretched hands arms of adult man ~ 1,7 meter.',
  'Cracow elbow': 'A unit of length, with different values depending on the State, the region and the historical epoch. Calculations are performed for the adoption of the measure of the elbow of the 14th century- 62.5 cm.',
  'Foot': 'A unit of length, originally derived from the length of the human foot. It is divided into to 30.48 centimeters.',
  'Danish rod': 'A unit of length, one of pręt duński is 14 foots. In Polish it is - pręt duński.',
  'Kilometre': 'A unit of length, the common measure of distances equal to 1000 meters.',
  'Centimeter': 'One 100th of a meter.',
  'Meter': 'The fundamental unit of length in the metric system, one meter is 100 centimeter & 0,001 kilometre.'
  },
  
  'Foot': {
  'Sążen': 'Unit of length. Sążeń had a length of outstretched hands arms of adult man ~ 1,7 meter.',
  'Cracow elbow': 'A unit of length, with different values depending on the State, the region and the historical epoch. Calculations are performed for the adoption of the measure of the elbow of the 14th century- 62.5 cm.',
  'Foot': 'A unit of length, originally derived from the length of the human foot. It is divided into to 30.48 centimeters.',
  'Danish rod': 'A unit of length, one of pręt duński is 14 foots. In Polish it is - pręt duński.',
  'Kilometre': 'A unit of length, the common measure of distances equal to 1000 meters.',
  'Centimeter': 'One 100th of a meter.',
  'Meter': 'The fundamental unit of length in the metric system, one meter is 100 centimeter & 0,001 kilometre.'
  },
  
  'Danish rod': {
  'Sążen': 'Unit of length. Sążeń had a length of outstretched hands arms of adult man ~ 1,7 meter.',
  'Cracow elbow': 'A unit of length, with different values depending on the State, the region and the historical epoch. Calculations are performed for the adoption of the measure of the elbow of the 14th century- 62.5 cm.',
  'Foot': 'A unit of length, originally derived from the length of the human foot. It is divided into to 30.48 centimeters.',
  'Danish rod': 'A unit of length, one of pręt duński is 14 foots. In Polish it is - pręt duński.',
  'Kilometre': 'A unit of length, the common measure of distances equal to 1000 meters.',
  'Centimeter': 'One 100th of a meter.',
  'Meter': 'The fundamental unit of length in the metric system, one meter is 100 centimeter & 0,001 kilometre.'
  },
  
  'Kilometre': {
  'Sążen': 'Unit of length. Sążeń had a length of outstretched hands arms of adult man ~ 1,7 meter.',
  'Cracow elbow': 'A unit of length, with different values depending on the State, the region and the historical epoch. Calculations are performed for the adoption of the measure of the elbow of the 14th century- 62.5 cm.',
  'Foot': 'A unit of length, originally derived from the length of the human foot. It is divided into to 30.48 centimeters.',
  'Danish rod': 'A unit of length, one of pręt duński is 14 foots. In Polish it is - pręt duński.',
  'Kilometre': 'A unit of length, the common measure of distances equal to 1000 meters.',
  'Centimeter': 'One 100th of a meter.',
  'Meter': 'The fundamental unit of length in the metric system, one meter is 100 centimeter & 0,001 kilometre.'
  },
  
  'Centimeter': {
  'Sążen': 'Unit of length. Sążeń had a length of outstretched hands arms of adult man ~ 1,7 meter.',
  'Cracow elbow': 'A unit of length, with different values depending on the State, the region and the historical epoch. Calculations are performed for the adoption of the measure of the elbow of the 14th century- 62.5 cm.',
  'Foot': 'A unit of length, originally derived from the length of the human foot. It is divided into to 30.48 centimeters.',
  'Danish rod': 'A unit of length, one of pręt duński is 14 foots. In Polish it is - pręt duński.',
  'Kilometre': 'A unit of length, the common measure of distances equal to 1000 meters.',
  'Centimeter': 'One 100th of a meter.',
  'Meter': 'The fundamental unit of length in the metric system, one meter is 100 centimeter & 0,001 kilometre.'
  },
  
  'Meter': {
  'Sążen': 'Unit of length. Sążeń had a length of outstretched hands arms of adult man ~ 1,7 meter.',
  'Cracow elbow': 'A unit of length, with different values depending on the State, the region and the historical epoch. Calculations are performed for the adoption of the measure of the elbow of the 14th century- 62.5 cm.',
  'Foot': 'A unit of length, originally derived from the length of the human foot. It is divided into to 30.48 centimeters.',
  'Danish rod': 'A unit of length, one of pręt duński is 14 foots. In Polish it is - pręt duński.',
  'Kilometre': 'A unit of length, the common measure of distances equal to 1000 meters.',
  'Centimeter': 'One 100th of a meter.',
  'Meter': 'The fundamental unit of length in the metric system, one meter is 100 centimeter & 0,001 kilometre.'
  },
  

#jednostki miary

  'Prussian okseft': {
  'Prussian okseft': 'Okseft of Prussia equal was 206 litres, this measure was depending in other countries on the time.',
  'Log': 'Biblical liquid measure equal to approximately 0. 5 liters.',
  'Litre': 'A unit of capacity redefined in 1964 by a reduction of 28 parts in a million to be exactly equal to 1000 mililiters.',
  'Mililiter': 'A unit of capacity equal to one thousandth of a liter.'
  },
  
  'Log': {
  'Prussian okseft': 'Okseft of Prussia equal was 206 litres, this measure was depending in other countries on the time.',
  'Log': 'Biblical liquid measure equal to approximately 0. 5 liters.',
  'Litre': 'A unit of capacity redefined in 1964 by a reduction of 28 parts in a million to be exactly equal to 1000 mililiters.',
  'Mililiter': 'A unit of capacity equal to one thousandth of a liter.'
  },
  
  'Litre': {
  'Prussian okseft': 'Okseft of Prussia equal was 206 litres, this measure was depending in other countries on the time.',
  'Log': 'Biblical liquid measure equal to approximately 0. 5 liters.',
  'Litre': 'A unit of capacity redefined in 1964 by a reduction of 28 parts in a million to be exactly equal to 1000 mililiters.',
  'Mililiter': 'A unit of capacity equal to one thousandth of a liter.'
  },
  
  'Mililiter': {
  'Prussian okseft': 'Okseft of Prussia equal was 206 litres, this measure was depending in other countries on the time.',
  'Log': 'Biblical liquid measure equal to approximately 0. 5 liters.',
  'Litre': 'A unit of capacity redefined in 1964 by a reduction of 28 parts in a million to be exactly equal to 1000 mililiters.',
  'Mililiter': 'A unit of capacity equal to one thousandth of a liter.'
  },
  
#jednostki pieniężne
  
  'Yuan': {
  'Yuan': 'The Yuan renminbi is the official currency of the People Republic of China.',
  'Baht': 'The Baht  is the currency of Thailand.',
  'Euro': 'The Euro (sign: €; code: EUR) is the official currency of the eurozone, which consists of 19 of the 28 member states of the European Union.',
  'American dollar': 'The Dollar is the official currency of the United States and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Yen': 'The Yen is the official currency of the Japan and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Forint': 'The Forint is the official currency in Hungary and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Złoty': 'The Zloty, which literally means "golden", is the currency of Poland. The modern złoty is subdivided into 100 groszy.'
  },
  
  'Baht': {
  'Yuan': 'The Yuan renminbi is the official currency of the People Republic of China.',
  'Baht': 'The Baht  is the currency of Thailand.',
  'Euro': 'The Euro (sign: €; code: EUR) is the official currency of the eurozone, which consists of 19 of the 28 member states of the European Union.',
  'American dollar': 'The Dollar is the official currency of the United States and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Yen': 'The Yen is the official currency of the Japan and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Forint': 'The Forint is the official currency in Hungary and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Złoty': 'The Zloty, which literally means "golden", is the currency of Poland. The modern złoty is subdivided into 100 groszy.'
  },
  
  'Euro': {
  'Yuan': 'The Yuan renminbi is the official currency of the People Republic of China.',
  'Baht': 'The Baht  is the currency of Thailand.',
  'Euro': 'The Euro (sign: €; code: EUR) is the official currency of the eurozone, which consists of 19 of the 28 member states of the European Union.',
  'American dollar': 'The Dollar is the official currency of the United States and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Yen': 'The Yen is the official currency of the Japan and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Forint': 'The Forint is the official currency in Hungary and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Złoty': 'The Zloty, which literally means "golden", is the currency of Poland. The modern złoty is subdivided into 100 groszy.'
  },
  
  'American dollar': {
  'Yuan': 'The Yuan renminbi is the official currency of the People Republic of China.',
  'Baht': 'The Baht  is the currency of Thailand.',
  'Euro': 'The Euro (sign: €; code: EUR) is the official currency of the eurozone, which consists of 19 of the 28 member states of the European Union.',
  'American dollar': 'The Dollar is the official currency of the United States and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Yen': 'The Yen is the official currency of the Japan and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Forint': 'The Forint is the official currency in Hungary and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Złoty': 'The Zloty, which literally means "golden", is the currency of Poland. The modern złoty is subdivided into 100 groszy.'
  },
  
  'Yen': {
  'Yuan': 'The Yuan renminbi is the official currency of the People Republic of China.',
  'Baht': 'The Baht  is the currency of Thailand.',
  'Euro': 'The Euro (sign: €; code: EUR) is the official currency of the eurozone, which consists of 19 of the 28 member states of the European Union.',
  'American dollar': 'The Dollar is the official currency of the United States and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Yen': 'The Yen is the official currency of the Japan and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Forint': 'The Forint is the official currency in Hungary and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Złoty': 'The Zloty, which literally means "golden", is the currency of Poland. The modern złoty is subdivided into 100 groszy.'
  },
  
  'Forint': {
  'Yuan': 'The Yuan renminbi is the official currency of the People Republic of China.',
  'Baht': 'The Baht  is the currency of Thailand.',
  'Euro': 'The Euro (sign: €; code: EUR) is the official currency of the eurozone, which consists of 19 of the 28 member states of the European Union.',
  'American dollar': 'The Dollar is the official currency of the United States and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Yen': 'The Yen is the official currency of the Japan and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Forint': 'The Forint is the official currency in Hungary and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Złoty': 'The Zloty, which literally means "golden", is the currency of Poland. The modern złoty is subdivided into 100 groszy.'
  },
  
  'Złoty': {
  'Yuan': 'The Yuan renminbi is the official currency of the People Republic of China.',
  'Baht': 'The Baht  is the currency of Thailand.',
  'Euro': 'The Euro (sign: €; code: EUR) is the official currency of the eurozone, which consists of 19 of the 28 member states of the European Union.',
  'American dollar': 'The Dollar is the official currency of the United States and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Yen': 'The Yen is the official currency of the Japan and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Forint': 'The Forint is the official currency in Hungary and its insular territories per the United States Constitution. It is divided into 100 smaller cent units.',
  'Złoty': 'The Zloty, which literally means "golden", is the currency of Poland. The modern złoty is subdivided into 100 groszy.'
  },
  
  'Pound': {
  'Pound': 'It is a unit of force used in some systems of measurement including English Engineering units and the British Gravitational System.',
  'Cetnar': 'A British unit of weight equivalent to 112 pounds.',
  'Kilogram': 'The kilogram is the base unit of mass in the International System of Units (SI) and is defined as being equal to the mass of the International Prototype of the Kilogram. ',
  'Stone': 'The stone or stone weight is an English and imperial unit of mass now equal to 14 pounds (6.35029318 kg).'
  },
  
  'Cetnar': {
  'Pound': 'It is a unit of force used in some systems of measurement including English Engineering units and the British Gravitational System.',
  'Cetnar': 'A British unit of weight equivalent to 112 pounds.',
  'Kilogram': 'The kilogram is the base unit of mass in the International System of Units (SI) and is defined as being equal to the mass of the International Prototype of the Kilogram.',
  'Stone': 'The stone or stone weight is an English and imperial unit of mass now equal to 14 pounds (6.35029318 kg).'
  },
  
  'Kilogram': {
  'Pound': 'It is a unit of force used in some systems of measurement including English Engineering units and the British Gravitational System.',
  'Cetnar': 'A British unit of weight equivalent to 112 pounds.',
  'Kilogram': 'The kilogram is the base unit of mass in the International System of Units (SI) and is defined as being equal to the mass of the International Prototype of the Kilogram.',
  'Stone': 'The stone or stone weight is an English and imperial unit of mass now equal to 14 pounds (6.35029318 kg).'
  },
  
  'Stone': {
  'Pound': 'It is a unit of force used in some systems of measurement including English Engineering units and the British Gravitational System.',
  'Cetnar': 'A British unit of weight equivalent to 112 pounds.',
  'Kilogram': 'The kilogram is the base unit of mass in the International System of Units (SI) and is defined as being equal to the mass of the International Prototype of the Kilogram.',
  'Stone': 'The stone or stone weight is an English and imperial unit of mass now equal to 14 pounds (6.35029318 kg).'
  }
  # 'm':
}
