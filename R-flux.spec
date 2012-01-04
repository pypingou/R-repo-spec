%global packname  flux
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Flux rate calculation from dynamic closed chamber measurements

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-caTools 


BuildRequires:    R-devel tex(latex) R-caTools



%description
Functions for the calculation of greenhouse gas flux rates from closed
chamber concentration measurements. The package follows a modular concept:
Fluxes can be calculated in just two simple steps or in several steps if
more control in details is wanted. Additionaly plot and preparation
functions are provided.

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
%doc %{rlibdir}/flux/html
%doc %{rlibdir}/flux/DESCRIPTION
%{rlibdir}/flux/INDEX
%{rlibdir}/flux/help
%{rlibdir}/flux/ChangeLog
%{rlibdir}/flux/data
%{rlibdir}/flux/NAMESPACE
%{rlibdir}/flux/Meta
%{rlibdir}/flux/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora