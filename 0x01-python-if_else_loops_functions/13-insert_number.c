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
	int add = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = (NULL);

	current = *head;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	while (current != NULL && current->next != NULL)
	{
	if (current->n <= number && number < current->next->n)
	{
		tmp = current->next;
		current->next = new;
		new->next = tmp;
		add = 1;
	}

	current = current->next;
	}

	if (add == 0)
	{
		current->next = new;
	}
	return (new);
}
