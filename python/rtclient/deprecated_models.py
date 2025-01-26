"""
This module contains message types that are currently not in use.
These types are kept for reference and potential future use.
"""

from typing import Annotated, Literal, Optional, Union

from pydantic import BaseModel, Field

from .models import RealtimeError, ResponseItem, ServerMessageBase


class InputAudioBufferClearedMessage(ServerMessageBase):
    """Signals the server has cleared the audio buffer."""
    type: Literal["input_audio_buffer.cleared"] = "input_audio_buffer.cleared"


class ItemTruncatedMessage(ServerMessageBase):
    type: Literal["conversation.item.truncated"] = "conversation.item.truncated"
    item_id: Optional[str]
    content_index: Optional[int]
    audio_end_ms: Optional[int]


class ItemDeletedMessage(ServerMessageBase):
    type: Literal["conversation.item.deleted"] = "conversation.item.deleted"
    item_id: Optional[str]


class ItemInputAudioTranscriptionFailedMessage(ServerMessageBase):
    type: Literal["conversation.item.input_audio_transcription.failed"] = (
        "conversation.item.input_audio_transcription.failed"
    )
    item_id: Optional[str]
    content_index: Optional[int]
    error: Optional[RealtimeError]


class ResponseOutputItemAddedMessage(ServerMessageBase):
    type: Literal["response.output_item.added"] = "response.output_item.added"
    response_id: Optional[str]
    output_index: Optional[int]
    item: Optional[ResponseItem]


class ResponseOutputItemDoneMessage(ServerMessageBase):
    type: Literal["response.output_item.done"] = "response.output_item.done"
    response_id: Optional[str]
    output_index: Optional[int]
    item: Optional[ResponseItem]


class ResponseContentPartAddedMessage(ServerMessageBase):
    type: Literal["response.content_part.added"] = "response.content_part.added"
    response_id: Optional[str]
    item_id: Optional[str]
    output_index: Optional[int]
    content_index: Optional[int]


class ResponseContentPartDoneMessage(ServerMessageBase):
    type: Literal["response.content_part.done"] = "response.content_part.done"
    response_id: Optional[str]
    item_id: Optional[str]
    output_index: Optional[int]
    content_index: Optional[int]


class ResponseTextDeltaMessage(ServerMessageBase):
    type: Literal["response.text.delta"] = "response.text.delta"
    response_id: Optional[str]
    item_id: Optional[str]
    output_index: Optional[int]
    content_index: Optional[int]
    delta: Optional[str]


class ResponseTextDoneMessage(ServerMessageBase):
    type: Literal["response.text.done"] = "response.text.done"
    response_id: Optional[str]
    item_id: Optional[str]
    output_index: Optional[int]
    content_index: Optional[int]
    text: Optional[str]


class ResponseAudioDoneMessage(ServerMessageBase):
    type: Literal["response.audio.done"] = "response.audio.done"
    response_id: Optional[str]
    item_id: Optional[str]
    output_index: Optional[int]
    content_index: Optional[int]


class ResponseFunctionCallArgumentsDeltaMessage(ServerMessageBase):
    type: Literal["response.function_call_arguments.delta"] = "response.function_call_arguments.delta"
    response_id: Optional[str]
    item_id: Optional[str]
    output_index: Optional[int]
    call_id: Optional[str]
    delta: Optional[str]


class RateLimits(BaseModel):
    name: str
    limit: int
    remaining: int
    reset_seconds: float


class RateLimitsUpdatedMessage(ServerMessageBase):
    type: Literal["rate_limits.updated"] = "rate_limits.updated"
    rate_limits: list[RateLimits]


DeprecatedServerMessageType = Annotated[
    Union[
        InputAudioBufferClearedMessage,
        ItemTruncatedMessage,
        ItemDeletedMessage,
        ItemInputAudioTranscriptionFailedMessage,
        ResponseOutputItemAddedMessage,
        ResponseOutputItemDoneMessage,
        ResponseContentPartAddedMessage,
        ResponseContentPartDoneMessage,
        ResponseTextDeltaMessage,
        ResponseTextDoneMessage,
        ResponseAudioDoneMessage,
        ResponseFunctionCallArgumentsDeltaMessage,
        RateLimitsUpdatedMessage,
    ],
    Field(discriminator="type"),
] 