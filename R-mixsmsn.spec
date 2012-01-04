%global packname  mixsmsn
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Fitting finite mixture of scale mixture of skew-normal distributions .

Group:            Applications/Engineering 
License:          GPL (>= 3.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Functions to fit finite mixture of scale mixture of skew-normal (FM-SMSN)

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
%doc %{rlibdir}/mixsmsn/html
%doc %{rlibdir}/mixsmsn/DESCRIPTION
%{rlibdir}/mixsmsn/data
%{rlibdir}/mixsmsn/Meta
%{rlibdir}/mixsmsn/R
%{rlibdir}/mixsmsn/NAMESPACE
%{rlibdir}/mixsmsn/INDEX
%{rlibdir}/mixsmsn/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora