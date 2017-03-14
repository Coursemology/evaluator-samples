// Tests Factorial().

// Public tests have `public` in their test case name
TEST(FactorialPublic, test_public_1) {
  EXPECT_EQ(1, Factorial(-5));
  RecordProperty("expression", "Factorial(-5)");
  RecordProperty("output", Factorial(-5));
  RecordProperty("expected", 1);
}

TEST(FactorialPublic, test_public_2) {
  EXPECT_EQ(6, Factorial(3));
  RecordProperty("expression", "Factorial(3)");
  RecordProperty("output", Factorial(3));
  RecordProperty("expected", 6);
}

// Private tests have `private` in their test case name
TEST(FactorialPrivate, test_private_1) {
  EXPECT_EQ(1, Factorial(0));
  RecordProperty("expression", "Factorial(0)");
  RecordProperty("output", Factorial(0));
  RecordProperty("expected", 1);
}

// Evaluation tests have `evaluation` in their test case name
TEST(FactorialEvaluation, test_evaluation_1) {
  EXPECT_EQ(40320, Factorial(8));
  RecordProperty("expression", "Factorial(8)");
  RecordProperty("output", Factorial(8));
  RecordProperty("expected", 40320);
}

