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
	int i = 0;

	if (h == NULL)
		return (1);

	while (h != NULL)
	{
		tab = realloc(tab, (len * 4) + 4);
		*(tab + len++) = h->n;
		h = h->next;
	}
	while (i < len / 2)
	{
		if (tab[i] != tab[len - i - 1])
			return (0);
		i++;
	}
	free(tab);
	return (1);
}
