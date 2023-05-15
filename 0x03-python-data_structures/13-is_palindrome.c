#include "lists.h"

/**
 * is_palindrome - Checks palindrome singly linked lists
 * @head: list head
 * Return: 1 if the list is a palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	listint_t *h = *head;
	int *tab =  NULL;
	int len = 0;
	int i;

	if (h == NULL)
		return (1);

	while (h != NULL)
	{
		tab = realloc(tab, (len * 4) + 4);
		*(tab + len++) = h->n;
		h = h->next;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (tab[i] != tab[len - i - 1])
			return (0);
	}
	free(tab);
	return (1);
}
