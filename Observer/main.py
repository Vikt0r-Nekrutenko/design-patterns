from Observer.Observable import Publisher
from Observer.Observers import Post
from Observer.Subscribers import NewspaperSubscriber, JournalSubscriber


pub1 = Publisher()
post = Post()

sub1 = NewspaperSubscriber("Man")
sub2 = JournalSubscriber("Woman")

pub1.add_observer(post)

post.add_observer(sub1)
post.add_observer(sub2)

pub1.notify_observers()