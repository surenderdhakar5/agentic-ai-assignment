# Design Decisions

## Architecture

Customer

↓

run_agent()

↓

Select Tool

↓

Execute Tool

↓

Generate Response

## Tools

get_order()

Returns order information.

get_product()

Returns product information.

search_products()

Searches available products.

## Error Handling

- Invalid Order ID
- Invalid Product ID
- Empty Search Results

## Logging

Every tool call is stored inside agent.log.