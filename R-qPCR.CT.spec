%global packname  qPCR.CT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          qPCR data analysis and plot package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-RColorBrewer 


BuildRequires:    R-devel tex(latex) R-RColorBrewer



%description
use 2^ddCT methods calculate the relative gene expression, data file can
be export from bio-rad qpcr machine, the results can be plot with
errorbar. ver 1.1 add GroupPlot function, can plot all the groups once.

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
%doc %{rlibdir}/qPCR.CT/html
%doc %{rlibdir}/qPCR.CT/DESCRIPTION
%{rlibdir}/qPCR.CT/help
%{rlibdir}/qPCR.CT/data
%{rlibdir}/qPCR.CT/Meta
%{rlibdir}/qPCR.CT/INDEX
%{rlibdir}/qPCR.CT/R
%{rlibdir}/qPCR.CT/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora