#include "lists.h"

/*
 * aux_plain - recurses on the linked list
 * @head: head of the list
 * @end: end of the list
 * Returns: 0 if not 1 if true
 */

int aux_palin(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/*
 * is_plaindrome - function to know if this list is plaindrome
 * @head: head of the list
 * Returns: 1 if plaindrome 0 if not
 */

int is_plaindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_plain(head, *head);
}
