import test from "node:test";
import assert from "node:assert/strict";
import { dhakaDate, addCalendarDays, expectedUtc } from "../src/index.js";

test("Dhaka business date is used across UTC midnight", () => {
  assert.equal(dhakaDate(new Date("2026-11-15T18:30:00.000Z")), "2026-11-16");
});
test("calendar lookahead crosses month and year boundaries", () => {
  assert.equal(addCalendarDays("2026-12-31", 1), "2027-01-01");
});
test("Bangladesh local schedule converts to UTC correctly", () => {
  assert.equal(expectedUtc("2026-11-16", "05:00"), "2026-11-15T23:00:00.000Z");
});
