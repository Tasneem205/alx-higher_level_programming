#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checkes if there is a cycle
 * @list: pointer
 * Return: boolean
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->fast->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
