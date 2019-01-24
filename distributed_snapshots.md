# Distributed Snapshots 1/24

### Terms

Global States
Snapshots -- Chandy-Lamport Algorithm

### Global State
Find global property with only local observations at any time -- no gloabl observation
Eg., counting people in all EWS labs. 
    * One option is to go to every lab and count people one after another -- this is a bad solution.
    * Send one person to every lab to count. Synchronization is a problem here. Granularity of time synchonization needn't be 1us though.
    
### Distributed Garbage Collection
Newspaper on kitchen counter. Recycle after everyone is done. Go to everyone and asl 'Are you done?'. When do you know if it is ok to recycle ? If everyone says he is done, it is ok to recycle. 
 * *Stable Property* : Property checked once, it is likely to stay at the same in the future. Eg. Reading a paper. Termination of a job is a similar problem.
 * *Checkpoint* : Saved version of the state, so that in case the system crashes, it can recover to a 'known good' state.
 
### Histories
Say you have a process p1, which experiences events (computation/communication).

* History is the set of all the events happened in the process' lifetime.
* Prefix history is the first k events in the history
* Si(k) -- Pi's state after k events
* Global state -- Union of the process states at each of the process' local time. Eg., S1(3) U S2(5) U S3(2). Combining state of process' across at different times.
* Cut -- A collection of prefix histories. The prefixes can be at a different index for different processes. h1(3) U h2(5) U h3(2)
* Frontier -- last event in a cut

A cut is **consistent** iff for any event if something happened before, it is included as well. Inconsistence is possible if it includes receive but not send.

```
Whenever there is a consistent cut, we have a global snapshot
```
### Chandy Lamport Algorithm
Idea is to record state of every process, every channel -- this should capture the state assuming we pick a consistent cut.

**Assumptions** : Reliable, in-order(FIFO) channels. 
Each process records it own state (no central collection)
Snapshot can be initiated by anyone.

### Intuition: 

Contagion --  each process has 2 states: blue (before), Read(after snaphots). To initiate, color self red, send red marker to other process, When a blue marker receives it, it colors itself red and sends it to every other processes.

When a process is marked red, it turns on recording on incoming channels. A channel on which marker is received is marked emty.
Eg., Hamster example.
Q. How is it *consistent*? Conservation property. At no point was the state previously this particular consistent state.
Q. Why is FIFO important?
FIFO: So that messages in flight are counted before markers.
Q. if ei --> ej. If ej is in the cut, then ei is also in the cut.
Proof of Chandy-Lamport Algorithm -- Refer slides.

### Notion of Predicates
Idea: We have a sequence of events, at different times at different processes. One way is to put all these events in a sequence. A run is to take all events across all processes and then order them, *without* a global view of time.
Linearization: if it is consistent with happens-before(partial order) relationship. We can think of a Distributed System as evolving through a set of global state.

Liveness Property: Eventually come to a state where everyone terminates irrespective of the way you order them. Guarantee of termination.
Safety Property: For all sequences of states, does safety hold? guarantee that something bad will never happen.

It is imp to understand which prop is wanted in our DS>CS







