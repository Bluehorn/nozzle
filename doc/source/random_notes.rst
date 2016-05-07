Random notes
============


More abstraction
----------------

How can the injection mechanism be used to inject simple method or function calls?  Like for event handling
where you can pass a lot of information to an event handler but the basic usages of the event don't care for
most of the information. Or for extending an event with additional information when it is already used, where
injection will only pass the requested information to the event handler.


Dependency Graph
----------------

To reduce the fear from the magic of the injections, it should be possible to create a graph about the
configuration of the injector so that one can check what will be injected without running the code.


Static Analysis
---------------

To reduce the risk that things break at runtime it should be possible to scan a code base and have all
injections checked for usability. My goal would be to have a viable default injection for every class so that
the injector can create an instance without any configuration.

For unit testing a different default should be selectable to use less expensive implementations. Finally, the
configurations should be detectable from their modules so that each configuration is checked for validity
before any application code is run.
