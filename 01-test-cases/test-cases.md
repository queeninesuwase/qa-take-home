# Appointment Booking Test Cases

| ID | Title | Preconditions | Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC01 | Book appointment successfully | Member has an active policy and provider is in-network | 1. Log in 2. Open appointment booking 3. Select provider 4. Select available slot 5. Confirm booking | Active member, in-network provider, available slot | Appointment is booked successfully | High |
| TC02 | Reject booking for inactive policy | Member's policy is inactive | 1. Log in 2. Try to book an appointment | Inactive policy | Booking is not allowed and member sees a clear message | High |
| TC03 | Reject booking with out-of-network provider | Member has active policy | 1. Open booking 2. Select out-of-network provider 3. Try to confirm | Out-of-network provider | Booking is rejected | High |
| TC04 | Book the next available slot today | Member has active policy and a slot is available today | 1. Open booking 2. Select today's next available slot 3. Confirm | Next available slot today | Booking succeeds | High |
| TC05 | [BVA] Book exactly 30 days ahead | Member has active policy and slot is available | 1. Open booking 2. Select a date exactly 30 days from today 3. Select a slot 4. Confirm | Date = today + 30 days | Booking succeeds | High |
| TC06 | [BVA] Reject booking 31 days ahead | Member has active policy | 1. Open booking 2. Try to select a date 31 days from today | Date = today + 31 days | Booking is not allowed | High |
| TC07 | [BVA] Book first valid slot at 08:00 | Member has active policy and 08:00 slot is available | 1. Open booking 2. Select 08:00 slot 3. Confirm | 08:00 | Booking succeeds | Medium |
| TC08 | [BVA] Reject slot before 08:00 | Member has active policy | 1. Open booking 2. Try to select a slot before opening time | 07:30 | Slot cannot be booked | Medium |
| TC09 | [BVA] Book last valid slot ending at 17:00 | Member has active policy and slot is available | 1. Open booking 2. Select 16:30 slot 3. Confirm | 16:30–17:00 | Booking succeeds | Medium |
| TC10 | [BVA] Allow third upcoming appointment | Member already has 2 upcoming appointments | 1. Open booking 2. Select valid appointment 3. Confirm | Existing appointments = 2 | Third appointment is booked successfully | High |
| TC11 | [BVA] Reject fourth upcoming appointment | Member already has 3 upcoming appointments | 1. Open booking 2. Select another appointment 3. Confirm | Existing appointments = 3 | Booking is rejected because the limit is 3 upcoming appointments | High |
| TC12 | [BVA] Cancel exactly 2 hours before appointment | Member has an upcoming appointment | 1. Open appointment 2. Cancel exactly 2 hours before start time | Appointment at 14:00, cancel at 12:00 | Appointment is cancelled free of charge | High |
| TC13 | Receive confirmation after successful booking | Member has active policy and valid phone number | 1. Complete a valid booking 2. Check in-app messages 3. Check SMS | Valid booking | Member receives both an in-app confirmation and an SMS | High |

## Questions for the Product Manager

1. What should happen if a member cancels less than 2 hours before the appointment? Is cancellation blocked, or is a fee charged?

2. Does 17:00 mean the last appointment must finish by 17:00, or can an appointment start at 17:00?

3. What should happen if the booking succeeds but the SMS notification fails?