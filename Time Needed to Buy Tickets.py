def timeRequiredToBuy(tickets, k):
        ans = 0

        for i, ticket in enumerate(tickets):
            if i <= k:
                ans += min(ticket, tickets[k])
            else:
                ans += min(ticket, tickets[k] - 1)

        return ans

tickets =[2,3,2]
k=2
print(timeRequiredToBuy(tickets, k))
