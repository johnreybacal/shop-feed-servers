<?php

namespace App\MessageHandler;

use App\Message\UserMutation;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

#[AsMessageHandler]
class UserMutationHandler
{
    public function __invoke(UserMutation $event)
    {
        echo $event->getEventType();
        echo $event->getUser();
    }
}
