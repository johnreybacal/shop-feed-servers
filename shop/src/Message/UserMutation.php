<?php

namespace App\Message;

use App\Entity\User;

class UserMutation
{
    private string $eventType;
    private User $user;

    public function __construct(string $eventType, User $user)
    {
        $this->eventType = $eventType;
        $this->user = $user;
    }

    public function getEventType(): string
    {
        return $this->eventType;
    }

    public function getUser(): User
    {
        return $this->user;
    }
}
