public class OrderedMap<Key extends Comparable<Key>, Value> implements Map<Key, Value> {

    // Typing variables 
        private Key[] keys ;
        private Value[] values ;
        private int numElements ;
        private int max_array_size ;
    
        // Constructer
         @SuppressWarnings("unchecked")
         public OrderedMap(int maxSize) {
             keys = (Key[])new Comparable[maxSize] ;
             values = (Value[])new Object[maxSize] ;
             numElements = 0;
             max_array_size = maxSize ;
         }

         public boolean contains(Key key) {
            return BinarySearch.exists( keys, 0, numElements, key) ;
         }

        public Key minKey() {
            return keys[0] ;
        }

         public Key maxKey() {
             return keys[numElements - 1] ; 
        }

        public int size() {
            return numElements ;
        }

        public boolean isEmpty() {
            if (numElements == 0) {
                return true ; 
            } 
            else {  
                return false ;
            }    
        }

        public Value get(Key key) {
            boolean is_contains = contains(key) ; 
            if (is_contains) {
                int idx = BinarySearch.lowerBound(keys, 0, numElements, key);
                return values[idx] ;
            }
            else {
                return null ;
            }
        }

        public void put(Key key, Value value) {
            // case #1: numelements = maxsize 
            // case #2: when we need to update an existing key with a new value 
            // case #3: when we need to insert a new key into the respected value
            if ( numElements > 0 && numElements < max_array_size) {
                if (contains(key) == true) {
                    // handle case #2
                    int idx = BinarySearch.lowerBound(keys, 0, numElements, key);
                    values[idx] = value ;
                } 
                else {
                    // handle case #3
                    // insert the new key into the keys array and sort it
                    int idx = BinarySearch.lowerBound(keys, 0, numElements, key);
                    if (idx == numElements || !keys[idx].equals(key)) {
                        keys[numElements++] = key;
                        ArrayUtils.rotateRight(keys, idx, numElements);
                    }
                        ArrayUtils.rotateRight(values, idx, numElements);
                        values[idx] = value;
                }
            } 
            else if(numElements == 0) {
                // handles adding the first key/value pair to the map
                keys[0] = key ;
                values[0] = value ;
                numElements = 1 ;
            }
        }
        
        public String toString() {
            String return_string = "[" ;
            for (int index = 0 ; index < numElements ; index++) {
                return_string = return_string + " (" + keys[index] + " " + values[index] + ")" ;
            }
            return_string = return_string + " ]" ;
            return return_string ; 
        }
     }