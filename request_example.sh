curl http://127.0.0.1/invocations -H "Content-Type: application/json" --data '{
  "inputs": [
    {
      "num__Age": 22,
      "num__Fare": 7.25,
      "num__Siblings/Spouses Aboard": 1,
      "num__Parents/Children Aboard": 0,
      "cat__Pclass_1": 1,
      "cat__Pclass_2": 0,
      "cat__Pclass_3": 0,
      "cat__Sex_female": 0,
      "cat__Sex_male": 1
    },
    {
      "num__Age": 38,
      "num__Fare": 71.83,
      "num__Siblings/Spouses Aboard": 1,
      "num__Parents/Children Aboard": 0,
      "cat__Pclass_1": 0,
      "cat__Pclass_2": 0,
      "cat__Pclass_3": 1,
      "cat__Sex_female": 1,
      "cat__Sex_male": 0
    },
    {
      "num__Age": 22,
      "num__Fare": 7.25,
      "num__Siblings/Spouses Aboard": 1,
      "num__Parents/Children Aboard": 0,
      "cat__Pclass_1": 1,
      "cat__Pclass_2": 0,
      "cat__Pclass_3": 0,
      "cat__Sex_female": 0,
      "cat__Sex_male": 1
    }
  ]
}'
