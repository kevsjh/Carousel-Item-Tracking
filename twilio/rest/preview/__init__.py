# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.preview.bulk_exports import BulkExports
from twilio.rest.preview.deployed_devices import DeployedDevices
from twilio.rest.preview.hosted_numbers import HostedNumbers
from twilio.rest.preview.marketplace import Marketplace
from twilio.rest.preview.sync import Sync
from twilio.rest.preview.trusted_comms import TrustedComms
from twilio.rest.preview.understand import Understand
from twilio.rest.preview.wireless import Wireless


class Preview(Domain):

    def __init__(self, twilio):
        """
        Initialize the Preview Domain

        :returns: Domain for Preview
        :rtype: twilio.rest.preview.Preview
        """
        super(Preview, self).__init__(twilio)

        self.base_url = 'https://preview.twilio.com'

        # Versions
        self._bulk_exports = None
        self._deployed_devices = None
        self._hosted_numbers = None
        self._marketplace = None
        self._sync = None
        self._understand = None
        self._wireless = None
        self._trusted_comms = None

    @property
    def bulk_exports(self):
        """
        :returns: Version bulk_exports of preview
        :rtype: twilio.rest.preview.bulk_exports.BulkExports
        """
        if self._bulk_exports is None:
            self._bulk_exports = BulkExports(self)
        return self._bulk_exports

    @property
    def deployed_devices(self):
        """
        :returns: Version deployed_devices of preview
        :rtype: twilio.rest.preview.deployed_devices.DeployedDevices
        """
        if self._deployed_devices is None:
            self._deployed_devices = DeployedDevices(self)
        return self._deployed_devices

    @property
    def hosted_numbers(self):
        """
        :returns: Version hosted_numbers of preview
        :rtype: twilio.rest.preview.hosted_numbers.HostedNumbers
        """
        if self._hosted_numbers is None:
            self._hosted_numbers = HostedNumbers(self)
        return self._hosted_numbers

    @property
    def marketplace(self):
        """
        :returns: Version marketplace of preview
        :rtype: twilio.rest.preview.marketplace.Marketplace
        """
        if self._marketplace is None:
            self._marketplace = Marketplace(self)
        return self._marketplace

    @property
    def sync(self):
        """
        :returns: Version sync of preview
        :rtype: twilio.rest.preview.sync.Sync
        """
        if self._sync is None:
            self._sync = Sync(self)
        return self._sync

    @property
    def understand(self):
        """
        :returns: Version understand of preview
        :rtype: twilio.rest.preview.understand.Understand
        """
        if self._understand is None:
            self._understand = Understand(self)
        return self._understand

    @property
    def wireless(self):
        """
        :returns: Version wireless of preview
        :rtype: twilio.rest.preview.wireless.Wireless
        """
        if self._wireless is None:
            self._wireless = Wireless(self)
        return self._wireless

    @property
    def trusted_comms(self):
        """
        :returns: Version trusted_comms of preview
        :rtype: twilio.rest.preview.trusted_comms.TrustedComms
        """
        if self._trusted_comms is None:
            self._trusted_comms = TrustedComms(self)
        return self._trusted_comms

    @property
    def exports(self):
        """
        :rtype: twilio.rest.preview.bulk_exports.export.ExportList
        """
        return self.bulk_exports.exports

    @property
    def export_configuration(self):
        """
        :rtype: twilio.rest.preview.bulk_exports.export_configuration.ExportConfigurationList
        """
        return self.bulk_exports.export_configuration

    @property
    def fleets(self):
        """
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetList
        """
        return self.deployed_devices.fleets

    @property
    def authorization_documents(self):
        """
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentList
        """
        return self.hosted_numbers.authorization_documents

    @property
    def hosted_number_orders(self):
        """
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderList
        """
        return self.hosted_numbers.hosted_number_orders

    @property
    def available_add_ons(self):
        """
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnList
        """
        return self.marketplace.available_add_ons

    @property
    def installed_add_ons(self):
        """
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnList
        """
        return self.marketplace.installed_add_ons

    @property
    def services(self):
        """
        :rtype: twilio.rest.preview.sync.service.ServiceList
        """
        return self.sync.services

    @property
    def assistants(self):
        """
        :rtype: twilio.rest.preview.understand.assistant.AssistantList
        """
        return self.understand.assistants

    @property
    def commands(self):
        """
        :rtype: twilio.rest.preview.wireless.command.CommandList
        """
        return self.wireless.commands

    @property
    def rate_plans(self):
        """
        :rtype: twilio.rest.preview.wireless.rate_plan.RatePlanList
        """
        return self.wireless.rate_plans

    @property
    def sims(self):
        """
        :rtype: twilio.rest.preview.wireless.sim.SimList
        """
        return self.wireless.sims

    @property
    def branded_calls(self):
        """
        :rtype: twilio.rest.preview.trusted_comms.branded_call.BrandedCallList
        """
        return self.trusted_comms.branded_calls

    @property
    def brands_information(self):
        """
        :rtype: twilio.rest.preview.trusted_comms.brands_information.BrandsInformationList
        """
        return self.trusted_comms.brands_information

    @property
    def businesses(self):
        """
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessList
        """
        return self.trusted_comms.businesses

    @property
    def cps(self):
        """
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsList
        """
        return self.trusted_comms.cps

    @property
    def current_calls(self):
        """
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallList
        """
        return self.trusted_comms.current_calls

    @property
    def phone_calls(self):
        """
        :rtype: twilio.rest.preview.trusted_comms.phone_call.PhoneCallList
        """
        return self.trusted_comms.phone_calls

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview>'
