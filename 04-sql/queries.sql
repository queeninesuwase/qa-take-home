-- Question 1
SELECT
    claims.id AS claim_id,
    members.name AS member_name,
    providers.name AS provider_name,
    claims.amount,
    claims.status,
    claims.submitted_on
FROM claims
JOIN members
    ON claims.member_id = members.id
JOIN providers
    ON claims.provider_id = providers.id
ORDER BY claims.submitted_on DESC;

-- Question 2
SELECT
    employers.name AS employer_name,
    SUM(claims.amount) AS total_approved_amount
FROM employers
JOIN members
    ON employers.id = members.employer_id
JOIN claims
    ON members.id = claims.member_id
WHERE claims.status = 'approved'
GROUP BY employers.name;

-- Question 3
SELECT
    members.id,
    members.name
FROM members
LEFT JOIN claims
    ON members.id = claims.member_id
WHERE claims.id IS NULL;

-- Question 4
SELECT
    claims.id AS claim_id,
    members.name AS member_name,
    members.policy_end,
    claims.submitted_on,
    claims.amount,
    claims.status
FROM claims
JOIN members
    ON claims.member_id = members.id
WHERE claims.submitted_on > members.policy_end;

-- Question 5
SELECT
    member_id,
    provider_id,
    amount,
    submitted_on,
    COUNT(*) AS duplicate_count
FROM claims
GROUP BY
    member_id,
    provider_id,
    amount,
    submitted_on
HAVING COUNT(*) > 1;