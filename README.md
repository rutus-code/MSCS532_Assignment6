
# **Assignment 6: Medians and Order Statistics & Elementary Data**

# **Created By: Rutu Shah** #
# **Created Date:  24th November 2024** #

## **Overview**  
This assignment focuses on implementing and analyzing selection algorithms and elementary data structures. It provides detailed performance analysis, empirical testing, and comparisons to highlight practical applications in real-world scenarios.

---

## **Contents**  

### **Part 1: Selection Algorithms**
1. **Implementation**  
   - Deterministic Algorithm: *Median of Medians*  
   - Randomized Algorithm: *Quickselect*  
2. **Performance Analysis**  
   - Time and space complexity breakdown.  
   - Practical considerations and overhead.
3. **Empirical Analysis**  
   - Implementation and benchmarking.  
   - Performance visualization for input distributions.  

### **Part 2: Elementary Data Structures**
1. **Implementation**  
   - Arrays, Matrices, Stacks, Queues, Linked Lists, and Rooted Trees.  
2. **Performance Analysis**  
   - Time complexity of basic operations.  
   - Comparison and trade-offs between structures.  
3. **Discussion**  
   - Practical applications of each data structure.  
   - Scenarios favoring one structure over another.  

4. **Conclusion**  
   Summary of findings and recommendations.  

---

## **Implementation Highlights**

### **Algorithms**
- **Median of Medians (Deterministic):** Guarantees \(O(n)\) worst-case time complexity.
- **Randomized Quickselect:** Offers \(O(n)\) expected time complexity with simpler implementation.

### **Data Structures**
- Arrays and Matrices: Basic structures for data storage and operations.  
- Stacks and Queues: Linear data structures for LIFO/FIFO operations.  
- Linked Lists: Flexible for dynamic memory allocation.  
- Rooted Trees: Efficient for hierarchical data.

---

## **Performance Insights**

### **Algorithms**
| Algorithm                 | Best Case | Average Case | Worst Case |
|---------------------------|-----------|--------------|------------|
| Median of Medians         | \(O(n)\) | \(O(n)\)     | \(O(n)\)   |
| Randomized Quickselect    | \(O(n)\) | \(O(n)\)     | \(O(n^2)\) |

### **Data Structures**
| Data Structure   | Insertion | Deletion | Access | Traversal |
|-------------------|-----------|----------|--------|-----------|
| Array            | \(O(n)\)  | \(O(n)\) | \(O(1)\) | \(O(n)\) |
| Stack (Array)    | \(O(1)\)  | \(O(1)\) | \(O(1)\) | N/A       |
| Queue (Array)    | \(O(1)\)  | \(O(n)\) | \(O(1)\) | N/A       |
| Linked List      | \(O(1)\)  | \(O(1)\) | \(O(n)\) | \(O(n)\) |
| Rooted Tree      | \(O(1)\)  | \(O(1)\) | \(O(n)\) | \(O(n)\) |

---

## **How to Run**

### **Requirements**
- Python 3.x  
- Libraries: `matplotlib`, `numpy`

### **Steps**
1. Clone the repository:  
   ```bash
   git clone https://github.com/rutus-code/MSCS532_Assignment6
   cd MSCS532_Assignment6
   ```
2. Run the implementations:

   1. For Part 1 Implementation
   ```bash
   python3 selection_algorithms.py
   ```
   
   ```
   python3 data_structures.py
   ```

   2. View empirical analysis:  
   ```bash
   python empirical_analysis.py
   ```

   3. For Part 2 Implementation
   ```
   python3 arrays.py
   ```
   
   ```
   python3 matrices.py
   ```
   
   ```
   python3 queues.py
   ```
   
   ```
   python3 stack.py
   ```

   ```
   python3 singlyLinkedList.py
   ```

   ```
   python3 rootedTress.py
   ```
---

## **Practical Applications**

1. **Selection Algorithms**  
   - Randomized Quickselect for real-time systems requiring quick computations.  
   - Median of Medians for worst-case performance guarantees.

2. **Data Structures**  
   - **Arrays and Matrices**: Image processing, numerical computations.  
   - **Stacks and Queues**: Function calls, task scheduling, BFS/DFS.  
   - **Linked Lists**: Dynamic memory management, undo functionality.  
   - **Rooted Trees**: File systems, decision-making algorithms, prefix trees.

---

## **GitHub Repository**  
Access the full code and details [here](https://github.com/rutus-code/MSCS532_Assignment6).

---

## **References**  
1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.  
2. Goodrich, M. T., & Tamassia, R. (2011). *Data Structures and Algorithms in Python*. Wiley.  
3. Knuth, D. E. (1998). *The Art of Computer Programming, Vol. 1: Fundamental Algorithms* (3rd ed.). Addison-Wesley.  

---
