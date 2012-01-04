%global packname  kerdiest
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Nonparametric kernel estimation of the distribution function. Bandwidth selection and estimation of related functions.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-date R-chron 

BuildRequires:    R-devel tex(latex) R-date R-chron 

%description
Nonparametric kernel distribution function estimation is performed. Three
automatic bandwidth selection methods for nonparametric kernel
distribution function estimation are implemented: the plug-in of Altman
and Leger, the plug-in of Polansky and Baker, and the modified
cross-validation of Bowman, Hall and Prvan. The exceedence function, the
mean return period and the return level are also computed.

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
%doc %{rlibdir}/kerdiest/html
%doc %{rlibdir}/kerdiest/DESCRIPTION
%{rlibdir}/kerdiest/R
%{rlibdir}/kerdiest/NAMESPACE
%{rlibdir}/kerdiest/help
%{rlibdir}/kerdiest/INDEX
%{rlibdir}/kerdiest/Meta
%{rlibdir}/kerdiest/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora