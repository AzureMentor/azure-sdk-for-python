# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TextAnalyticsClientOperationsMixin:

    async def entities_recognition_general(
        self,
        documents: List["_models.MultiLanguageInput"],
        model_version: Optional[str] = None,
        show_stats: Optional[bool] = None,
        string_index_type: Optional[Union[str, "_models.StringIndexType"]] = "TextElements_v8",
        **kwargs
    ) -> "_models.EntitiesResult":
        """Named Entity Recognition.

        The API returns a list of general named entities in a given document. For the list of supported
        entity types, check :code:`<a href="https://aka.ms/taner">Supported Entity Types in Text
        Analytics API</a>`. See the :code:`<a href="https://aka.ms/talangs">Supported languages in Text
        Analytics API</a>` for the list of enabled languages.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_1_preview_2.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics.
        :type show_stats: bool
        :param string_index_type: (Optional) Specifies the method used to interpret string offsets.
         Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information
         see https://aka.ms/text-analytics-offsets.
        :type string_index_type: str or ~azure.ai.textanalytics.v3_1_preview_2.models.StringIndexType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EntitiesResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_1_preview_2.models.EntitiesResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EntitiesResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _input = _models.MultiLanguageBatchInput(documents=documents)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.entities_recognition_general.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if model_version is not None:
            query_parameters['model-version'] = self._serialize.query("model_version", model_version, 'str')
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')
        if string_index_type is not None:
            query_parameters['stringIndexType'] = self._serialize.query("string_index_type", string_index_type, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_input, 'MultiLanguageBatchInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('EntitiesResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    entities_recognition_general.metadata = {'url': '/entities/recognition/general'}  # type: ignore


    async def entities_recognition_pii(
        self,
        documents: List["_models.MultiLanguageInput"],
        model_version: Optional[str] = None,
        show_stats: Optional[bool] = None,
        domain: Optional[str] = None,
        string_index_type: Optional[Union[str, "_models.StringIndexType"]] = "TextElements_v8",
        **kwargs
    ) -> "_models.PiiEntitiesResult":
        """Entities containing personal information.

        The API returns a list of entities with personal information (\"SSN\", \"Bank Account\" etc) in
        the document. For the list of supported entity types, check :code:`<a
        href="https://aka.ms/tanerpii">Supported Entity Types in Text Analytics API</a>`. See the
        :code:`<a href="https://aka.ms/talangs">Supported languages in Text Analytics API</a>` for the
        list of enabled languages.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_1_preview_2.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics.
        :type show_stats: bool
        :param domain: (Optional) if set to 'PHI', response will contain only PHI entities.
        :type domain: str
        :param string_index_type: (Optional) Specifies the method used to interpret string offsets.
         Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information
         see https://aka.ms/text-analytics-offsets.
        :type string_index_type: str or ~azure.ai.textanalytics.v3_1_preview_2.models.StringIndexType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PiiEntitiesResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_1_preview_2.models.PiiEntitiesResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PiiEntitiesResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _input = _models.MultiLanguageBatchInput(documents=documents)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.entities_recognition_pii.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if model_version is not None:
            query_parameters['model-version'] = self._serialize.query("model_version", model_version, 'str')
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')
        if domain is not None:
            query_parameters['domain'] = self._serialize.query("domain", domain, 'str')
        if string_index_type is not None:
            query_parameters['stringIndexType'] = self._serialize.query("string_index_type", string_index_type, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_input, 'MultiLanguageBatchInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PiiEntitiesResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    entities_recognition_pii.metadata = {'url': '/entities/recognition/pii'}  # type: ignore


    async def entities_linking(
        self,
        documents: List["_models.MultiLanguageInput"],
        model_version: Optional[str] = None,
        show_stats: Optional[bool] = None,
        string_index_type: Optional[Union[str, "_models.StringIndexType"]] = "TextElements_v8",
        **kwargs
    ) -> "_models.EntityLinkingResult":
        """Linked entities from a well-known knowledge base.

        The API returns a list of recognized entities with links to a well-known knowledge base. See
        the :code:`<a href="https://aka.ms/talangs">Supported languages in Text Analytics API</a>` for
        the list of enabled languages.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_1_preview_2.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics.
        :type show_stats: bool
        :param string_index_type: (Optional) Specifies the method used to interpret string offsets.
         Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information
         see https://aka.ms/text-analytics-offsets.
        :type string_index_type: str or ~azure.ai.textanalytics.v3_1_preview_2.models.StringIndexType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EntityLinkingResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_1_preview_2.models.EntityLinkingResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EntityLinkingResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _input = _models.MultiLanguageBatchInput(documents=documents)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.entities_linking.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if model_version is not None:
            query_parameters['model-version'] = self._serialize.query("model_version", model_version, 'str')
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')
        if string_index_type is not None:
            query_parameters['stringIndexType'] = self._serialize.query("string_index_type", string_index_type, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_input, 'MultiLanguageBatchInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('EntityLinkingResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    entities_linking.metadata = {'url': '/entities/linking'}  # type: ignore


    async def key_phrases(
        self,
        documents: List["_models.MultiLanguageInput"],
        model_version: Optional[str] = None,
        show_stats: Optional[bool] = None,
        **kwargs
    ) -> "_models.KeyPhraseResult":
        """Key Phrases.

        The API returns a list of strings denoting the key phrases in the input text. See the :code:`<a
        href="https://aka.ms/talangs">Supported languages in Text Analytics API</a>` for the list of
        enabled languages.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_1_preview_2.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics.
        :type show_stats: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: KeyPhraseResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_1_preview_2.models.KeyPhraseResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.KeyPhraseResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _input = _models.MultiLanguageBatchInput(documents=documents)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.key_phrases.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if model_version is not None:
            query_parameters['model-version'] = self._serialize.query("model_version", model_version, 'str')
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_input, 'MultiLanguageBatchInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('KeyPhraseResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    key_phrases.metadata = {'url': '/keyPhrases'}  # type: ignore


    async def languages(
        self,
        documents: List["_models.LanguageInput"],
        model_version: Optional[str] = None,
        show_stats: Optional[bool] = None,
        **kwargs
    ) -> "_models.LanguageResult":
        """Detect Language.

        The API returns the detected language and a numeric score between 0 and 1. Scores close to 1
        indicate 100% certainty that the identified language is true. See the :code:`<a
        href="https://aka.ms/talangs">Supported languages in Text Analytics API</a>` for the list of
        enabled languages.

        :param documents:
        :type documents: list[~azure.ai.textanalytics.v3_1_preview_2.models.LanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics.
        :type show_stats: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LanguageResult, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_1_preview_2.models.LanguageResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LanguageResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _input = _models.LanguageBatchInput(documents=documents)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.languages.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if model_version is not None:
            query_parameters['model-version'] = self._serialize.query("model_version", model_version, 'str')
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_input, 'LanguageBatchInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('LanguageResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    languages.metadata = {'url': '/languages'}  # type: ignore


    async def sentiment(
        self,
        documents: List["_models.MultiLanguageInput"],
        model_version: Optional[str] = None,
        show_stats: Optional[bool] = None,
        opinion_mining: Optional[bool] = None,
        string_index_type: Optional[Union[str, "_models.StringIndexType"]] = "TextElements_v8",
        **kwargs
    ) -> "_models.SentimentResponse":
        """Sentiment.

        The API returns a detailed sentiment analysis for the input text. The analysis is done in
        multiple levels of granularity, start from the a document level, down to sentence and key terms
        (aspects) and opinions.

        :param documents: The set of documents to process as part of this batch.
        :type documents: list[~azure.ai.textanalytics.v3_1_preview_2.models.MultiLanguageInput]
        :param model_version: (Optional) This value indicates which model will be used for scoring. If
         a model-version is not specified, the API should default to the latest, non-preview version.
        :type model_version: str
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics.
        :type show_stats: bool
        :param opinion_mining: (Optional) if set to true, response will contain input and document
         level statistics including aspect-based sentiment analysis results.
        :type opinion_mining: bool
        :param string_index_type: (Optional) Specifies the method used to interpret string offsets.
         Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information
         see https://aka.ms/text-analytics-offsets.
        :type string_index_type: str or ~azure.ai.textanalytics.v3_1_preview_2.models.StringIndexType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SentimentResponse, or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v3_1_preview_2.models.SentimentResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SentimentResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _input = _models.MultiLanguageBatchInput(documents=documents)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.sentiment.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if model_version is not None:
            query_parameters['model-version'] = self._serialize.query("model_version", model_version, 'str')
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')
        if opinion_mining is not None:
            query_parameters['opinionMining'] = self._serialize.query("opinion_mining", opinion_mining, 'bool')
        if string_index_type is not None:
            query_parameters['stringIndexType'] = self._serialize.query("string_index_type", string_index_type, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_input, 'MultiLanguageBatchInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SentimentResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    sentiment.metadata = {'url': '/sentiment'}  # type: ignore

