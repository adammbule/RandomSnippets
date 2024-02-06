import json

data = [
    {
        "requestId": "70611116998176911113035",
        "partnerSolutionId": None,
        "referenceNumber": "101-10000",
        "firstName": "KRUPXXX XXXX",
        "lastName": "PATEL",
        "email": "abcefd@gmail.com",
        "paymentMethod": "MasterCard",
        "merchantId": "absa_britam_0956516_kes",
        "accountSuffix": "0898",
        "authIndicator": None,
        "digitalPaymentMethod": None,
        "partnerOriginalTransactionId": None,
        "deviceId": None,
        "terminalSerialNumber": None,
        "processor": "vdcbarclayske",
        "businessApplicationId": None,
        "terminalId": None,
        "xid": None,
        "paTransactionId": None,
        "salesSlipNumber": None,
        "authorizationCode": "05933E",
        "acquirerAccountId": None,
        "jccaTerminalId": None,
        "billingAddress1": "xyz",
        "billingCity": "abcd",
        "billingState": "N/A",
        "billingCountry": "KE",
        "billingPostalCode": "N/A",
        "billingPhoneNumber": "254722222222",
        "ipAddress": None,
        "shippingFirstName": None,
        "shippingLastName": None,
        "shippingAddress1": None,
        "shippingCity": None,
        "shippingState": None,
        "shippingPostalCode": None,
        "shippingCountry": None,
        "shippingPhoneNumber": None,
        "customerId": None,
        "clientApplication": "Recurring Billing Engine",
        "deviceFingerprint": None,
        "icsRflag": "SOK",
        "icsRcode": "1",
        "reasonCode": "100",
        "currency": "KES",
        "amount": "14499.99",
        "clientApplicationUser": None,
        "retrievalReferenceNumber": "403223494441",
        "transRefNumber": [
            {
                "transRefNo": "70611116998176911113035"
            }
        ],
        "date": "Feb 02 2024 01:55:30 AM EET",
        "dmTransaction": False,
        "applications": [
            {
                "displayName": "Card Payments - Authorization",
                "status": "Success"
            },
            {
                "displayName": "Card Payments - Settlement",
                "status": "Success"
            }
        ],
        "ecommerceIndicatorLabel": "internet",
        "installmentIdentifier": None,
        "merchantDefinedData1": None,
        "merchantDefinedData2": None,
        "merchantDefinedData3": None,
        "merchantDefinedData4": None,
        "tokenId": None
    }, {
        "requestId": "70611116998176911113035",
        "partnerSolutionId": None,
        "referenceNumber": "100-0000",
        "firstName": "ELI XXXXX",
        "lastName": "XXXXX",
        "email": "abcdefg@gmail.com",
        "paymentMethod": "Visa",
        "merchantId": "absa_britam_0956516_kes",
        "accountSuffix": "4810",
        "authIndicator": None,
        "digitalPaymentMethod": None,
        "partnerOriginalTransactionId": None,
        "deviceId": None,
        "terminalSerialNumber": None,
        "processor": "vdcbarclayske",
        "businessApplicationId": None,
        "terminalId": None,
        "xid": None,
        "paTransactionId": None,
        "salesSlipNumber": None,
        "authorizationCode": "NOGIJA",
        "acquirerAccountId": None,
        "jccaTerminalId": None,
        "billingAddress1": "xyz",
        "billingCity": "abcd",
        "billingState": "N/A",
        "billingCountry": "KE",
        "billingPostalCode": "N/A",
        "billingPhoneNumber": "254722222222",
        "ipAddress": None,
        "shippingFirstName": None,
        "shippingLastName": None,
        "shippingAddress1": None,
        "shippingCity": None,
        "shippingState": None,
        "shippingPostalCode": None,
        "shippingCountry": None,
        "shippingPhoneNumber": None,
        "customerId": None,
        "clientApplication": "Recurring Billing Engine",
        "deviceFingerprint": None,
        "icsRflag": "SOK",
        "icsRcode": "1",
        "reasonCode": "200",
        "currency": "KES",
        "amount": "10500.00",
        "clientApplicationUser": None,
        "retrievalReferenceNumber": "403223996744",
        "transRefNumber": [
            {
                "transRefNo": "70611116998176911113035"
            }
        ],
        "date": "Feb 02 2024 01:54:59 AM EET",
        "dmTransaction": False,
        "applications": [
            {
                "displayName": "Card Payments - Settlement",
                "status": "Success"
            },
            {
                "displayName": "Card Payments - Authorization",
                "status": "Success"
            }
        ],
        "ecommerceIndicatorLabel": "internet",
        "installmentIdentifier": None,
        "merchantDefinedData1": None,
        "merchantDefinedData2": None,
        "merchantDefinedData3": None,
        "merchantDefinedData4": None,
        "tokenId": None
    }
]

# Iterate over the data and generate SQL insert statement if reasonCode is 100
for entry in data:
    if entry.get('reasonCode') == '100':
        requestId = entry.get('requestId', 'None')
        referenceNumber = entry.get('referenceNumber', 'None')
        firstName = entry.get('firstName', 'None')
        lastName = entry.get('lastName', 'None')
        billingPhoneNumber = entry.get('billingPhoneNumber', 'None')
        reasonCode = entry.get('reasonCode', 'None')
        amount = entry.get('amount', 'None')
		

        insert_statement = f"INSERT INTO your_table_name (requestId, referenceNumber, firstName, lastName, billingPhoneNumber, reasonCode, amount) VALUES ('{requestId}', '{referenceNumber}', '{firstName}', '{lastName}', '{billingPhoneNumber}', '{reasonCode}', '{amount}');"
        print(insert_statement)
