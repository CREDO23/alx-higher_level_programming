#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *h;
	listint_t *tl;

	if (list == NULL)
		return (0);

	h = list;
	tl = list;

	while (tl != NULL && tl->next != NULL)
	{
		h = h->next;
		tl = tl->next->next;

		if (h == tl)
			return (1);

	}
	return (0);
}