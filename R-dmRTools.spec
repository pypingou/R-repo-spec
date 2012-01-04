%global packname  dmRTools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Data Management Reporting Tool Version 1.0.1

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-chron R-RgoogleMaps R-rgdal R-sp R-sqldf R-xtable R-utils 


BuildRequires:    R-devel tex(latex) R-chron R-RgoogleMaps R-rgdal R-sp R-sqldf R-xtable R-utils



%description
Data Management Reporting Tools This package can be used for a clinical
trials data management systems. The clinical trial data could be monitored
for accrual and performance of the sites. The details of the data
collection process can be examined during the trial.  The ancestor of this
package called "dfRTools" specifically designed to be used for Clinical
DataFax System (http://www.datafax.com).

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora