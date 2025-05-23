# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest

class ConfidentialLedgerTests(ScenarioTest):

    @AllowLargeResponse(size_kb=10240)
    def test_list_bysubscription_confidentialledger(self):
        accounts_list = self.cmd('az confidentialledger list').get_output_in_json()
        assert len(accounts_list) > 0

    @AllowLargeResponse(size_kb=10240)
    def test_list_byresourcegroup_confidentialledger(self):
        self.kwargs.update({
            'rg': 'AzCliExtensionRg',
        })
        accounts_list = self.cmd('az confidentialledger list --resource-group {rg}').get_output_in_json()
        assert len(accounts_list) > 0

    @AllowLargeResponse(size_kb=10240)
    def test_show_confidentialledger(self):
        self.kwargs.update({
            'ledger_name': 'azclitest1',
            'rg': 'AzCliExtensionRg',
        })
        self.cmd('az confidentialledger show --name {ledger_name} --resource-group {rg}', checks=[
            self.check('name', '{ledger_name}'),
            self.check('resourceGroup', '{rg}')
        ])

    @AllowLargeResponse(size_kb=10240)
    def test_create_confidentialledger(self):
        self.kwargs.update({
            'ledger_name': 'azclitest',
            'rg': 'AzCliExtensionRg',
            'location': 'eastus',
            'ledger_type': 'Public',
        })
        self.cmd('az confidentialledger create --name {ledger_name} --resource-group {rg} --location {location} --ledger-type {ledger_type}', checks=[
            self.check('name', '{ledger_name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('location', '{location}'),
            self.check('properties.ledgerType', '{ledger_type}')
        ])

    @AllowLargeResponse(size_kb=10240)
    def test_update_confidentialledger(self):
        self.kwargs.update({
            'ledger_name': 'azclitest',
            'rg': 'AzCliExtensionRg',
            'location': 'eastus',
            'ledger-role-name': 'Administrator',
            'principal-id': '78945818-3e7d-4708-bd84-3a480f1fbeb5',
            'tenant-id': '72f988bf-86f1-41af-91ab-2d7cd011db47',
        })
        self.cmd('az confidentialledger update --name {ledger_name} --resource-group {rg} ' 
                 '--aad-based-security-principals "[{{\'principal-id\':{principal-id},\'tenant-id\':{tenant-id},\'ledger-role-name\':{ledger-role-name}}}]"', 
        checks=[
            self.check('name', '{ledger_name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('location', '{location}'),
            self.check('properties.aadBasedSecurityPrincipals[?principalId==\'{principal-id}\'].ledgerRoleName | [0]', '{ledger-role-name}'),
            self.check('properties.aadBasedSecurityPrincipals[?principalId==\'{principal-id}\'].principalId | [0]', '{principal-id}'),
            self.check('properties.aadBasedSecurityPrincipals[?principalId==\'{principal-id}\'].tenantId | [0]', '{tenant-id}'),
        ])

    @AllowLargeResponse(size_kb=10240)
    def test_delete_confidentialledger(self):
        self.kwargs.update({
            'ledger_name': 'azclitest',
            'rg': 'AzCliExtensionRg',
        })
        self.cmd('az confidentialledger delete --name {ledger_name} --resource-group {rg} --yes')

    @AllowLargeResponse(size_kb=10240)
    def test_checknameavailability_confidentialledger(self):
        self.kwargs.update({
            'ledger_name': 'azclitest',
            'type': 'Microsoft.ConfidentialLedger/Ledgers',
            'rg': 'AzCliExtensionRg',
        })
        self.cmd('az confidentialledger check-name-availability --type {type} --name {ledger_name}', checks=[
            self.check('nameAvailable', 'True')
        ])
