#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

/**
 * struct listint_s - singly list
 * @n: integer
 * @next:points to the next node
 *
 * descriptio n:singly linked list node structure
 * for alx project
 */
typedef struct listint_s
{
	size_t print_listint(const listint_t *h);
	listint_t *add_nodeint(listint_t **head, const int n);
	void free_listint(listint_t *head);
	int check_cycle(listint_t *list);

	endif /* LISTS_H */
}
