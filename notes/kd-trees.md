---
title: "k-d Trees"
layout: single
sidebar:
  nav: "ml"
---

# k-d Trees for Nearest-Neighbor Search

(authored by Claude, edited lightly by Dr. White)

To classify a point with k-NN, we need its nearest neighbors in the training set. The brute-force way is to compute the distance to every point and keep the smallest. That works, but it costs $n$ distance computations for every query. If you have a million training points and want to classify a thousand new ones, that adds up to a billion distance computations.

Using the idea of binary search in more dimensions turns out to work, but there's a bit of geometry that makes it hard. The closest point is not always the last point we find in the binary search tree. We have to work a bit harder.

A **k-d tree** (short for "k-dimensional tree") is built like a binary search tree, but it takes turns between the axes. It splits on $x$, then on $y$, then on $x$ again, and so on. That way it can prune in every direction.

## Building the tree

The rule is short. Given a set of points:

1. Pick the axis for this level: $x$ at the root, $y$ one level down, $x$ again below that, and so on.
2. Sort the points on that axis and take the **median** point. It becomes this node.
3. Points with a smaller coordinate go to the left subtree and points with a larger one go to the right. Build each subtree the same way, one level down.

Here are seven points and the tree they produce:

![Seven points, the lines that split them, and the k-d tree they form]({{ '/notes/kd-trees-build.svg' | relative_url }})

D has the median $x$-value (6 out of 1, 3, 4, 6, 7, 8, 9), so it becomes the root, and its vertical line $x = 6$ splits the plane in half. On the left side, the median $y$ among A, B and C is A's, so A splits the left half with the horizontal line $y = 4$. That line only runs from $x = 0$ to $x = 6$, because A only owns the left half. The same thing happens on the right with G. At the bottom level, C, B, F and E each split their own small rectangles on $x$ again.

Two things to notice:

- **Every node owns a rectangle.** The root owns the whole plane. Each child owns one side of its parent's line. Each line only runs across its own node's rectangle, which is why the picture looks like a set of nested boxes rather than a grid. The tree and the boxes are the same information, drawn two ways.
- **The tree is balanced.** Splitting at the median puts half the points on each side, so a tree on $n$ points has about $\log_2 n$ levels. A million points gives about 20 levels.

## Searching the tree

Finding the nearest neighbor of a query point $q$ happens in two phases.

**Going down.** Start at the root and walk toward $q$ the way a binary search would. At each node, compare $q$'s coordinate to the node's split value and go left or right, or for a $y$-split, down or up. Along the way, compute the distance from $q$ to each node you pass and remember the closest one so far. When you hit the bottom, you have a pretty good candidate after only about $\log_2 n$ distance computations.

**Coming back up.** The candidate might not be the true nearest neighbor, because the nearest point could sit just across one of the lines we passed. So we walk back up the same path. At each node we ask: *could a closer point be hiding on the other side of this node's line?*

The answer uses the distance to the closest partition line. Any point on the far side of a vertical line $x = s$ is at least $|q_x - s|$ away from $q$. If that gap is **bigger** than our best distance so far, nothing over there can win, and we skip that entire subtree without computing a single distance. If the gap is **smaller**, we have to go look. We search the other side the same way, going down toward $q$ and then back up, and we carry our best-so-far along.

There's a nice way to picture this. Draw a circle around $q$ with radius equal to the best distance so far. A line that the circle doesn't reach can't hide anything closer. A line the circle crosses has to be checked.

Here's an example with the query $q = (5, 9)$:

![The query point with its search circles]({{ '/notes/kd-trees-search.svg' | relative_url }})

Going down, we visit D (left, since $5 < 6$), then A (up, since $9 > 4$), then B at the bottom. B is the closest so far at distance $\sqrt{5} \approx 2.24$, which is the dashed circle.

Coming back up, we first check A's line $y = 4$. The gap is $9 - 4 = 5$, bigger than 2.24, so C's whole region is skipped. Next is D's line $x = 6$. The gap is only 1, and the circle clearly crosses it, so we have to search the right side. Going down there, we visit G and then E, and E turns out to be closer, at distance exactly 2 (the solid circle). Finally, G's line $y = 6$ is 3 away, which is bigger than 2, so F is skipped.

The answer is E. We computed 5 distances instead of 7. That's not much of a savings with 7 points, but the skipped regions get much bigger as $n$ grows.

In code, the whole search is a short recursive function:

```python
def search(node, q, best):
    if node is None:
        return best
    best = min(best, (dist(node.point, q), node.point))
    gap = q[node.axis] - node.point[node.axis]
    near, far = (node.left, node.right) if gap < 0 else (node.right, node.left)
    best = search(near, q, best)          # going down
    if abs(gap) < best[0]:                # coming back up: does the circle cross the line?
        best = search(far, q, best)
    return best

best_dist, nearest = search(root, q, (float("inf"), None))
```

For k-NN with $k > 1$, keep the $k$ best points instead of one. The circle's radius is then the distance to the $k$-th best.

## When it helps, and when it doesn't

In good cases the search touches about $\log_2 n$ nodes instead of $n$, which is a huge win. A million points needs a few dozen distance computations instead of a million. The bad cases are queries that sit close to many splitting lines, or far away from all the data. Either way, the circle stays big compared with the gaps, it crosses a lot of lines, and the search ends up visiting much of the tree.

Dimension matters a lot. In 2-d, each level cuts the space in half along one axis. In 50 dimensions, a balanced tree on a million points only has about 20 levels, so most of the axes never get split at all. On top of that, distances between points in high dimensions tend to be similar, so the circle (now a hypersphere) crosses almost everything. As a rough rule, k-d trees are great up to about 10 to 20 dimensions and then lose to brute force. Past that point, large systems switch to *approximate* nearest-neighbor methods, which give up the guarantee of finding the exact nearest point in exchange for speed.

## What to do next

1. Open the [k-d tree explorer]({{ '/notebooks/05-classification/kdtree-explorer.html' | relative_url }}). On the **Build** tab, step through the construction slowly and watch the plane and the tree change together. Before each median gets placed, predict which point it will be.
2. On the **Search** tab, run the three example queries in order. For each one, predict before every "coming back up" step whether the search will cross the line or skip it. Then click your own query points and try to find one that forces the search to visit almost every node.
3. Do the worksheet by hand.
