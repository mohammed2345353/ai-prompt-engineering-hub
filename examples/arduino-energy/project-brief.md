# Smart Energy Consumption Monitoring System

Status: READY_FOR_GEMINI. No firmware has been generated for this example yet.

## Confirmed in the current session

- Course: Real Time System.
- Board: Arduino UNO R3, confirmed by the user.
- Current/voltage monitor: not purchased yet, confirmed by the user.
- Gemini owns substantial programming. ChatGPT owns checks and GitHub delivery.
- Google Drive is the shared source and handoff location.

## Carried forward from the project discussion

- Arduino USB cable, OLED display, buzzer, breadboard 830, jumper wires, and
  a 5 V supply were reported available; resistors are already available.
- Use Serial Monitor commands: `0` turns the LED loads off; `1`, `2`, and `3`
  select how many LED loads are enabled.
- Three slide switches were rejected. A single push button was only optional;
  it is not a requirement for the first version.
- The previous buzzer choice was a two-wire active buzzer rated 3–24 V.
  Its exact current, operating point, and driver remain unverified.

## Previous proposals, not confirmed hardware

- INA219 was proposed; INA226 was an alternative. Neither is confirmed owned.
- Three LEDs were on the missing-parts list; acquisition is not confirmed.
- A 2N2222-family driver was proposed for the buzzer; ownership and the exact
  device/package are not confirmed. Do not assume its pin order.
- A 5 V DC demonstration load was discussed. The actual load arrangement and
  power routing still need a reviewed wiring plan.

## Required behavior and honesty

- Handle serial input and periodic work without long blocking waits.
- Accept only the documented load commands; an invalid command must not
  unexpectedly change outputs. Handle normal line endings explicitly.
- Without an installed and configured sensor, display measurement unavailable.
  Do not substitute LED count, a fixed value, or generated data for measured
  current, voltage, power, or energy.
- Only calculate energy from valid, timestamped measurements. Distinguish
  calculation examples, host tests, simulations and actual hardware readings.
- Treat this as a low-voltage teaching demonstration. Do not design mains
  wiring or present it as a safety-rated protection device.

## Unresolved before final wiring and full monitoring

1. Sensor model, module markings, shunt, range and calibration.
2. OLED controller, resolution, interface/address and power requirements.
3. Buzzer operating current and validated driver circuit.
4. LED/resistor values, available parts and a proposed pin allocation.
5. Sampling/display periods, alert threshold, hysteresis and response deadline.

The report `Arduino - Real-Time Systems Report - University Logo.pdf` is a
general introduction, not the energy project's specification. Its example
room monitor does not authorize adding PIR or temperature sensors here.
Use the Drive source index for access to the report; no private report bytes
or private Drive links belong in the public repository.
