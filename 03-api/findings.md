# API Findings

## Authentication response time exceeded 2 seconds

The authentication endpoint did not consistently meet the required response time of under 2 seconds.

Observed examples during testing included:

- Approximately 2.34 seconds
- Approximately 2.23 seconds
- Approximately 2.12 seconds

The endpoint still returned the expected HTTP status and response body.

Because Restful Booker is a shared public test API, network or server load may contribute to the slower response. However, based on the test requirement, these requests do not meet the expected response-time limit when they exceed 2 seconds.

## PUT update response time exceeded 2 seconds

While updating a booking with PUT, the request returned HTTP 200 and the booking was updated successfully.

However, the response took 2.74 seconds, which is above the required 2-second response-time limit.

This may be affected by the shared public test environment or network conditions, but based on the requirement, the request does not meet the expected performance limit.

## DELETE response time exceeded 2 seconds

The booking delete request returned HTTP 201, which shows that the booking was deleted successfully.

However, the response took 2.43 seconds, which is above the required 2-second response-time limit.

This may be influenced by the shared public test environment or network conditions, but based on the task requirement, the request does not meet the expected performance limit.

## Missing booking fields return HTTP 500

I tried to create a booking with only `firstname` and `lastname`, leaving out required fields such as `totalprice`, `depositpaid` and `bookingdates`.

I expected the API to reject the request with a client error such as HTTP 400 or 422.

Instead, the API returned HTTP 500 Internal Server Error.

This looks like a bug because invalid user input should normally be handled as a validation error rather than causing a server error.

## Booking API accepts incorrect data types

I tried to create a booking using incorrect data types.

I sent:

- `totalprice` as the text `"two hundred"` instead of a number
- `depositpaid` as the text `"yes"` instead of a boolean

I expected the API to reject the request with a client validation error such as HTTP 400 or 422.

Instead, the API returned HTTP 200 and accepted the booking.

This looks like a data validation issue because invalid field types can be stored and may cause problems for systems that expect consistent booking data.
## Non-existent booking request exceeded 2 seconds

The request for a booking ID that does not exist returned the expected HTTP 404 status.

However, during the full test run the response took approximately 2.24 seconds, which is above the required 2-second response-time limit.

The same test had previously completed in under 2 seconds, so the response time appears to be inconsistent.