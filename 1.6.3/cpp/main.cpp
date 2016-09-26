#include <iostream>
#include <iomanip>
#include <math.h>

/**
 * Your job is to compute, from a list of expenses, the minimum amount of money that must
 *  change hands in order to equalize (within one cent) all the students’ costs.
 */

unsigned int TERMINATE = 0;

int main() {
    unsigned int numberOfStudents;

    std::cin >> numberOfStudents;

    while (numberOfStudents != TERMINATE) {
        double expenses[numberOfStudents];
        double total = 0.00;
        double payback = 0.00;
        for (unsigned int i = 0; i < numberOfStudents; i++)
        {
            std::cin >> expenses[i];
            total += expenses[i];
        }

        double average = total / numberOfStudents;

        for (unsigned int i = 0; i < numberOfStudents; i++)
        {
            double difference = expenses[i] - average;
            if (difference > 0)
            {
                payback = floorf((difference + payback) * 100 ) / 100;
            }
        }

        std::cout << std::setprecision(4) << std::showpoint;
        std::cout << "The total is: $" << total << std::endl;
        std::cout << "The minimum that needs to change hands is: $" << payback <<std::endl;

        std::cin >> numberOfStudents;
    }

    return 0;
}