def summarize_sales(sales):
    result = {}
    result["count"] = len(sales)
    result["total"] = sum(sales)
    result["average"] = result["total"] / max(1, result["count"])
    result["min"] = min(sales) if sales else 0
    result["max"] = max(sales) if sales else 0
    result["positive_count"] = len([x for x in sales if x > 0])
    result["negative_count"] = len([x for x in sales if x < 0])
    result["is_empty"] = len(sales) == 0
    result["formatted"] = (
        f"count={result['count']}, total={result['total']}, avg={result['average']:.2f}"
    )
    return result


def summarize_purchases(purchases):
    result = {}
    result["count"] = len(purchases)
    result["total"] = sum(purchases)
    result["average"] = result["total"] / max(1, result["count"])
    result["min"] = min(purchases) if purchases else 0
    result["max"] = max(purchases) if purchases else 0
    result["positive_count"] = len([x for x in purchases if x > 0])
    result["negative_count"] = len([x for x in purchases if x < 0])
    result["is_empty"] = len(purchases) == 0
    result["formatted"] = (
        f"count={result['count']}, total={result['total']}, avg={result['average']:.2f}"
    )
    return result

def summarize_purchases(purchases):
    result = {}
    result["count"] = len(purchases)
    result["total"] = sum(purchases)
    result["average"] = result["total"] / max(1, result["count"])
    return result


def _summarize_values(values):
    count = len(values)
    total = sum(values)
    average = total / max(1, count)
    return {
        "count": count,
        "total": total,
        "average": average,
        "min": min(values) if values else 0,
        "max": max(values) if values else 0,
        "positive_count": len([x for x in values if x > 0]),
        "negative_count": len([x for x in values if x < 0]),
        "is_empty": count == 0,
        "formatted": f"count={count}, total={total}, avg={average:.2f}",
    }


def summarize_sales(sales):
    return _summarize_values(sales)


def summarize_purchases(purchases):
    return _summarize_values(purchases)