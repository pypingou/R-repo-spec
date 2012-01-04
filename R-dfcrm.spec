%global packname  dfcrm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Dose-finding by the continual reassessment method

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides functions to run the CRM and TITE-CRM in phase I
trials and calibration tools for trial planning purposes.

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
%doc %{rlibdir}/dfcrm/html
%doc %{rlibdir}/dfcrm/DESCRIPTION
%{rlibdir}/dfcrm/NAMESPACE
%{rlibdir}/dfcrm/INDEX
%{rlibdir}/dfcrm/R
%{rlibdir}/dfcrm/help
%{rlibdir}/dfcrm/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora