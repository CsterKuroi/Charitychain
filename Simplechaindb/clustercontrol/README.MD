## clustercontrol

##shell+fabric

##control
```
configure blockchain-nodes

./clustercontrol.sh  start   启动整个集群
./clustercontrol.sh  stop    关闭整个集群

./startnode.sh  -h user@host   -p password   [ -r ]  [ -b ]   启动指定的节点。 -r 启动 该节点上的rethinkdb ，-b 启动该节点上的bigchaindb。

./stopnode.sh  -h user@host   -p password   [ -r ]  [ -b ]   关闭指定的节点。 -r 关闭 该节点上的rethinkdb ，-b 关闭该节点上的bigchaindb。
```
