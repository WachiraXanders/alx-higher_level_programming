#include <stdio.h>
#include "hash_tables.h"

/**
 * hash_table_print - Prints a hash table
 * @ht: The hash table
 */
void hash_table_print(const hash_table_t *ht)
{
	unsigned long int i;
	hash_node_t *current_node;
	int comma_flag = 0;

	if (ht == NULL)
		return;

	printf("{");
	for (i = 0; i < ht->size; i++)
	{
		current_node = ht->array[i];
		while (current_node != NULL)
		{
			if (comma_flag == 1)
				printf(", ");
			printf("'%s': '%s'", current_node->key, current_node->value);
			comma_flag = 1;
			current_node = current_node->next;
		}
	}
	printf("}\n");
}
