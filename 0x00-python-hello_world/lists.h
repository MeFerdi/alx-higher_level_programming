#ifndef LISTS_H
#define LISTS_H

#include<stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: Points to the next node
 *
 * Description: singly linked list node structure for the ALX tasks
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint_t;



#endif /*LISTS_H*/
