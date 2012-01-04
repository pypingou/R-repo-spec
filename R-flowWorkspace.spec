%global packname  flowWorkspace
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Import flowJo Workspaces into BioConductor and replicate flowJo gating with flowCore

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-RBGL R-graph R-XML R-flowCore R-flowViz R-Rgraphviz R-Biobase R-IDPmisc 

BuildRequires:    R-devel tex(latex) R-methods R-RBGL R-graph R-XML R-flowCore R-flowViz R-Rgraphviz R-Biobase R-IDPmisc 

%description
This package is designed to facilitate comparison of automated gating
methods against manual gating done in flowJo. This package allows you to
import basic flowJo workspaces into BioConductor and replicate the gating
from flowJo using the flowCore functionality. Gating hierarchies, groups
of samples, compensation, and transformation are performed so that the
output matches the flowJo analysis.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora