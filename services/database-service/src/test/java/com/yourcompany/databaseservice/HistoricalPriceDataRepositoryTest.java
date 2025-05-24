// services/database-service/src/test/java/com/yourcompany/databaseservice/HistoricalPriceDataRepositoryTest.java

package com.yourcompany.databaseservice;

import org.junit.jupiter.api.Test;
import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;

public class HistoricalPriceDataRepositoryTest {

    @Test
    void testSavePriceData() {
        HistoricalPriceDataRepository repository = new HistoricalPriceDataRepository();
        LocalDate testDate = LocalDate.of(2023, 10, 26);

        // Verify that calling savePriceData does not throw an exception
        assertDoesNotThrow(() -> repository.savePriceData(
            "TEST",
            testDate,
            110.0,
            115.0,
            108.0,
            112.0,
            150000
        ));

        // In a real test, you would verify interaction with a mocked database
        // or check the output if testing the printing behavior.
    }
}
