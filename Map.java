public interface Map<Key, Value> {

    // adds key to the map with the given value; 
    // if the map already has an entry for key, it just updates the value
    void put(Key key, Value value) ;

    // returns the value associated with key
    // , or null if their is no entry for key
    Value get(Key key) ;

    // returns true if their is an entry in the map for key, false otherwise
    boolean contains(Key key) ;

    // returns the maximum key in the map
    Key maxKey() ;

    // returns the minimum key in the map
    Key minKey() ;

    // returns the number of entries (key/value pairs) in the map
    int size() ;
    
    // returns true if the map has no entries, false otherwise
    boolean isEmpty() ;
    
    
     
    
 }