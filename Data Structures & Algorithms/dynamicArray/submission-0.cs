public class DynamicArray {
    private int[] container;
    private int size;
    private int capacity;
    public DynamicArray(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        container = new int [capacity];
    }

    public int Get(int i) {
        return container[i];
    }

    public void Set(int i, int n) {
        container[i] = n;
   
    }

    public void PushBack(int n) {
        if(size == capacity)
            Resize();
        container[size] = n;
        size++;
    }

    public int PopBack() {
        var element = container[size - 1];
        size--;
        return element;
    }

    private void Resize() {
        capacity = capacity * 2;
        var newContainer = new int [capacity];
        Array.Copy(container, newContainer, size);
        container = newContainer;
    }

    public int GetSize() {
        return size;
    }

    public int GetCapacity() {
        return capacity;
    }
}
