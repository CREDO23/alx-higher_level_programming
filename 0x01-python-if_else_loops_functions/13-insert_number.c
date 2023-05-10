#include "lists.h"
/**
 * listint_t - Insert a node in the listin list on asc order
 * @head: The adress of the head of the ll
 * @number: The number of the new node
 *
 * Return: The adress of the new node , NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *tmp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = (NULL);

	current = *head;

	while (current != NULL)
	{
	if (current->n <= number && number < current->next->n)
	{
		tmp = current->next;
		current->next = new;
		new->next = tmp;
	}

	current = current->next;
	}
	return (new);
}
